from time import sleep, time
import sys
import os
from os import system
import os

sys.path.insert(0, './replays')

nons = -1+int(input("Which game u want to see: "))
replay = 'replays/replay' + str(len( os.listdir('replays') ) - nons) + '.txt'


with open( replay, "r") as replayfiles:
    for index in replayfiles:
        if index.strip() == "format":
            sleep(0.2)
            system("clear")
        else:
            print(index, end="")