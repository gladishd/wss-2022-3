from pycosat import itersolve   # https://pypi.python.org/pypi/pycosat
from itertools import combinations
from sys import intern
from pprint import pprint


# SAT Utility Functions solve_one, from_dnf, one_of, https://github.com/redmage123/problem_solvers/blob/master/src/sat_utils.py.


class Q:
    'Quantifier for the number of elements that are true'

    def __init__(self, elements):
        self.elements = tuple(elements)

    def __lt__(self, n: int) -> 'cnf':
        return list(combinations(map(neg, self.elements), n))

    def __le__(self, n: int) -> 'cnf':
        return self < n + 1

    def __gt__(self, n: int) -> 'cnf':
        return list(combinations(self.elements, len(self.elements)-n))

    def __ge__(self, n: int) -> 'cnf':
        return self > n - 1

    def __eq__(self, n: int) -> 'cnf':
        return (self <= n) + (self >= n)

    def __ne__(self, n) -> 'cnf':
        raise NotImplementedError

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(elements={self.elements!r})'


def neg(element) -> 'element':
    'Negate a single element'
    return intern(element[1:] if element.startswith('~') else '~' + element)


def one_of(elements) -> 'cnf':
    'Exactly one of the elements is true'
    return Q(elements) == 1


def from_dnf(groups) -> 'cnf':
    'Convert from or-of-ands to and-of-ors'
    cnf = {frozenset()}
    for group in groups:
        nl = {frozenset([literal]): neg(literal) for literal in group}
        # The "clause | literal" prevents dup lits: {x, x, y} -> {x, y}
        # The nl check skips over identities: {x, ~x, y} -> True
        cnf = {clause | literal for literal in nl for clause in cnf
               if nl[literal] not in clause}
        # The sc check removes clauses with superfluous terms:
        #     {{x}, {x, z}, {y, z}} -> {{x}, {y, z}}
        # Should this be left until the end?
        sc = min(cnf, key=len)          # XXX not deterministic
        cnf -= {clause for clause in cnf if clause > sc}
    return list(map(tuple, cnf))


def make_translate(cnf):
    """Make translator from symbolic CNF to PycoSat's numbered clauses.
       Return a literal to number dictionary and reverse lookup dict
        >>> make_translate([['~a', 'b', '~c'], ['a', '~c']])
        ({'a': 1, 'c': 3, 'b': 2, '~a': -1, '~b': -2, '~c': -3},
         {1: 'a', 2: 'b', 3: 'c', -1: '~a', -3: '~c', -2: '~b'})
    """
    lit2num = {}
    for clause in cnf:
        for literal in clause:
            if literal not in lit2num:
                var = literal[1:] if literal[0] == '~' else literal
                num = len(lit2num) // 2 + 1
                lit2num[intern(var)] = num
                lit2num[intern('~' + var)] = -num
    num2var = {num: lit for lit, num in lit2num.items()}
    return lit2num, num2var


def translate(cnf, uniquify=False):
    'Translate a symbolic cnf to a numbered cnf and return a reverse mapping'
    # DIMACS CNF file format:
    # http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html
    if uniquify:
        cnf = list(dict.fromkeys(cnf))
    lit2num, num2var = make_translate(cnf)
    numbered_cnf = [tuple([lit2num[lit] for lit in clause]) for clause in cnf]
    return numbered_cnf, num2var


def lookup_itersolve(symbolic_cnf, include_neg=False):
    numbered_cnf, num2var = translate(symbolic_cnf)
    for solution in itersolve(numbered_cnf):
        yield [num2var[n] for n in solution if include_neg or n > 0]


def solve_one(symcnf, include_neg=False):
    return next(lookup_itersolve(symcnf, include_neg))


# SAT Solver Solution to the Einstein Puzzle, https://rhettinger.github.io/einstein.html.


houses = ['1',          '2',      '3',           '4',         '5']

groups = [
    ['Red',    'Green',    'Ivory',       'Yellow',     'Blue'],
    ['Englishman',      'Spaniard',   'Ukrainian',       'Japanese', 'Norwegian'],
    ['Coffee',     'Tea',    'Milk',        'Orange juice',    'Water'],
    ['Old Gold', 'Kools', 'Lucky Strike', 'Parliament',   'Chesterfield'],
    ['Dog',     'Snails',    'Zebra',        'Horse',      'Fox'],
]

values = [value for group in groups for value in group]


def comb(value, house):
    'Format how a value is shown at a given house'
    return intern(f'{value} {house}')


def found_at(value, house):
    'Value known to be at a specific house'
    return [(comb(value, house),)]


def same_house(value1, value2):
    'The two values occur in the same house:  Englishman1 & red1 | Englishman2 & red2 ...'
    return from_dnf([(comb(value1, i), comb(value2, i)) for i in houses])


def consecutive(value1, value2):
    'The values are in consecutive houses:  green1 & white2 | green2 & white3 ...'
    return from_dnf([(comb(value1, i), comb(value2, j))
                     for i, j in zip(houses, houses[1:])])


def beside(value1, value2):
    'The values occur side-by-side: blends1 & fox2 | blends2 & fox1 ...'
    return from_dnf([(comb(value1, i), comb(value2, j))
                     for i, j in zip(houses, houses[1:])] +
                    [(comb(value2, i), comb(value1, j))
                     for i, j in zip(houses, houses[1:])]
                    )


cnf = []

# each house gets exactly one value from each attribute group
for house in houses:
    for group in groups:
        cnf += one_of(comb(value, house) for value in group)

# each value gets assigned to exactly one house
for value in values:
    cnf += one_of(comb(value, house) for house in houses)


# The Englishman lives in the Red house.
cnf += same_house('Englishman', 'Red')
cnf += same_house('Spaniard', 'Dog')  # The Spaniard owns the Dog.
cnf += same_house('Coffee', 'Green')  # Coffee is drunk in the Green house.
cnf += same_house('Ukrainian', 'Tea')  # The Ukrainian drinks Tea.
# The Green house is immediately to the right of the Ivory house.
cnf += consecutive('Ivory', 'Green')
cnf += same_house('Old Gold', 'Snails')  # The Old Gold smoker owns Snails.
cnf += same_house('Kools', 'Yellow')  # Kools are smoked in the Yellow house.
cnf += found_at('Milk', 3)  # Milk is drunk in the middle house.
cnf += found_at('Norwegian', 1)  # The Norwegian lives in the first house.
# The man who smokes Chesterfields lives in the house next to the man with the Fox.
cnf += beside('Chesterfield', 'Fox')
# Kools are smoked in the house next to the house where the Horse is kept.
cnf += beside('Kools', 'Horse')
# The Lucky Strike smoker drinks Orange juice.
cnf += same_house('Lucky Strike', 'Orange juice')
# The Japanese smokes Parliaments.
cnf += same_house('Japanese', 'Parliament')
# The Norwegian lives next to the Blue house.
cnf += beside('Norwegian', 'Blue')


pprint(solve_one(cnf))
