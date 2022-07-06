from src.input_ import *
from src.Ground import Village
from os import system
from src.king import king
from src.Barbarians_new import Barbarians
from src.Balloons import Balloon
from src.Archers import Archers

Attacker = input("Choose Character King(k) or Queen(q): ")

village = Village()
comp=0


while(village.ongoing):
    inp = village.king.motion(village, Attacker)
    barbarian = village.barbarians.inc(inp)
    balloon = village.balloons.inc(inp)
    archer = village.archers.inc(inp)
    if(inp == 'q'):
        system("clear")
        comp=1
        break
    else:
        village.render()

if(comp == 1):
    print("Game is paused")
elif(village.win==0):
    print("Defeat")
elif(village.win==3):
    system("clear")
    print("Victory")