from colorama import Back, Style
from src.input_ import get_input
from os import system
import src.Ground

class Archers():
    def __init__(self):
        self.gree = Back.GREEN + ' ' + Style.RESET_ALL
        self.yell = Back.YELLOW + ' ' + Style.RESET_ALL
        self.blak = Back.BLACK + ' ' + Style.RESET_ALL
        self.rd = Back.RED + ' ' + Style.RESET_ALL
        self.blu = Back.BLUE + ' ' + Style.RESET_ALL

        self.x_archers = [10,11,14]
        self.y_archers = [130, 140, 120]

        self.count_bar = 0
        self.activate = [-1,-1,-1]
        self.bar_damage = 1
        self.archer_range = 4

    def inc(self,inp):
        # inp = get_input()
        if(inp == 'j'):
            self.activate[0] = 0
            self.count_bar = self.count_bar + 1
        elif(inp == 'k'):
            self.activate[1] = 0
            self.count_bar = self.count_bar + 1
        elif(inp == 'l'):
            self.activate[2] = 0
            self.count_bar = self.count_bar + 1
        
    def find_min_dist(self, ground, i):
        distances = [(ground.huts_xcor1 - self.x_archers[i])**2 , (ground.huts_xcor2 - self.x_archers[i])**2 , (ground.huts_xcor3 - self.x_archers[i])**2 , (ground.huts_xcor4 - self.x_archers[i])**2, (ground.huts_xcor5 - self.x_archers[i])**2, (ground.huts_xcor6 - self.x_archers[i])**2]
        min_hut = min(distances)
        min_hut_no = distances.index(min_hut)
        dist_townhall = (ground.townhall_xcor - self.x_archers[i])**2 + (ground.townhall_ycor - self.y_archers[i])**2
        if(min_hut + (ground.huts_ycor - self.y_archers[i])**2 > dist_townhall):
            return 0, 0
        else: 
            if(min_hut_no == 0):
                return ground.huts_xcor1, 1
            elif(min_hut_no == 1):
                return ground.huts_xcor2, 2
            elif(min_hut_no == 2):
                return ground.huts_xcor3, 3 
            elif(min_hut_no == 3):
                return ground.huts_xcor4, 4
            elif(min_hut_no == 4):
                return ground.huts_xcor5, 5
            elif(min_hut_no == 5):
                return ground.huts_xcor6, 6

    def changeColor(self, ground, i):
        if(i == 0):
            # change wall colors
            h = 0
        elif(i == 1): 
            ground.hut1_life = ground.hut1_life - self.bar_damage
            if(ground.hut1_life >= 10 and ground.hut1_life <= 20):
                ground.hut1_color = self.gree
            elif(ground.hut1_life >= 4 and ground.hut1_life <= 10):
                ground.hut1_color = self.yell
            elif(ground.hut1_life >= 0 and ground.hut1_life <= 4):
                ground.hut1_color = self.rd
            else: 
                ground.hut1_color = self.blak
                ground.huts_xcor1 = -1000

        elif(i == 2):
            ground.hut2_life = ground.hut2_life - self.bar_damage
            if(ground.hut2_life >= 10 and ground.hut2_life <= 20):
                ground.hut2_color = self.gree
            elif(ground.hut2_life >= 4 and ground.hut2_life <= 10):
                ground.hut2_color = self.yell
            elif(ground.hut2_life >= 0 and ground.hut2_life <= 4):
                ground.hut2_color = self.rd
            else: 
                ground.hut2_color = self.blak
                ground.huts_xcor2 = -1000
        elif(i == 3):
            ground.hut3_life = ground.hut3_life - self.bar_damage
            if(ground.hut3_life >= 10 and ground.hut3_life <= 20):
                ground.hut3_color = self.gree
            elif(ground.hut3_life >= 4 and ground.hut3_life <= 10):
                ground.hut3_color = self.yell
            elif(ground.hut3_life >= 0 and ground.hut3_life <= 4):
                ground.hut3_color = self.rd
            else: 
                ground.hut3_color = self.blak
                ground.huts_xcor3 = -1000
        elif(i == 4):
            ground.hut4_life = ground.hut4_life - self.bar_damage
            if(ground.hut4_life >= 10 and ground.hut4_life <= 20):
                ground.hut4_color = self.gree
            elif(ground.hut4_life >= 4 and ground.hut4_life <= 10):
                ground.hut4_color = self.yell
            elif(ground.hut4_life >= 0 and ground.hut4_life <= 4):
                ground.hut4_color = self.rd
            else: 
                ground.hut4_color = self.blak
                ground.huts_xcor4 = -1000
        elif(i == 5):
            ground.hut5_life = ground.hut5_life - self.bar_damage
            if(ground.hut5_life >= 10 and ground.hut5_life <= 20):
                ground.hut5_color = self.gree
            elif(ground.hut5_life >= 4 and ground.hut5_life <= 10):
                ground.hut5_color = self.yell
            elif(ground.hut5_life >= 0 and ground.hut5_life <= 4):
                ground.hut5_color = self.rd
            else: 
                ground.hut5_color = self.blak
                ground.huts_xcor5 = -1000
        elif(i == 6):
            ground.hut6_life = ground.hut6_life - self.bar_damage
            if(ground.hut6_life >= 10 and ground.hut6_life <= 20):
                ground.hut6_color = self.gree
            elif(ground.hut6_life >= 4 and ground.hut6_life <= 10):
                ground.hut6_color = self.yell
            elif(ground.hut6_life >= 0 and ground.hut6_life <= 4):
                ground.hut6_color = self.rd
            else: 
                ground.hut6_color = self.blak
                ground.huts_xcor6 = -1000
            
    def Archer_movement(self, ground):
        if(self.activate[0] == 0):
            min_hutxcor = self.find_min_dist(ground, 0)
            min_hut_ycor = ground.huts_ycor
            min_hut_xcor = list(min_hutxcor)
            if(min_hut_xcor[0] == 0):
                if(self.y_archers[0] > ground.townhall_ycor + 5 and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor + 2))**2)):
                    self.y_archers[0] = self.y_archers[0] - 1
                elif(self.y_archers[0]  < ground.townhall_ycor - 5 and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor))**2)):
                    self.y_archers[0] = self.y_archers[0] + 1
                elif(self.y_archers[0] in range(ground.townhall_ycor - 4, ground.townhall_ycor + 5)):
                    if((self.y_archers[0] > ground.townhall_ycor + 2 and ground.townhall==self.gree) and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor + 2))**2)):
                        self.y_archers[0] = self.y_archers[0] - 1
                    elif(self.y_archers[0] < ground.townhall_ycor and ground.townhall==self.gree and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor))**2)):
                        self.y_archers[0] = self.y_archers[0] + 1
                    else: 
                        if(self.x_archers[0] > ground.townhall_xcor + 7 and not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[0] = self.x_archers[0] - 1
                        elif(self.x_archers[0] < ground.townhall_xcor - 5 and not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor))**2)):
                            self.x_archers[0] = self.x_archers[0] + 1
                else:
                    if(((self.y_archers[0] == ground.townhall_ycor - 5 and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor))**2)) or (self.y_archers[0] == ground.townhall_ycor + 5) and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor + 2))**2)) and not(self.x_archers[0] in range(ground.townhall_xcor, ground.townhall_xcor + 4)) ):
                        if(self.x_archers[0] < ground.townhall_xcor and not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor))**2)):
                            self.x_archers[0] = self.x_archers[0] + 1
                        elif(self.x_archers[0] > ground.townhall_xcor + 3 and not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[0] = self.x_archers[0] - 1
                
                if(((self.x_archers[0]==ground.townhall_xcor+5 or self.x_archers[0]==ground.townhall_xcor+7))):
                    if((self.y_archers[0] in range(ground.townhall_ycor,ground.townhall_ycor+3)) and ground.wall1_col[-ground.townhall_ycor+4+self.y_archers[0]] != self.blak):
                        if(not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor + 3))**2)):
                            ground.wall1_col[-ground.townhall_ycor+4+self.y_archers[0]]=self.blak
                    if((self.y_archers[0] in range(ground.townhall_ycor-4,ground.townhall_ycor+5))):
                        if(self.x_archers[0] > ground.townhall_xcor + 4 and not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[0] = self.x_archers[0] - 1
                        elif(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor + 3))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.x_archers[0]==ground.townhall_xcor-5 or self.x_archers[0]==ground.townhall_xcor-3)):
                    # ground.kingcolor = self.yell
                    if((self.y_archers[0] in range(ground.townhall_ycor,ground.townhall_ycor+3)) and ground.wall2_col[-ground.townhall_ycor+4+self.y_archers[0]] != self.blak):
                        if(not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor))**2)):
                            ground.wall2_col[-ground.townhall_ycor+4+self.y_archers[0]]=self.blak
                            # ground.kingcolor = self.rd
                    if((self.y_archers[0] in range(ground.townhall_ycor-4,ground.townhall_ycor+5))):
                        # ground.kingcolor = self.rd
                        if(self.x_archers[0] < ground.townhall_xcor - 1 and not(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor))**2)):
                            self.x_archers[0] = self.x_archers[0] + 1
                        elif(min((ground.townhall_ycor - self.y_archers[0])**2, (ground.townhall_ycor + 1 - self.y_archers[0])**2, (ground.townhall_ycor + 2 - self.y_archers[0])**2) <= self.archer_range**2 - (self.x_archers[0] - (ground.townhall_xcor))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.y_archers[0]==ground.townhall_ycor-5 or self.y_archers[0]==ground.townhall_ycor-3)):
                    if ((self.x_archers[0] in range(ground.townhall_xcor,ground.townhall_xcor+4)) and ground.wall3_col[-ground.townhall_xcor+4+self.x_archers[0]] != self.blak):
                        if(not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor))**2)):
                            ground.wall3_col[-ground.townhall_xcor+4+self.x_archers[0]]=self.blak
                    if((self.x_archers[0] in range(ground.townhall_xcor-4,ground.townhall_xcor+6))):
                        if(self.y_archers[0] < ground.townhall_ycor - 1 and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor))**2)):
                            self.y_archers[0] = self.y_archers[0] + 1
                        elif(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.y_archers[0]==ground.townhall_ycor+3 or self.y_archers[0]==ground.townhall_ycor+5 or self.y_archers[0]==ground.townhall_ycor+6)):
                    if((self.x_archers[0] in range(ground.townhall_xcor,ground.townhall_xcor+4)) and (ground.wall4_col[-ground.townhall_xcor+4+self.x_archers[0]] != self.blak)):
                        if(not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor + 2))**2)):
                            ground.wall4_col[-ground.townhall_xcor+4+self.x_archers[0]]=self.blak
                    if((self.x_archers[0] in range(ground.townhall_xcor-4,ground.townhall_xcor+6))):
                        if(self.y_archers[0] > ground.townhall_ycor + 3 and not(min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor + 2))**2)):
                            self.y_archers[0] = self.y_archers[0] - 1
                        elif((min((ground.townhall_xcor - self.x_archers[0])**2, (ground.townhall_xcor + 1 - self.x_archers[0])**2, (ground.townhall_xcor + 2 - self.x_archers[0])**2, (ground.townhall_xcor + 3 - self.x_archers[0])**2) <= self.archer_range**2 - (self.y_archers[0] - (ground.townhall_ycor + 2))**2)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

            else: 
                if(min_hut_xcor[0] > self.x_archers[0] + 1 and ((min_hut_xcor[0] - self.x_archers[0])**2 + (min_hut_ycor - self.y_archers[0])**2) > self.archer_range**2):
                    self.x_archers[0] = self.x_archers[0] + 1
                elif(min_hut_xcor[0] < self.x_archers[0] - 1 and ((min_hut_xcor[0] - self.x_archers[0])**2 + (min_hut_ycor - self.y_archers[0])**2) > self.archer_range**2):
                    self.x_archers[0] = self.x_archers[0] - 1
                else:
                    if(min_hut_ycor > self.y_archers[0] and ((min_hut_xcor[0] - self.x_archers[0])**2 + (min_hut_ycor - self.y_archers[0])**2) > self.archer_range**2):
                        self.y_archers[0] = self.y_archers[0] + 1
                    elif(min_hut_ycor < self.y_archers[0] and ((min_hut_xcor[0] - self.x_archers[0])**2 + (min_hut_ycor - self.y_archers[0])**2) > self.archer_range**2):
                        self.y_archers[0] = self.y_archers[0] - 1
                    else:
                        self.changeColor(ground,min_hut_xcor[1])
        if(self.activate[1] == 0):
            min_hutxcor = self.find_min_dist(ground, 1)
            min_hut_ycor = ground.huts_ycor
            min_hut_xcor = list(min_hutxcor)
            if(min_hut_xcor[0] == 0):
                if(self.y_archers[1] > ground.townhall_ycor + 5 and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor + 2))**2)):
                    self.y_archers[1] = self.y_archers[1] - 1
                elif(self.y_archers[1]  < ground.townhall_ycor - 5 and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor))**2)):
                    self.y_archers[1] = self.y_archers[1] + 1
                elif(self.y_archers[1] in range(ground.townhall_ycor - 4, ground.townhall_ycor + 5)):
                    if((self.y_archers[1] > ground.townhall_ycor + 2 and ground.townhall==self.gree) and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor + 2))**2)):
                        self.y_archers[1] = self.y_archers[1] - 1
                    elif(self.y_archers[1] < ground.townhall_ycor and ground.townhall==self.gree and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor))**2)):
                        self.y_archers[1] = self.y_archers[1] + 1
                    else: 
                        if(self.x_archers[1] > ground.townhall_xcor + 7 and not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[1] = self.x_archers[1] - 1
                        elif(self.x_archers[1] < ground.townhall_xcor - 5 and not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor))**2)):
                            self.x_archers[1] = self.x_archers[1] + 1
                else:
                    if(((self.y_archers[1] == ground.townhall_ycor - 5 and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor))**2)) or (self.y_archers[1] == ground.townhall_ycor + 5) and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor + 2))**2)) and not(self.x_archers[1] in range(ground.townhall_xcor, ground.townhall_xcor + 4)) ):
                        if(self.x_archers[1] < ground.townhall_xcor and not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor))**2)):
                            self.x_archers[1] = self.x_archers[1] + 1
                        elif(self.x_archers[1] > ground.townhall_xcor + 3 and not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[1] = self.x_archers[1] - 1
                
                if(((self.x_archers[1]==ground.townhall_xcor+5 or self.x_archers[1]==ground.townhall_xcor+7))):
                    if((self.y_archers[1] in range(ground.townhall_ycor,ground.townhall_ycor+3)) and ground.wall1_col[-ground.townhall_ycor+4+self.y_archers[1]] != self.blak):
                        if(not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor + 3))**2)):
                            ground.wall1_col[-ground.townhall_ycor+4+self.y_archers[1]]=self.blak
                    if((self.y_archers[1] in range(ground.townhall_ycor-4,ground.townhall_ycor+5))):
                        if(self.x_archers[1] > ground.townhall_xcor + 4 and not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[1] = self.x_archers[1] - 1
                        elif(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor + 3))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.x_archers[1]==ground.townhall_xcor-5 or self.x_archers[1]==ground.townhall_xcor-3)):
                    # ground.kingcolor = self.yell
                    if((self.y_archers[1] in range(ground.townhall_ycor,ground.townhall_ycor+3)) and ground.wall2_col[-ground.townhall_ycor+4+self.y_archers[1]] != self.blak):
                        if(not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor))**2)):
                            ground.wall2_col[-ground.townhall_ycor+4+self.y_archers[1]]=self.blak
                            # ground.kingcolor = self.rd
                    if((self.y_archers[1] in range(ground.townhall_ycor-4,ground.townhall_ycor+5))):
                        # ground.kingcolor = self.rd
                        if(self.x_archers[1] < ground.townhall_xcor - 1 and not(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor))**2)):
                            self.x_archers[1] = self.x_archers[1] + 1
                        elif(min((ground.townhall_ycor - self.y_archers[1])**2, (ground.townhall_ycor + 1 - self.y_archers[1])**2, (ground.townhall_ycor + 2 - self.y_archers[1])**2) <= self.archer_range**2 - (self.x_archers[1] - (ground.townhall_xcor))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.y_archers[1]==ground.townhall_ycor-5 or self.y_archers[1]==ground.townhall_ycor-3)):
                    if ((self.x_archers[1] in range(ground.townhall_xcor,ground.townhall_xcor+4)) and ground.wall3_col[-ground.townhall_xcor+4+self.x_archers[1]] != self.blak):
                        if(not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor))**2)):
                            ground.wall3_col[-ground.townhall_xcor+4+self.x_archers[1]]=self.blak
                    if((self.x_archers[1] in range(ground.townhall_xcor-4,ground.townhall_xcor+6))):
                        if(self.y_archers[1] < ground.townhall_ycor - 1 and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor))**2)):
                            self.y_archers[1] = self.y_archers[1] + 1
                        elif(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.y_archers[1]==ground.townhall_ycor+3 or self.y_archers[1]==ground.townhall_ycor+5 or self.y_archers[1]==ground.townhall_ycor+6)):
                    if((self.x_archers[1] in range(ground.townhall_xcor,ground.townhall_xcor+4)) and (ground.wall4_col[-ground.townhall_xcor+4+self.x_archers[1]] != self.blak)):
                        if(not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor + 2))**2)):
                            ground.wall4_col[-ground.townhall_xcor+4+self.x_archers[1]]=self.blak
                    if((self.x_archers[1] in range(ground.townhall_xcor-4,ground.townhall_xcor+6))):
                        if(self.y_archers[1] > ground.townhall_ycor + 3 and not(min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor + 2))**2)):
                            self.y_archers[1] = self.y_archers[1] - 1
                        elif((min((ground.townhall_xcor - self.x_archers[1])**2, (ground.townhall_xcor + 1 - self.x_archers[1])**2, (ground.townhall_xcor + 2 - self.x_archers[1])**2, (ground.townhall_xcor + 3 - self.x_archers[1])**2) <= self.archer_range**2 - (self.y_archers[1] - (ground.townhall_ycor + 2))**2)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

            else: 
                if(min_hut_xcor[0] > self.x_archers[1] + 1 and ((min_hut_xcor[0] - self.x_archers[1])**2 + (min_hut_ycor - self.y_archers[1])**2) > self.archer_range**2):
                    self.x_archers[1] = self.x_archers[1] + 1
                elif(min_hut_xcor[0] < self.x_archers[1] - 1 and ((min_hut_xcor[0] - self.x_archers[1])**2 + (min_hut_ycor - self.y_archers[1])**2) > self.archer_range**2):
                    self.x_archers[1] = self.x_archers[1] - 1
                else:
                    if(min_hut_ycor > self.y_archers[1] and ((min_hut_xcor[0] - self.x_archers[1])**2 + (min_hut_ycor - self.y_archers[1])**2) > self.archer_range**2):
                        self.y_archers[1] = self.y_archers[1] + 1
                    elif(min_hut_ycor < self.y_archers[1] and ((min_hut_xcor[0] - self.x_archers[1])**2 + (min_hut_ycor - self.y_archers[1])**2) > self.archer_range**2):
                        self.y_archers[1] = self.y_archers[1] - 1
                    else:
                        self.changeColor(ground,min_hut_xcor[1])

        if(self.activate[2] == 0):
            min_hutxcor = self.find_min_dist(ground, 2)
            min_hut_ycor = ground.huts_ycor
            min_hut_xcor = list(min_hutxcor)
            if(min_hut_xcor[0] == 0):
                if(self.y_archers[2] > ground.townhall_ycor + 5 and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor + 2))**2)):
                    self.y_archers[2] = self.y_archers[2] - 1
                elif(self.y_archers[2]  < ground.townhall_ycor - 5 and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor))**2)):
                    self.y_archers[2] = self.y_archers[2] + 1
                elif(self.y_archers[2] in range(ground.townhall_ycor - 4, ground.townhall_ycor + 5)):
                    if((self.y_archers[2] > ground.townhall_ycor + 2 and ground.townhall==self.gree) and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor + 2))**2)):
                        self.y_archers[2] = self.y_archers[2] - 1
                    elif(self.y_archers[2] < ground.townhall_ycor and ground.townhall==self.gree and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor))**2)):
                        self.y_archers[2] = self.y_archers[2] + 1
                    else: 
                        if(self.x_archers[2] > ground.townhall_xcor + 7 and not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[2] = self.x_archers[2] - 1
                        elif(self.x_archers[2] < ground.townhall_xcor - 5 and not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor))**2)):
                            self.x_archers[2] = self.x_archers[2] + 1
                else:
                    if(((self.y_archers[2] == ground.townhall_ycor - 5 and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor))**2)) or (self.y_archers[2] == ground.townhall_ycor + 5) and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor + 2))**2)) and not(self.x_archers[2] in range(ground.townhall_xcor, ground.townhall_xcor + 4)) ):
                        if(self.x_archers[2] < ground.townhall_xcor and not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor))**2)):
                            self.x_archers[2] = self.x_archers[2] + 1
                        elif(self.x_archers[2] > ground.townhall_xcor + 3 and not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[2] = self.x_archers[2] - 1
                
                if(((self.x_archers[2]==ground.townhall_xcor+5 or self.x_archers[2]==ground.townhall_xcor+7))):
                    if((self.y_archers[2] in range(ground.townhall_ycor,ground.townhall_ycor+3)) and ground.wall1_col[-ground.townhall_ycor+4+self.y_archers[2]] != self.blak):
                        if(not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor + 3))**2)):
                            ground.wall1_col[-ground.townhall_ycor+4+self.y_archers[2]]=self.blak
                    if((self.y_archers[2] in range(ground.townhall_ycor-4,ground.townhall_ycor+5))):
                        if(self.x_archers[2] > ground.townhall_xcor + 4 and not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor + 3))**2)):
                            self.x_archers[2] = self.x_archers[2] - 1
                        elif(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor + 3))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.x_archers[2]==ground.townhall_xcor-5 or self.x_archers[2]==ground.townhall_xcor-3)):
                    # ground.kingcolor = self.yell
                    if((self.y_archers[2] in range(ground.townhall_ycor,ground.townhall_ycor+3)) and ground.wall2_col[-ground.townhall_ycor+4+self.y_archers[2]] != self.blak):
                        if(not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor))**2)):
                            ground.wall2_col[-ground.townhall_ycor+4+self.y_archers[2]]=self.blak
                            # ground.kingcolor = self.rd
                    if((self.y_archers[2] in range(ground.townhall_ycor-4,ground.townhall_ycor+5))):
                        # ground.kingcolor = self.rd
                        if(self.x_archers[2] < ground.townhall_xcor - 1 and not(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor))**2)):
                            self.x_archers[2] = self.x_archers[2] + 1
                        elif(min((ground.townhall_ycor - self.y_archers[2])**2, (ground.townhall_ycor + 1 - self.y_archers[2])**2, (ground.townhall_ycor + 2 - self.y_archers[2])**2) <= self.archer_range**2 - (self.x_archers[2] - (ground.townhall_xcor))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.y_archers[2]==ground.townhall_ycor-5 or self.y_archers[2]==ground.townhall_ycor-3)):
                    if ((self.x_archers[2] in range(ground.townhall_xcor,ground.townhall_xcor+4)) and ground.wall3_col[-ground.townhall_xcor+4+self.x_archers[2]] != self.blak):
                        if(not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor))**2)):
                            ground.wall3_col[-ground.townhall_xcor+4+self.x_archers[2]]=self.blak
                    if((self.x_archers[2] in range(ground.townhall_xcor-4,ground.townhall_xcor+6))):
                        if(self.y_archers[2] < ground.townhall_ycor - 1 and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor))**2)):
                            self.y_archers[2] = self.y_archers[2] + 1
                        elif(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor))**2):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.y_archers[2]==ground.townhall_ycor+3 or self.y_archers[2]==ground.townhall_ycor+5 or self.y_archers[2]==ground.townhall_ycor+6)):
                    if((self.x_archers[2] in range(ground.townhall_xcor,ground.townhall_xcor+4)) and (ground.wall4_col[-ground.townhall_xcor+4+self.x_archers[2]] != self.blak)):
                        if(not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor + 2))**2)):
                            ground.wall4_col[-ground.townhall_xcor+4+self.x_archers[2]]=self.blak
                    if((self.x_archers[2] in range(ground.townhall_xcor-4,ground.townhall_xcor+6))):
                        if(self.y_archers[2] > ground.townhall_ycor + 3 and not(min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor + 2))**2)):
                            self.y_archers[2] = self.y_archers[2] - 1
                        elif((min((ground.townhall_xcor - self.x_archers[2])**2, (ground.townhall_xcor + 1 - self.x_archers[2])**2, (ground.townhall_xcor + 2 - self.x_archers[2])**2, (ground.townhall_xcor + 3 - self.x_archers[2])**2) <= self.archer_range**2 - (self.y_archers[2] - (ground.townhall_ycor + 2))**2)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

            else: 
                if(min_hut_xcor[0] > self.x_archers[2] + 1 and ((min_hut_xcor[0] - self.x_archers[2])**2 + (min_hut_ycor - self.y_archers[2])**2) > self.archer_range**2):
                    self.x_archers[2] = self.x_archers[2] + 1
                elif(min_hut_xcor[0] < self.x_archers[2] - 1 and ((min_hut_xcor[0] - self.x_archers[2])**2 + (min_hut_ycor - self.y_archers[2])**2) > self.archer_range**2):
                    self.x_archers[2] = self.x_archers[2] - 1
                else:
                    if(min_hut_ycor > self.y_archers[2] and ((min_hut_xcor[0] - self.x_archers[2])**2 + (min_hut_ycor - self.y_archers[2])**2) > self.archer_range**2):
                        self.y_archers[2] = self.y_archers[2] + 1
                    elif(min_hut_ycor < self.y_archers[2] and ((min_hut_xcor[0] - self.x_archers[2])**2 + (min_hut_ycor - self.y_archers[2])**2) > self.archer_range**2):
                        self.y_archers[2] = self.y_archers[2] - 1
                    else:
                        self.changeColor(ground,min_hut_xcor[1])