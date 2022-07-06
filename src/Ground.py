from colorama import Fore, Back, Style
from os import system
import math
from src.king import king
from src.Barbarians_new import Barbarians
from src.Balloons import Balloon
from src.Archers import Archers
import os
from time import time

class Village():
    def __init__(self):
        self.columns = 200
        self.rows = 45
        self.use = str(len(os.listdir("replays")) + 1)
        self.townhall_xcor = int(self.rows / 2)
        self.townhall_ycor = int(self.columns / 2)
        self.ongoing = 1
        self.start_time =-0.4
        self.balloon_start_time =-0.2
        self.archer_start_time =-0.2
        self.prev_pos = ''
        # canons
        self.cx1 = 30
        self.cy1 = 50
        self.cx2 = 30
        self.cy2 = 180

        self.cx3 = 30 
        self.cy3 = 190
        self.cx4 = 30 
        self.cy4 = 40
        self.cdamage = 1
        self.crange = 3
        self.chealth = 10
        self.chealth1 = 10
        self.chealth2 = 10
        self.chealth3 = 10 
        self.ArcherHealth = [10,10,10]
        self.kingh = 20
        self.copyx = int(self.rows / 2)
        self.copyy = int(self.columns / 2)
        self.huts_xcor1 = 4
        self.huts_xcor2 = 8
        self.huts_xcor3 = 12
        self.huts_xcor4 = 16
        self.huts_xcor5 = 20
        self.huts_xcor6 = 24

        self.huts_ycor = 120

        self.hut_maxlife = 20
        self.hut1_life = 20
        self.hut2_life = 20
        self.hut3_life = 20
        self.hut4_life = 20
        self.hut5_life = 20
        self.hut6_life = 20

        self.wtx1 = 20
        self.wty1 = 50
        self.wtx2 = 20
        self.wty2 = 180
        self.wtx3 = 20
        self.wty3 = 190
        self.wtx4 = 20
        self.wty4 = 40
        self.wt_health1 = 10
        self.wt_health2 = 10
        self.wt_health3 = 10
        self.wt_health4 = 10
        self.wt_color1 = Back.CYAN + " " + Style.RESET_ALL
        self.wt_color2 = Back.CYAN + " " + Style.RESET_ALL
        self.wt_color3 = Back.CYAN + " " + Style.RESET_ALL
        self.wt_color4 = Back.CYAN + " " + Style.RESET_ALL

        self.background = Back.BLACK + " " + Style.RESET_ALL
        self.huts = Back.GREEN + " " + Style.RESET_ALL
        self.townhall = Back.GREEN + " " + Style.RESET_ALL
        self.cannon = Back.BLUE + " " + Style.RESET_ALL
        self.cannon1 = Back.BLUE + " " + Style.RESET_ALL
        self.cannon2 = Back.BLUE + " " + Style.RESET_ALL
        self.cannon3 = Back.BLUE + " " + Style.RESET_ALL
        self.kingcolor = Back.MAGENTA + " " + Style.RESET_ALL
        self.spawning = Back.RED + " " + Style.RESET_ALL
        self.townwall = Back.WHITE + " " + Style.RESET_ALL

        self.hut1_color = self.huts
        self.hut2_color = self.huts
        self.hut3_color = self.huts
        self.hut4_color = self.huts
        self.hut5_color = self.huts
        self.hut6_color = self.huts

        self.wall1_col = []
        self.wall2_col = []
        self.wall3_col = []
        self.wall4_col = []

        for i in range(9):
            self.wall1_col.append(self.townwall)
            self.wall2_col.append(self.townwall)

        for i in range(10):
            self.wall3_col.append(self.townwall)
            self.wall4_col.append(self.townwall)

        self.king_xcor = 20
        self.king_ycor = 150
        self.king_life = 40
        self.king_damage = 5
        self.queen_damage = 3
        self.king = king(self.king_xcor, self.king_ycor)
        self.barbarians = Barbarians()
        self.balloons = Balloon()
        self.archers = Archers()
        self.win = 0
        self.render()

    def render(self):
        system("clear")
    
        self.ground = [[self.background for i in range(self.columns)] for j in range(self.rows)]
        for i in range(0, 4):
            for j in range(0, 3):
                if(self.townhall_xcor != -1000):
                    self.ground[self.townhall_xcor + i][self.townhall_ycor + j] = self.townhall

        if(self.cx1 != -1000):
            self.ground[self.cx1][self.cy1] = self.cannon
        if(self.cx2 != -1000):
            self.ground[self.cx2][self.cy2] = self.cannon1
        if(self.win >= 1):
            if(self.cx3 != -1000):
                self.ground[self.cx3][self.cy3] = self.cannon2
            if(self.wtx3 != -1000):
                self.ground[self.wtx3][self.wty3] = self.wt_color3
        if(self.win == 2): 
            if(self.cx4 != -1000):
                self.ground[self.cx4][self.cy4] = self.cannon3
            if(self.wtx4 != -1000):
                self.ground[self.wtx4][self.wty4] = self.wt_color4
        if(self.wtx1 != -1000):
            self.ground[self.wtx1][self.wty1] = self.wt_color1
        if(self.wtx2 != -1000):
            self.ground[self.wtx2][self.wty2] = self.wt_color2
        for i in range(0, 1):
            for j in range(0, 1):
                if self.huts_xcor1 != -1000:
                    self.ground[self.huts_xcor1 + i][self.huts_ycor + j] = self.hut1_color
                if self.huts_xcor2 != -1000:
                    self.ground[self.huts_xcor2 + i][self.huts_ycor + j] = self.hut2_color
                if self.huts_xcor3 != -1000:
                    self.ground[self.huts_xcor3 + i][self.huts_ycor + j] = self.hut3_color
                if self.huts_xcor4 != -1000:
                    self.ground[self.huts_xcor4 + i][self.huts_ycor + j] = self.hut4_color
                if self.huts_xcor5 != -1000:
                    self.ground[self.huts_xcor5 + i][self.huts_ycor + j] = self.hut5_color
                if self.huts_xcor6 != -1000:
                    self.ground[self.huts_xcor6 + i][self.huts_ycor + j] = self.hut6_color

        # self.ground[self.townhall_xcor][self.townhall_ycor] = self.background

        for i in range(0, 9):
            # if(self.ground[self.townhall_xcor + 6][self.townhall_ycor -4 + i] ==self.wall1_col[i]):
            # if(self.townhall_xcor != -1000):
                self.ground[self.copyx + 6][self.copyy - 4 + i] = self.wall1_col[i]
                self.ground[self.copyx - 4][self.copyy - 4 + i] = self.wall2_col[i]

        for i in range(0, 10):
            # if(self.townhall_xcor != -1000):
                self.ground[self.copyx - 4 + i][self.copyy - 4] = self.wall3_col[i]
                self.ground[self.copyx - 4 + i][self.copyy + 4] = self.wall4_col[i]


        # self.ground[self.townhall_xcor + 5][self.townhall_ycor + 1] = self.kingcolor
        # if time()-self.la
        
        
        self.ground[self.king_xcor][self.king_ycor] = self.kingcolor
        if(self.barbarians.count_bar > 0): 
            if self.barbarians.activate[0] == 0:
                if(time()-self.start_time>0.4):
                    self.barbarians.Barbarian_movement(self)
                    self.start_time=time()
            if self.barbarians.activate[1] == 0:
                if(time()-self.start_time>0.4):
                    self.start_time=time()
                    self.barbarians.Barbarian_movement(self)
            if self.barbarians.activate[2] == 0:
                if(time()-self.start_time>0.4):
                    self.barbarians.Barbarian_movement(self)
                    self.start_time=time()

            if self.barbarians.activate[0] == 0 :
                self.ground[self.barbarians.bar_xcords[0]][self.barbarians.bar_ycords[0]] = Back.GREEN + " " + Style.RESET_ALL
            if self.barbarians.activate[1] == 0 :
                self.ground[self.barbarians.bar_xcords[1]][self.barbarians.bar_ycords[1]] = Back.GREEN + " " + Style.RESET_ALL
            if self.barbarians.activate[2] == 0 :
                self.ground[self.barbarians.bar_xcords[2]][self.barbarians.bar_ycords[2]] = Back.GREEN + " " + Style.RESET_ALL
        
        if(self.balloons.activate[0] == 0):
            if(time()-self.balloon_start_time>0.2):
                self.balloons.Balloon_movement(self)
                self.balloon_start_time=time()
        if self.balloons.activate[1] == 0:
            if(time()-self.balloon_start_time>0.2):
                self.balloons.Balloon_movement(self)
                self.balloon_start_time=time()
        if self.balloons.activate[2] == 0:
            if(time()-self.balloon_start_time>0.2):
                self.balloons.Balloon_movement(self)
                self.balloon_start_time=time()

        if (self.balloons.activate[0] == 0 or self.balloons.activate[0] == -2):
            self.ground[self.balloons.x_balloon[0]][self.balloons.y_balloon[0]] = Back.YELLOW + " " + Style.RESET_ALL
        if (self.balloons.activate[1] == 0 or self.balloons.activate[1] == -2):
            self.ground[self.balloons.x_balloon[1]][self.balloons.y_balloon[1]] = Back.YELLOW + " " + Style.RESET_ALL
        if (self.balloons.activate[2] == 0 or self.balloons.activate[2] == -2):
            self.ground[self.balloons.x_balloon[2]][self.balloons.y_balloon[2]] = Back.YELLOW + " " + Style.RESET_ALL

        if(self.archers.activate[0] == 0):
            if(time()-self.archer_start_time>0.2):
                self.archers.Archer_movement(self)
                self.archer_start_time=time()
        if self.archers.activate[1] == 0:
            if(time()-self.archer_start_time>0.2):
                self.archers.Archer_movement(self)
                self.archer_start_time=time()
        if self.archers.activate[2] == 0:
            if(time()-self.archer_start_time>0.2):
                self.archers.Archer_movement(self)
                self.archer_start_time=time()

        if self.archers.activate[0] == 0 :
            self.ground[self.archers.x_archers[0]][self.archers.y_archers[0]] = Back.RED + " " + Style.RESET_ALL
        if self.archers.activate[1] == 0 :
            self.ground[self.archers.x_archers[1]][self.archers.y_archers[1]] = Back.RED + " " + Style.RESET_ALL
        if self.archers.activate[2] == 0 :
            self.ground[self.archers.x_archers[2]][self.archers.y_archers[2]] = Back.RED + " " + Style.RESET_ALL


        count = 1

        if self.huts_xcor1 != -1000:
            count = 0
        if self.huts_xcor2 != -1000:
            count = 0
        if self.huts_xcor3 != -1000:
            count = 0
        if self.huts_xcor4 != -1000:
            count = 0
        if self.huts_xcor5 != -1000:
            count = 0
        if self.huts_xcor6 != -1000:
            count = 0

        if (self.king_xcor - self.cx1) ** 2 + (
            self.king_ycor - self.cy1
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        if (self.king_xcor - self.cx3) ** 2 + (
            self.king_ycor - self.cy3
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        if (self.king_xcor - self.cx4) ** 2 + (
            self.king_ycor - self.cy4
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        if (self.king_xcor - self.cx2) ** 2 + (
            self.king_ycor - self.cy2
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        if (self.king_xcor - self.wtx1) ** 2 + (
            self.king_ycor - self.wtx1
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        if (self.king_xcor - self.wtx3) ** 2 + (
            self.king_ycor - self.wty3
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        if (self.king_xcor - self.wtx4) ** 2 + (
            self.king_ycor - self.wty4
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        if (self.king_xcor - self.wtx2) ** 2 + (
            self.king_ycor - self.wty2
        ) ** 2 < self.crange**2:
            self.kingh -= self.cdamage

        for b in range(0,3):
            if(self.balloons.activate[b] == 0):
                if((self.wtx1 - self.balloons.x_balloon[b])**2 + (self.wty1 - self.balloons.y_balloon[b])**2 < self.crange**2):
                    self.balloons.balloonHealth[b] = self.balloons.balloonHealth[b] - self.cdamage
                    if(self.balloons.balloonHealth[b] <= 0): 
                        self.balloons.activate[b] = -2
                if((self.wtx2 - self.balloons.x_balloon[b])**2 + (self.wty2 - self.balloons.y_balloon[b])**2 < self.crange**2):
                    self.balloons.balloonHealth[b] = self.balloons.balloonHealth[b] - self.cdamage
                    if(self.balloons.balloonHealth[b] <= 0): 
                        self.balloons.activate[b] = -2
                if((self.wtx3 - self.balloons.x_balloon[b])**2 + (self.wty3 - self.balloons.y_balloon[b])**2 < self.crange**2):
                    self.balloons.balloonHealth[b] = self.balloons.balloonHealth[b] - self.cdamage
                    if(self.balloons.balloonHealth[b] <= 0): 
                        self.balloons.activate[b] = -2
                if((self.wtx4 - self.balloons.x_balloon[b])**2 + (self.wty4 - self.balloons.y_balloon[b])**2 < self.crange**2):
                    self.balloons.balloonHealth[b] = self.balloons.balloonHealth[b] - self.cdamage
                    if(self.balloons.balloonHealth[b] <= 0): 
                        self.balloons.activate[b] = -2

        title = "Health Bar"
        for j in range(0, len(title)):
            self.ground[40][20+ j] = (
                Back.LIGHTBLUE_EX + Fore.WHITE + title[j] + Style.RESET_ALL)
        
        for i in range(self.kingh):
            self.ground[41][14 + i] = self.spawning

        if count == 1 and self.townhall_xcor == -1000:
            self.win = self.win + 1
            self.chealth = 10
            self.chealth1 = 10 
            self.ArcherHealth = [10,10,10]
            self.kingh = 20 
            self.townhall_xcor = int(self.rows / 2)
            self.townhall_ycor = int(self.columns / 2)
            self.prev_pos = ''
            self.cx1 = 30
            self.cy1 = 50
            self.cx2 = 30
            self.cy2 = 180
            self.cx3 = 30 
            self.cy3 = 190
            self.barbarians.activate = [-1, -1, -1]
            self.cx4 = 30 
            self.cy4 = 40
            self.chealth2 = 10
            self.chealth3 = 10 

            self.wtx1 = 20
            self.wty1 = 50
            self.wtx2 = 20
            self.wty2 = 180
            self.wtx3 = 20
            self.wty3 = 190
            self.wtx4 = 20
            self.wty4 = 40

            self.wt_health1 = 10
            self.wt_health2 = 10
            self.wt_health3 = 10
            self.wt_health4 = 10
            self.wt_color1 = Back.CYAN + " " + Style.RESET_ALL
            self.wt_color2 = Back.CYAN + " " + Style.RESET_ALL
            self.wt_color3 = Back.CYAN + " " + Style.RESET_ALL
            self.wt_color4 = Back.CYAN + " " + Style.RESET_ALL

            self.balloons.activate = [-1,-1,-1]
            self.balloons.x_balloon = [4,5,6]
            self.balloons.y_balloon = [130, 100, 120]
            self.balloons.balloonHealth = [10,10,10]
            self.barbarians.bar_xcords = [3,2,1]
            self.barbarians.bar_ycords = [130, 100, 120]
            self.archers.x_archers = [10,11,14]
            self.archers.y_archers = [130, 140, 120]
            self.archers.activate = [-1, -1, -1]
            if(self.win >= 1 and self.cannon2 == Back.BLUE + " " + Style.RESET_ALL):
                if(self.cx3 != -1000):
                    self.ground[self.cx3][self.cy3] = self.cannon2
            if(self.win >= 1 and self.wt_color3 == Back.CYAN + " " + Style.RESET_ALL):
                if(self.wtx3 != -1000):
                    self.ground[self.wtx3][self.wty3] = self.wt_color3
            if(self.win == 2 and self.wt_color4 == Back.CYAN + " " + Style.RESET_ALL):
                if(self.wtx4 != -1000):
                    self.ground[self.wtx4][self.wty4] = self.wt_color4
            if(self.win == 2 and self.cannon3 == Back.BLUE + " " + Style.RESET_ALL): 
                if(self.cx4 != -1000):
                    self.ground[self.cx4][self.cy4] = self.cannon3
            self.huts_xcor1 = 4
            self.huts_xcor2 = 8
            self.huts_xcor3 = 12
            self.huts_xcor4 = 16
            self.huts_xcor5 = 20
            self.huts_xcor6 = 24
            self.hut1_life = 20
            self.hut2_life = 20
            self.hut3_life = 20
            self.hut4_life = 20
            self.hut5_life = 20
            self.hut6_life = 20
            self.hut1_color = self.huts
            self.hut2_color = self.huts
            self.hut3_color = self.huts
            self.hut4_color = self.huts
            self.hut5_color = self.huts
            self.hut6_color = self.huts

            self.background = Back.BLACK + " " + Style.RESET_ALL
            self.huts = Back.GREEN + " " + Style.RESET_ALL
            self.townhall = Back.GREEN + " " + Style.RESET_ALL
            self.cannon = Back.BLUE + " " + Style.RESET_ALL
            self.cannon1 = Back.BLUE + " " + Style.RESET_ALL
            self.cannon2 = Back.BLUE + " " + Style.RESET_ALL
            self.cannon3 = Back.BLUE + " " + Style.RESET_ALL
            self.kingcolor = Back.MAGENTA + " " + Style.RESET_ALL
            self.spawning = Back.RED + " " + Style.RESET_ALL
            self.townwall = Back.WHITE + " " + Style.RESET_ALL
            
            self.wall1_col = []
            self.wall2_col = []
            self.wall3_col = []
            self.wall4_col = []

            for i in range(9):
                self.wall1_col.append(self.townwall)
                self.wall2_col.append(self.townwall)

            for i in range(10):
                self.wall3_col.append(self.townwall)
                self.wall4_col.append(self.townwall)

            self.king_xcor = 20
            self.king_ycor = 150
            self.king_life = 40
        
            if(self.win == 3): 
                self.ongoing = 0

        if self.kingh <= 0:
            self.win = 0
            self.ongoing = 0

        self.output="\n".join(["".join(row) for row in self.ground])
        print(self.output)
        repfile = "replays/replay" + self.use + ".txt"
        with open(repfile, "a+") as file:
            for i in self.output:
                for j in i:
                    file.write(j)
            file.write("\n")
            file.write("format\n")