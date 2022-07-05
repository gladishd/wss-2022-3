import pygame
import math


# Create a new surface and window.
surface = pygame.display.set_mode([800,800])

def tree_fractal(order, angle, size, posn, heading, color, depth=0):
   trunk_ratio = 0.29       # How big is the trunk relative to whole tree?
   trunk = size * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(surface, color, posn, newpos)

   if order > 0:   # Draw another layer of subtrees
      # Recursively draws the two halves of the tree
      tree_fractal(order-1, angle, size*(1 - trunk_ratio), newpos, heading-angle, (255,0,0), depth+1)
      tree_fractal(order-1, angle, size*(1 - trunk_ratio), newpos, heading+angle, color, depth+1)

def draw_tree():
    pygame.init()   # Initialize Pygame
    angle = 20
    while True:

        # Handle events from keyboard, mouse, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: #scroll up
            angle += 0.1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: #scroll down
            angle -= 0.1

        # Draw everything
        surface.fill((0, 0, 0))
        tree_fractal(6, angle, 800*0.9, (800//2, 800-50), -math.pi/2, (255,255,255))

        pygame.display.flip()





def random(order, angle, size, posn, heading, color, depth=0):
   delta_x = 50*math.cos(heading)
   delta_y = 50*math.sin(heading)
   u = 400
   v = 400
   (u, v) = posn
   c1 = 50 * math.cos(heading+math.pi/9)
   c2 = 50 * math.sin(heading+math.pi/9)
   c3 = 50 * math.cos(heading+2*math.pi/9)
   c4 = 50 * math.sin(heading+2*math.pi/9)
   
   
   c5 = 50 * math.cos(heading-math.pi/9)
   c6 = 50 * math.sin(heading-math.pi/9)
   c7 = 50 * math.cos(heading-2*math.pi/9)
   c8 = 50 * math.sin(heading-2*math.pi/9)
   if order > 0:   #
      if order & 1 == 0:
            c1 = 50 * math.cos(heading-math.pi/9)
            c2 = 50 * math.sin(heading-math.pi/9)
            c3 = 50 * math.cos(heading-2*math.pi/9)
            c4 = 50 * math.sin(heading-2*math.pi/9)
      else:
            c1 = 50 * math.cos(heading+math.pi/9)
            c2 = 50 * math.sin(heading+math.pi/9)
            c3 = 50 * math.cos(heading+2*math.pi/9)
            c4 = 50 * math.sin(heading+2*math.pi/9)

   newpos = (u + delta_x, v + delta_y)
   newpos2 = (newpos[0] + c1, newpos[1] + c2)
   newpos3 = (newpos2[0] + c3, newpos2[1] + c4)
   

   
   pygame.draw.line(surface, color, posn, newpos)
   pygame.draw.line(surface, color, newpos, newpos2)
   pygame.draw.line(surface, color, newpos2, newpos3)
   

   
   
   if order > 0:
        random(order-1, angle, size, newpos, heading-angle, color, depth+1)

#   if order > 0:   
#      if order & 1 == 0:
#            random(order-1, angle + math.pi/3, size, newpos3, heading-angle, color, depth+1)
#      else:
#            random(order-1, angle - math.pi/3, size, newpos3, heading+angle, color, depth+1)

def draw_random():
    pygame.init()   # Initialize Pygame
    angle = math.pi/2
    while True:

        # Handle events from keyboard, mouse, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: #scroll up
            angle += 0.1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: #scroll down
            angle -= 0.1
        #angle += 0.01
        # Draw everything
        surface.fill((255, 255, 255))
        random(800, angle, 800*0.2, (400, 400), math.pi, (0,0,0))

        pygame.display.flip()



def sierpinski(order, angle, size, posn, heading, color, depth=0):
   delta_x = 50*math.cos(heading)
   delta_y = 50*math.sin(heading)
   u = 400
   v = 400
   (u, v) = posn
   c1 = 50 * math.cos(heading+math.pi/3)
   c2 = 50 * math.sin(heading+math.pi/3)
   c3 = 50 * math.cos(heading+2*math.pi/3)
   c4 = 50 * math.sin(heading+2*math.pi/3)
   if order > 0:   #
      if order & 1 == 0:
            c1 = 50 * math.cos(heading-math.pi/3)
            c2 = 50 * math.sin(heading-math.pi/3)
            c3 = 50 * math.cos(heading-2*math.pi/3)
            c4 = 50 * math.sin(heading-2*math.pi/3)
      else:
            c1 = 50 * math.cos(heading+math.pi/3)
            c2 = 50 * math.sin(heading+math.pi/3)
            c3 = 50 * math.cos(heading+2*math.pi/3)
            c4 = 50 * math.sin(heading+2*math.pi/3)
   
   

   newpos = (u + delta_x, v + delta_y)
   newpos2 = (newpos[0] + c1, newpos[1] + c2)
   newpos3 = (newpos2[0] + c3, newpos2[1] + c4)
   

   
   pygame.draw.line(surface, color, posn, newpos)
   pygame.draw.line(surface, color, newpos, newpos2)
   pygame.draw.line(surface, color, newpos2, newpos3)
   

   
   
   if order > 0:
        sierpinski(order-1, angle, size, newpos3, heading-angle, color, depth+1)


def draw_sierpinski():
    pygame.init()   # Initialize Pygame
    angle = math.pi/1
    while True:

        # Handle events from keyboard, mouse, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: #scroll up
            angle += 0.1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: #scroll down
            angle -= 0.1
        #angle += 0.01
        # Draw everything
        surface.fill((255, 255, 255))
        sierpinski(5, angle, 800*0.2, (400, 400), math.pi, (0,0,0))

        pygame.display.flip()










def dragon(order, angle, size, posn, heading, color, depth=0):
   u = 400
   v = 400
   (u, v) = posn
   s = 10
#y becomes x, and x becomes negative y when rotating counterclockwise by 90 degrees.
#x becomes y, and y becomes negative x when rotating clockwise by 90 degrees.
   newpos = (u - s, v + s)
   newpos2 = (newpos[0] - s, newpos[1] - s)
#   newpos2 = (newpos[0] - 10*math.cos(heading-angle/.707), newpos[1] - 10*math.sin(heading-angle)/.707)
   if order == 3 or order == 7 or order == 11 or order == 15 or order == 19:
       newpos3 = (newpos2[0] + s, newpos2[1] - s)
       newpos4 = (newpos3[0] - s, newpos3[1] - s)
       newpos5 = (newpos4[0] + s, newpos4[1] - s)
       newpos6 = (newpos5[0] + s, newpos5[1] + s)
       newpos7 = (newpos6[0] + s, newpos6[1] - s)
       newpos8 = (newpos7[0] - s, newpos7[1] - s)
       newpos9 = (newpos8[0] + s, newpos8[1] - s)
       newpos10 = (newpos9[0] + s, newpos9[1] + s)
       newpos11 = (newpos10[0] - s, newpos10[1] + s)
       newpos12 = (newpos11[0] + s, newpos11[1] + s)
       newpos13 = (newpos12[0] + s, newpos12[1] - s)
       newpos14 = (newpos13[0] + s, newpos13[1] + s)
       newpos15 = (newpos14[0] + s, newpos14[1] - s)
       newpos16 = (newpos15[0] - s, newpos15[1] - s)
       newpos17 = (newpos16[0] - s, newpos16[1] + s)
       newpos18 = (newpos17[0] - s, newpos17[1] - s)
       newpos19 = (newpos18[0] + s, newpos18[1] - s)
       newpos20 = (newpos19[0] - s, newpos19[1] - s)
       newpos21 = (newpos20[0] + s, newpos20[1] - s)
       newpos22 = (newpos21[0] + s, newpos21[1] + s)
       newpos23 = (newpos22[0] + s, newpos22[1] - s)
       newpos24 = (newpos23[0] - s, newpos23[1] - s)
       newpos25 = (newpos24[0] - s, newpos24[1] + s)
       newpos26 = (newpos25[0] - s, newpos25[1] - s)
       newpos27 = (newpos26[0] + s, newpos26[1] - s)
       newpos28 = (newpos27[0] - s, newpos27[1] - s)
       newpos29 = (newpos28[0] - s, newpos28[1] + s)
       newpos30 = (newpos29[0] - s, newpos29[1] - s)
       newpos31 = (newpos30[0] - s, newpos30[1] + s)
       newpos32 = (newpos31[0] + s, newpos31[1] + s)
   if order == 2 or order == 6 or order == 10 or order == 14 or order == 18:
       newpos3 = (newpos2[0] + s, newpos2[1] + s)
       newpos4 = (newpos3[0] + s, newpos3[1] - s)
       newpos5 = (newpos4[0] + s, newpos4[1] + s)
       newpos6 = (newpos5[0] - s, newpos5[1] + s)
       newpos7 = (newpos6[0] + s, newpos6[1] + s)
       newpos8 = (newpos7[0] + s, newpos7[1] - s)
       newpos9 = (newpos8[0] + s, newpos8[1] + s)
       newpos10 = (newpos9[0] - s, newpos9[1] + s)
       newpos11 = (newpos10[0] - s, newpos10[1] - s)
       newpos12 = (newpos11[0] - s, newpos11[1] + s)
       newpos13 = (newpos12[0] + s, newpos12[1] + s)
       newpos14 = (newpos13[0] - s, newpos13[1] + s)
       newpos15 = (newpos14[0] + s, newpos14[1] + s)
       newpos16 = (newpos15[0] + s, newpos15[1] - s)
       newpos17 = (newpos16[0] - s, newpos16[1] - s)
       newpos18 = (newpos17[0] + s, newpos17[1] - s)
       newpos19 = (newpos18[0] + s, newpos18[1] + s)
       newpos20 = (newpos19[0] + s, newpos19[1] - s)
       newpos21 = (newpos20[0] + s, newpos20[1] + s)
       newpos22 = (newpos21[0] - s, newpos21[1] + s)
       newpos23 = (newpos22[0] + s, newpos22[1] + s)
       newpos24 = (newpos23[0] + s, newpos23[1] - s)
       newpos25 = (newpos24[0] - s, newpos24[1] - s)
       newpos26 = (newpos25[0] + s, newpos25[1] - s)
       newpos27 = (newpos26[0] + s, newpos26[1] + s)
       newpos28 = (newpos27[0] + s, newpos27[1] - s)
       newpos29 = (newpos28[0] - s, newpos28[1] - s)
       newpos30 = (newpos29[0] + s, newpos29[1] - s)
       newpos31 = (newpos30[0] - s, newpos30[1] - s)
       newpos32 = (newpos31[0] - s, newpos31[1] + s)
   if order == 1 or order == 5 or order == 9 or order == 13 or order == 17:
       newpos3 = (newpos2[0] - s, newpos2[1] + s)
       newpos4 = (newpos3[0] + s, newpos3[1] + s)
       newpos5 = (newpos4[0] - s, newpos4[1] + s)
       newpos6 = (newpos5[0] - s, newpos5[1] - s)
       newpos7 = (newpos6[0] - s, newpos6[1] + s)
       newpos8 = (newpos7[0] + s, newpos7[1] + s)
       newpos9 = (newpos8[0] - s, newpos8[1] + s)
       newpos10 = (newpos9[0] - s, newpos9[1] - s)
       newpos11 = (newpos10[0] + s, newpos10[1] - s)
       newpos12 = (newpos11[0] - s, newpos11[1] - s)
       newpos13 = (newpos12[0] - s, newpos12[1] + s)
       newpos14 = (newpos13[0] - s, newpos13[1] - s)
       newpos15 = (newpos14[0] - s, newpos14[1] + s)
       newpos16 = (newpos15[0] + s, newpos15[1] + s)
       newpos17 = (newpos16[0] + s, newpos16[1] - s)
       newpos18 = (newpos17[0] + s, newpos17[1] + s)
       newpos19 = (newpos18[0] - s, newpos18[1] + s)
       newpos20 = (newpos19[0] + s, newpos19[1] + s)
       newpos21 = (newpos20[0] - s, newpos20[1] + s)
       newpos22 = (newpos21[0] - s, newpos21[1] - s)
       newpos23 = (newpos22[0] - s, newpos22[1] + s)
       newpos24 = (newpos23[0] + s, newpos23[1] + s)
       newpos25 = (newpos24[0] + s, newpos24[1] - s)
       newpos26 = (newpos25[0] + s, newpos25[1] + s)
       newpos27 = (newpos26[0] - s, newpos26[1] + s)
       newpos28 = (newpos27[0] + s, newpos27[1] + s)
       newpos29 = (newpos28[0] + s, newpos28[1] - s)
       newpos30 = (newpos29[0] + s, newpos29[1] + s)
       newpos31 = (newpos30[0] + s, newpos30[1] - s)
       newpos32 = (newpos31[0] - s, newpos31[1] - s)
   if order == 0 or order == 4 or order == 8 or order == 12 or order == 16:
       newpos3 = (newpos2[0] - s, newpos2[1] - s)
       newpos4 = (newpos3[0] - s, newpos3[1] + s)
       newpos5 = (newpos4[0] - s, newpos4[1] - s)
       newpos6 = (newpos5[0] + s, newpos5[1] - s)
       newpos7 = (newpos6[0] - s, newpos6[1] - s)
       newpos8 = (newpos7[0] - s, newpos7[1] + s)
       newpos9 = (newpos8[0] - s, newpos8[1] - s)
       newpos10 = (newpos9[0] + s, newpos9[1] - s)
       newpos11 = (newpos10[0] + s, newpos10[1] + s)
       newpos12 = (newpos11[0] + s, newpos11[1] - s)
       newpos13 = (newpos12[0] - s, newpos12[1] - s)
       newpos14 = (newpos13[0] + s, newpos13[1] - s)
       newpos15 = (newpos14[0] - s, newpos14[1] - s)
       newpos16 = (newpos15[0] - s, newpos15[1] + s)
       newpos17 = (newpos16[0] + s, newpos16[1] + s)
       newpos18 = (newpos17[0] - s, newpos17[1] + s)
       newpos19 = (newpos18[0] - s, newpos18[1] - s)
       newpos20 = (newpos19[0] - s, newpos19[1] + s)
       newpos21 = (newpos20[0] - s, newpos20[1] - s)
       newpos22 = (newpos21[0] + s, newpos21[1] - s)
       newpos23 = (newpos22[0] - s, newpos22[1] - s)
       newpos24 = (newpos23[0] - s, newpos23[1] + s)
       newpos25 = (newpos24[0] + s, newpos24[1] + s)
       newpos26 = (newpos25[0] - s, newpos25[1] + s)
       newpos27 = (newpos26[0] - s, newpos26[1] - s)
       newpos28 = (newpos27[0] - s, newpos27[1] + s)
       newpos29 = (newpos28[0] + s, newpos28[1] + s)
       newpos30 = (newpos29[0] - s, newpos29[1] + s)
       newpos31 = (newpos30[0] + s, newpos30[1] + s)
       newpos32 = (newpos31[0] + s, newpos31[1] - s)
   lst = {1: posn, 2: newpos, 3: newpos2, 4: newpos3, 5: newpos4, 6: newpos5, 7: newpos6, 8: newpos7, 9: newpos8, 10: newpos9, 11: newpos10, 12: newpos11, 13: newpos12, 14: newpos13, 15: newpos14, 16: newpos15, 17: newpos16, 18: newpos17, 19: newpos18, 20: newpos19, 21: newpos20, 22: newpos21, 23: newpos22, 24: newpos23, 25: newpos24, 26: newpos25, 27: newpos26, 28: newpos27, 29: newpos28, 30: newpos29, 31: newpos30, 32: newpos31, 33: newpos32}
   for i in range(2, 34):
      pygame.draw.line(surface, color, lst[i-1], lst[i])


   if order > 0:
        dragon(order-1, angle, size, newpos31, heading-math.pi/3, color, depth+1)


def draw_dragon():
    pygame.init()   # Initialize Pygame
    angle = math.pi/1
    order = 2
    bg = (255, 255, 255)
    color = (0,0,0)
    s = 10
    while True:

        # Handle events from keyboard, mouse, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and order >= 0 and order <= 18: #scroll up
            order += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and order >= 1 and order <= 19: #scroll down
            order -= 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = (255, 255, 255)
            if event.key == pygame.K_2:
                color = (0, 0, 0)
            if event.key == pygame.K_3:
                color = (255, 0, 0)
            if event.key == pygame.K_4:
                color = (0, 255, 0)
            if event.key == pygame.K_5:
                color = (0, 0, 255)
            if event.key == pygame.K_6:
                color = (0, 255, 255)
            if event.key == pygame.K_7:
                color = (255, 0, 255)
            if event.key == pygame.K_8:
                color = (255, 255, 0)
            if event.key == pygame.K_9:
                bg = (0, 0, 0)
            if event.key == pygame.K_0:
                bg = (255, 255, 255)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                s += 0.1
            elif event.button == 5:
                s -= 0.1
            
                
            
        #angle += 0.01
        # Draw everything
        surface.fill(bg)
        dragon(order, angle, 800*0.2, (400, 400), math.pi, color)

        pygame.display.flip()

fractal = input('Choose a fractal from the list: Tree, Dragon, ???')
if fractal == 'Tree':
    draw_tree()
elif fractal == 'Dragon':
    draw_dragon()
elif fractal == '???':
    draw_random()