(* ::Package:: *)

BeginPackage["YaroslavPackage`"];
MiniMap::usage="MiniMap[loc] makes mat tiny map of a location.";
Begin["`Private`"];
MiniMap[loc_]:=GeoGraphics[toLocation[loc],ImageSize->100]
toLocation[loc_]:=Interpreter["Location"][loc]
End[];
EndPackage[];
