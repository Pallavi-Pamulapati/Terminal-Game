from colorama import Back, Style
from src.input_ import get_input
from os import system
import src.Ground

class Barbarians():
    def __init__(self):
        self.gree = Back.GREEN + ' ' + Style.RESET_ALL
        self.yell = Back.YELLOW + ' ' + Style.RESET_ALL
        self.blak = Back.BLACK + ' ' + Style.RESET_ALL
        self.rd = Back.RED + ' ' + Style.RESET_ALL

        self.bar_xcords = [3,2,1]
        self.bar_ycords = [130, 100, 120]

        self.count_bar = 0
        self.activate = [-1,-1,-1]
        self.bar_damage = 2

    def inc(self,inp):
        # inp = get_input()
        if(inp == 'z'):
            self.activate[0] = 0
            self.count_bar = self.count_bar + 1
        elif(inp == 'x'):
            self.activate[1] = 0
            self.count_bar = self.count_bar + 1
        elif(inp == 'c'):
            self.activate[2] = 0
            self.count_bar = self.count_bar + 1
        
    def find_min_dist(self, ground, i):
        distances = [(ground.huts_xcor1 - self.bar_xcords[i])**2 , (ground.huts_xcor2 - self.bar_xcords[i])**2 , (ground.huts_xcor3 - self.bar_xcords[i])**2 , (ground.huts_xcor4 - self.bar_xcords[i])**2, (ground.huts_xcor5 - self.bar_xcords[i])**2, (ground.huts_xcor6 - self.bar_xcords[i])**2]
        min_hut = min(distances)
        min_hut_no = distances.index(min_hut)
        dist_townhall = (ground.townhall_xcor - self.bar_xcords[i])**2 + (ground.townhall_ycor - self.bar_ycords[i])**2
        if(min_hut + (ground.huts_ycor - self.bar_ycords[i])**2 > dist_townhall):
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
            
    def Barbarian_movement(self, ground):
        if(self.activate[0] == 0):
            min_hut_ycor = ground.huts_ycor
            min_hutxcor = self.find_min_dist(ground, 0)
            min_hut_xcor = list(min_hutxcor)
            if(min_hut_xcor[0] == 0):
                if(self.bar_ycords[0] > ground.townhall_ycor + 5):
                    self.bar_ycords[0] = self.bar_ycords[0] - 1
                elif(self.bar_ycords[0]  < ground.townhall_ycor - 5):
                    self.bar_ycords[0] = self.bar_ycords[0] + 1
                elif(self.bar_ycords[0] in range(ground.townhall_ycor - 4, ground.townhall_ycor + 5)):
                    if(self.bar_ycords[0] > ground.townhall_ycor + 2 and ground.townhall==self.gree):
                        self.bar_ycords[0] = self.bar_ycords[0] - 1
                    elif(self.bar_ycords[0] < ground.townhall_ycor and ground.townhall==self.gree):
                        self.bar_ycords[0] = self.bar_ycords[0] + 1
                    else: 
                        if(self.bar_xcords[0] > ground.townhall_xcor + 7):
                            self.bar_xcords[0] = self.bar_xcords[0] - 1
                        elif(self.bar_xcords[0] < ground.townhall_xcor - 5):
                            self.bar_xcords[0] = self.bar_xcords[0] + 1
                else:
                    if((self.bar_ycords[0] == ground.townhall_ycor - 5 or self.bar_ycords[0] == ground.townhall_ycor + 5) and not(self.bar_xcords[0] in range(ground.townhall_xcor, ground.townhall_xcor + 4)) ):
                        if(self.bar_xcords[0] < ground.townhall_xcor):
                            self.bar_xcords[0] = self.bar_xcords[0] + 1
                        elif(self.bar_xcords[0] > ground.townhall_xcor + 3):
                            self.bar_xcords[0] = self.bar_xcords[0] - 1
                
                if((self.bar_xcords[0]==ground.townhall_xcor+5 or self.bar_xcords[0]==ground.townhall_xcor+7) and (self.bar_ycords[0] in range(ground.townhall_ycor, ground.townhall_ycor + 3))):
                    if ((self.bar_ycords[0] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[0]] != self.blak):
                        ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[0]]=self.blak
                    elif((self.bar_ycords[0] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[0]] == self.blak):
                        if(self.bar_xcords[0] > ground.townhall_xcor + 4):
                            self.bar_xcords[0] = self.bar_xcords[0] - 1
                        elif(self.bar_xcords[0] == ground.townhall_xcor + 4):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_xcords[0]==ground.townhall_xcor-5 or self.bar_xcords[0]==ground.townhall_xcor-3) and (self.bar_ycords[0] in range(ground.townhall_ycor, ground.townhall_ycor + 3))):
                    if ((self.bar_ycords[0] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[0]] != self.blak):
                        ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[0]]=self.blak
                    elif((self.bar_ycords[0] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[0]] == self.blak):
                        if(self.bar_xcords[0] < ground.townhall_xcor - 1):
                            self.bar_xcords[0] = self.bar_xcords[0] + 1
                        elif(self.bar_xcords[0] == ground.townhall_xcor - 1):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_ycords[0]==ground.townhall_ycor-5 or self.bar_ycords[0]==ground.townhall_ycor-3) and (self.bar_xcords[0] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                    if ((self.bar_xcords[0] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[0]] != self.blak):
                        ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[0]]=self.blak
                    elif((self.bar_xcords[0] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[0]] == self.blak):
                        if(self.bar_ycords[0] < ground.townhall_ycor - 1):
                            self.bar_ycords[0] = self.bar_ycords[0] + 1
                        elif(self.bar_ycords[0] == ground.townhall_ycor - 1):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_ycords[0]==ground.townhall_ycor+3 or self.bar_ycords[0]==ground.townhall_ycor+5) and (self.bar_xcords[0] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                    if ((self.bar_xcords[0] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ( ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[0]] != self.blak)):
                        ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[0]]=self.blak
                    elif((self.bar_xcords[0] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ( ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[0]] == self.blak)):
                        if(self.bar_ycords[0] > ground.townhall_ycor + 3):
                            self.bar_ycords[0] = self.bar_ycords[0] - 1
                        elif(self.bar_ycords[0] == ground.townhall_ycor + 3):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

            else: 
                if(min_hut_xcor[0] > self.bar_xcords[0] + 1):
                    self.bar_xcords[0] = self.bar_xcords[0] + 1
                elif(min_hut_xcor[0] < self.bar_xcords[0] - 1):
                    self.bar_xcords[0] = self.bar_xcords[0] - 1
                else:
                    if(min_hut_ycor > self.bar_ycords[0]):
                        self.bar_ycords[0] = self.bar_ycords[0] + 1
                    elif(min_hut_ycor < self.bar_ycords[0]):
                        self.bar_ycords[0] = self.bar_ycords[0] - 1
                    else:
                        self.changeColor(ground,min_hut_xcor[1])
        if(self.activate[1] == 0):
            min_hut_ycor = ground.huts_ycor
            min_hutxcor = self.find_min_dist(ground, 0)
            min_hut_xcor = list(min_hutxcor)
            if(min_hut_xcor[0] == 0):
                if(self.bar_ycords[1] > ground.townhall_ycor + 5):
                    self.bar_ycords[1] = self.bar_ycords[1] - 1
                elif(self.bar_ycords[1]  < ground.townhall_ycor - 5):
                    self.bar_ycords[1] = self.bar_ycords[1] + 1
                elif(self.bar_ycords[1] in range(ground.townhall_ycor - 4, ground.townhall_ycor + 5)):
                    if(self.bar_ycords[1] > ground.townhall_ycor + 2 and ground.townhall==self.gree):
                        self.bar_ycords[1] = self.bar_ycords[1] - 1
                    elif(self.bar_ycords[1] < ground.townhall_ycor and ground.townhall==self.gree):
                        self.bar_ycords[1] = self.bar_ycords[1] + 1
                    else: 
                        if(self.bar_xcords[1] > ground.townhall_xcor + 7):
                            self.bar_xcords[1] = self.bar_xcords[1] - 1
                        elif(self.bar_xcords[1] < ground.townhall_xcor - 5):
                            self.bar_xcords[1] = self.bar_xcords[1] + 1
                else:
                    if((self.bar_ycords[1] == ground.townhall_ycor - 5 or self.bar_ycords[1] == ground.townhall_ycor + 5) and not(self.bar_xcords[1] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                        if(self.bar_xcords[1] < ground.townhall_xcor):
                            self.bar_xcords[1] = self.bar_xcords[1] + 1
                        elif(self.bar_xcords[1] > ground.townhall_xcor + 3):
                            self.bar_xcords[1] = self.bar_xcords[1] - 1
                
                if((self.bar_xcords[1]==ground.townhall_xcor+5 or self.bar_xcords[1]==ground.townhall_xcor+7) and (self.bar_ycords[1] in range(ground.townhall_ycor, ground.townhall_ycor + 3))):
                    if ((self.bar_ycords[1] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[1]] != self.blak):
                        ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[1]]=self.blak
                    elif((self.bar_ycords[1] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[1]] == self.blak):
                        if(self.bar_xcords[1] > ground.townhall_xcor + 4):
                            self.bar_xcords[1] = self.bar_xcords[1] - 1
                        elif(self.bar_xcords[1] == ground.townhall_xcor + 4):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_xcords[1]==ground.townhall_xcor-5 or self.bar_xcords[1]==ground.townhall_xcor-3) and (self.bar_ycords[1] in range(ground.townhall_ycor, ground.townhall_ycor + 3))):
                    if ((self.bar_ycords[1] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[1]] != self.blak):
                        ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[1]]=self.blak
                    elif((self.bar_ycords[1] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[1]] == self.blak):
                        if(self.bar_xcords[1] < ground.townhall_xcor - 1):
                            self.bar_xcords[1] = self.bar_xcords[1] + 1
                        elif(self.bar_xcords[1] == ground.townhall_xcor - 1):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_ycords[1]==ground.townhall_ycor-5 or self.bar_ycords[1]==ground.townhall_ycor-3) and (self.bar_xcords[1] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                    if ((self.bar_xcords[1] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[1]] != self.blak):
                        ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[1]]=self.blak
                    elif((self.bar_xcords[1] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[1]] == self.blak):
                        if(self.bar_ycords[1] < ground.townhall_ycor - 1):
                            self.bar_ycords[1] = self.bar_ycords[1] + 1
                        elif(self.bar_ycords[1] == ground.townhall_ycor - 1):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_ycords[1]==ground.townhall_ycor+3 or self.bar_ycords[1]==ground.townhall_ycor+5) and (self.bar_xcords[1] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                    if ((self.bar_xcords[1] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ( ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[1]] != self.blak)):
                        ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[1]]=self.blak
                    elif((self.bar_xcords[1] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ( ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[1]] == self.blak)):
                        if(self.bar_ycords[1] > ground.townhall_ycor + 3):
                            self.bar_ycords[1] = self.bar_ycords[1] - 1
                        elif(self.bar_ycords[1] == ground.townhall_ycor + 3):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

            else: 
                if(min_hut_xcor[0] > self.bar_xcords[1] + 1):
                    self.bar_xcords[1] = self.bar_xcords[1] + 1
                elif(min_hut_xcor[0] < self.bar_xcords[1] - 1):
                    self.bar_xcords[1] = self.bar_xcords[1] - 1
                else:
                    if(min_hut_ycor > self.bar_ycords[1]):
                        self.bar_ycords[1] = self.bar_ycords[1] + 1
                    elif(min_hut_ycor < self.bar_ycords[1]):
                        self.bar_ycords[1] = self.bar_ycords[1] - 1
                    else:
                        self.changeColor(ground,min_hut_xcor[1])
        
        if(self.activate[2] == 0):
            min_hut_ycor = ground.huts_ycor
            min_hutxcor = self.find_min_dist(ground, 0)
            min_hut_xcor = list(min_hutxcor)
            if(min_hut_xcor[0] == 0):
                if(self.bar_ycords[2] > ground.townhall_ycor + 5):
                    self.bar_ycords[2] = self.bar_ycords[2] - 1
                elif(self.bar_ycords[2]  < ground.townhall_ycor - 5):
                    self.bar_ycords[2] = self.bar_ycords[2] + 1
                elif(self.bar_ycords[2] in range(ground.townhall_ycor - 4, ground.townhall_ycor + 5)):
                    if(self.bar_ycords[2] > ground.townhall_ycor + 2 and ground.townhall==self.gree):
                        self.bar_ycords[2] = self.bar_ycords[2] - 1
                    elif(self.bar_ycords[2] < ground.townhall_ycor and ground.townhall==self.gree):
                        self.bar_ycords[2] = self.bar_ycords[2] + 1
                    else: 
                        if(self.bar_xcords[2] > ground.townhall_xcor + 7):
                            self.bar_xcords[2] = self.bar_xcords[2] - 1
                        elif(self.bar_xcords[2] < ground.townhall_xcor - 5):
                            self.bar_xcords[2] = self.bar_xcords[2] + 1
                else:
                    if((self.bar_ycords[2] == ground.townhall_ycor - 5 or self.bar_ycords[2] == ground.townhall_ycor + 5) and not(self.bar_xcords[2] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                        if(self.bar_xcords[2] < ground.townhall_xcor):
                            self.bar_xcords[2] = self.bar_xcords[2] + 1
                        elif(self.bar_xcords[2] > ground.townhall_xcor + 3):
                            self.bar_xcords[2] = self.bar_xcords[2] - 1
                
                if((self.bar_xcords[2]==ground.townhall_xcor+5 or self.bar_xcords[2]==ground.townhall_xcor+7) and (self.bar_ycords[2] in range(ground.townhall_ycor, ground.townhall_ycor + 3))):
                    if ((self.bar_ycords[2] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[2]] != self.blak):
                        ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[2]]=self.blak
                    elif((self.bar_ycords[2] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall1_col[-ground.townhall_ycor+4+self.bar_ycords[2]] == self.blak):
                        if(self.bar_xcords[2] > ground.townhall_xcor + 4):
                            self.bar_xcords[2] = self.bar_xcords[2] - 1
                        elif(self.bar_xcords[2] == ground.townhall_xcor + 4):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_xcords[2]==ground.townhall_xcor-5 or self.bar_xcords[2]==ground.townhall_xcor-3) and (self.bar_ycords[2] in range(ground.townhall_ycor, ground.townhall_ycor + 3))):
                    if ((self.bar_ycords[2] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[2]] != self.blak):
                        ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[2]]=self.blak
                    elif((self.bar_ycords[2] in range(ground.townhall_ycor-4,ground.townhall_ycor+5)) and ground.wall2_col[-ground.townhall_ycor+4+self.bar_ycords[2]] == self.blak):
                        if(self.bar_xcords[2] < ground.townhall_xcor - 1):
                            self.bar_xcords[2] = self.bar_xcords[2] + 1
                        elif(self.bar_xcords[2] == ground.townhall_xcor - 1):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_ycords[2]==ground.townhall_ycor-5 or self.bar_ycords[2]==ground.townhall_ycor-3) and (self.bar_xcords[2] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                    if ((self.bar_xcords[2] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[2]] != self.blak):
                        ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[2]]=self.blak
                    elif((self.bar_xcords[2] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ground.wall3_col[-ground.townhall_xcor+4+self.bar_xcords[2]] == self.blak):
                        if(self.bar_ycords[2] < ground.townhall_ycor - 1):
                            self.bar_ycords[2] = self.bar_ycords[2] + 1
                        elif(self.bar_ycords[2] == ground.townhall_ycor - 1):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

                if((self.bar_ycords[2]==ground.townhall_ycor+3 or self.bar_ycords[2]==ground.townhall_ycor+5) and (self.bar_xcords[2] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                    if ((self.bar_xcords[2] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ( ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[2]] != self.blak)):
                        ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[2]]=self.blak
                    elif((self.bar_xcords[2] in range(ground.townhall_xcor-4,ground.townhall_xcor+6)) and ( ground.wall4_col[-ground.townhall_xcor+4+self.bar_xcords[2]] == self.blak)):
                        if(self.bar_ycords[2] > ground.townhall_ycor + 3):
                            self.bar_ycords[2] = self.bar_ycords[2] - 1
                        elif(self.bar_ycords[2] == ground.townhall_ycor + 3):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000

            else: 
                if(min_hut_xcor[0] > self.bar_xcords[2] + 1):
                    self.bar_xcords[2] = self.bar_xcords[2] + 1
                elif(min_hut_xcor[0] < self.bar_xcords[2] - 1):
                    self.bar_xcords[2] = self.bar_xcords[2] - 1
                else:
                    if(min_hut_ycor > self.bar_ycords[2]):
                        self.bar_ycords[2] = self.bar_ycords[2] + 1
                    elif(min_hut_ycor < self.bar_ycords[2]):
                        self.bar_ycords[2] = self.bar_ycords[2] - 1
                    else:
                        self.changeColor(ground,min_hut_xcor[1])