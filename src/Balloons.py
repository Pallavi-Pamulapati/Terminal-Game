from colorama import Back, Style
from src.input_ import get_input
from os import system
import src.Ground

class Balloon():
    def __init__(self):
        self.gree = Back.GREEN + ' ' + Style.RESET_ALL
        self.yell = Back.YELLOW + ' ' + Style.RESET_ALL
        self.blak = Back.BLACK + ' ' + Style.RESET_ALL
        self.rd = Back.RED + ' ' + Style.RESET_ALL
        self.blu = Back.BLUE + ' ' + Style.RESET_ALL

        self.x_balloon = [4,5,6]
        self.y_balloon = [130, 100, 120]

        self.count_bar = 0
        self.activate = [-1,-1,-1]
        self.bar_damage = 4

        self.balloonHealth = [10, 10, 10]

    def inc(self,inp):
        if(inp == 'i'):
            if(self.activate[0] != -2):
                self.activate[0] = 0
                self.count_bar = self.count_bar + 1
        elif(inp == 'o'):
            if(self.activate[1] != -2):
                self.activate[1] = 0
                self.count_bar = self.count_bar + 1
        elif(inp == 'p'):
            if(self.activate[2] != -2):
                self.activate[2] = 0
                self.count_bar = self.count_bar + 1
        
    def find_min_dist(self, ground, i):
        distances = [(ground.huts_xcor1 - self.x_balloon[i])**2 , (ground.huts_xcor2 - self.x_balloon[i])**2 , (ground.huts_xcor3 - self.x_balloon[i])**2 , (ground.huts_xcor4 - self.x_balloon[i])**2, (ground.huts_xcor5 - self.x_balloon[i])**2, (ground.huts_xcor6 - self.x_balloon[i])**2]
        min_hut = min(distances)
        min_hut_no = distances.index(min_hut)
        dist_townhall = (ground.townhall_xcor - self.x_balloon[i])**2 + (ground.townhall_ycor - self.y_balloon[i])**2
        if(min_hut + (ground.huts_ycor - self.y_balloon[i])**2 > dist_townhall):
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

    def find_min_defense(self, ground, i):
        distances = [(ground.cx1 - self.x_balloon[i])**2 + (ground.cy1 - self.y_balloon[i])**2, (ground.cx2 - self.x_balloon[i])**2 + (ground.cy2 - self.y_balloon[i])**2, (ground.wtx1 - self.x_balloon[i])**2 + (ground.wty1 - self.y_balloon[i])**2, (ground.wtx2 - self.x_balloon[i])**2 + (ground.wty2 - self.y_balloon[i])**2]
        if(ground.win >= 1):
            distances.append((ground.cx3 - self.x_balloon[i])**2 + (ground.cy3 - self.y_balloon[i])**2)
            distances.append((ground.wtx3 - self.x_balloon[i])**2 + (ground.wty3 - self.y_balloon[i])**2)
        if(ground.win == 2): 
            distances.append((ground.cx4 - self.x_balloon[i])**2 + (ground.cy4 - self.y_balloon[i])**2)
            distances.append((ground.wtx4 - self.x_balloon[i])**2 + (ground.wty4 - self.y_balloon[i])**2)
        min_defense = min(distances)
        min_defense_no = distances.index(min_defense)
        if(min_defense_no == 0):
            return ground.cx1,ground.cy1, "c1"
        elif(min_defense_no == 1): 
            return ground.cx2, ground.cy2, "c2"
        elif(min_defense_no == 2):
            return ground.wtx1, ground.wty1, "w1"
        elif(min_defense_no == 3):
            return ground.wtx2, ground.wty2, "w2"
        elif(min_defense_no == 4): 
            return ground.cx3, ground.cy3, "c3"
        elif(min_defense_no == 5):
            return ground.wtx3, ground.wty3, "w3"    
        elif(min_defense_no == 6):
            return ground.cx4, ground.cy4, "c4"
        elif(min_defense_no == 7): 
            return ground.wtx4, ground.wty4, "w4"  

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
    
    def changeCannonColor(self, ground, i):
        if(i == "c1"):
            ground.chealth = ground.chealth - self.bar_damage
            if(ground.chealth >= 5 and ground.chealth <= 10):
                ground.cannon = self.blu
            elif(ground.chealth >= 0 and ground.chealth <= 4):
                ground.cannon = self.rd
            else: 
                ground.cannon = self.blak
                ground.cx1 = -1000
        if(i == "c2"):
            ground.chealth1 = ground.chealth1 - self.bar_damage
            if(ground.chealth1 >= 5 and ground.chealth1 <= 10):
                ground.cannon1 = self.blu
            elif(ground.chealth1 >= 0 and ground.chealth1 <= 4):
                ground.cannon1 = self.rd
            else: 
                ground.cannon1 = self.blak
                ground.cx2 = -1000
        if(i == "c3"):
            ground.chealth2 = ground.chealth2 - self.bar_damage
            if(ground.chealth2 >= 5 and ground.chealth2 <= 10):
                ground.cannon2 = self.blu
            elif(ground.chealth2 >= 0 and ground.chealth2 <= 4):
                ground.cannon2 = self.rd
            else: 
                ground.cannon2 = self.blak
                ground.cx3 = -1000
        if(i == "c4"): 
            ground.chealth3 = ground.chealth3 - self.bar_damage
            if(ground.chealth3 >= 5 and ground.chealth3 <= 10):
                ground.cannon3 = self.blu
            elif(ground.chealth3 >= 0 and ground.chealth3 <= 4):
                ground.cannon3 = self.rd
            else: 
                ground.cannon3 = self.blak
                ground.cx4 = -1000

        if(i == "w1"): 
            ground.wt_health1 = ground.wt_health1 - self.bar_damage
            if(ground.wt_health1 >= 5 and ground.wt_health1 <= 10):
                ground.wt_color1 = self.blu
            elif(ground.wt_health1 >= 0 and ground.wt_health1 <= 4):
                ground.wt_color1 = self.rd
            else: 
                ground.wt_color1 = self.blak
                ground.wtx1 = -1000
        if(i == "w2"): 
            ground.wt_health2 = ground.wt_health2 - self.bar_damage
            if(ground.wt_health2 >= 5 and ground.wt_health2 <= 10):
                ground.wt_color2 = self.blu
            elif(ground.wt_health2 >= 0 and ground.wt_health2 <= 4):
                ground.wt_color2 = self.rd
            else: 
                ground.wt_color2 = self.blak
                ground.wtx2 = -1000
        if(i == "w3"): 
            ground.wt_health3 = ground.wt_health3 - self.bar_damage
            if(ground.wt_health3 >= 5 and ground.wt_health3 <= 10):
                ground.wt_color3 = self.blu
            elif(ground.wt_health3 >= 0 and ground.wt_health3 <= 4):
                ground.wt_color3 = self.rd
            else: 
                ground.wt_color3 = self.blak
                ground.wtx3 = -1000
        if(i == "w4"): 
            ground.wt_health4 = ground.wt_health4 - self.bar_damage
            if(ground.wt_health4 >= 5 and ground.wt_health4 <= 10):
                ground.wt_color4 = self.blu
            elif(ground.wt_health4 >= 0 and ground.wt_health4 <= 4):
                ground.wt_color4 = self.rd
            else: 
                ground.wt_color4 = self.blak
                ground.wtx4 = -1000

    def Balloon_movement(self, ground):
        if(self.activate[0] == 0):
            if(ground.cx1 + ground.cx2 + ground.wtx1 + ground.wtx2 != -4000 or (ground.win >= 1 and ground.cx1 + ground.cx2 + ground.cx3 + ground.wtx1 + ground.wtx2 + ground.wtx3 != -6000) or(ground.win == 2 and ground.cx1 + ground.cx2 + ground.cx3 + ground.cx4 + ground.wtx1 + ground.wtx2 + ground.wtx3 + ground.wtx4 != -8000)):
                min_canon = self.find_min_defense(ground, 0)
                min_cannon = list(min_canon)
                if(min_cannon[0] > self.x_balloon[0] + 1):
                    self.x_balloon[0] = self.x_balloon[0] + 1
                elif(min_cannon[0] < self.x_balloon[0] - 1):
                    self.x_balloon[0] = self.x_balloon[0] - 1
                else:
                    if(min_cannon[1] > self.y_balloon[0]):
                        self.y_balloon[0] = self.y_balloon[0] + 1
                    elif(min_cannon[1] < self.y_balloon[0]):
                        self.y_balloon[0] = self.y_balloon[0] - 1
                    else:
                        self.changeCannonColor(ground, min_cannon[2])
            else: 
                min_hut_ycor = ground.huts_ycor
                min_hutxcor = self.find_min_dist(ground, 0)
                min_hut_xcor = list(min_hutxcor)
                if(min_hut_xcor[0] == 0):
                    if(self.y_balloon[0] > ground.townhall_ycor + 3): 
                        self.y_balloon[0] = self.y_balloon[0] - 1
                    elif(self.y_balloon[0] < ground.townhall_ycor - 1):
                        self.y_balloon[0] = self.y_balloon[0] + 1
                    else: 
                        if((self.y_balloon[0] == ground.townhall_ycor - 1 or self.y_balloon[0] == ground.townhall_ycor + 3) and not(self.x_balloon[0] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                            if(self.y_balloon[0] == ground.townhall_ycor - 1):
                                self.y_balloon[0] = self.y_balloon[0] + 1
                            elif(self.y_balloon[0] == ground.townhall_ycor + 3): 
                                self.y_balloon[0] = self.y_balloon[0] - 1

                        if(self.y_balloon[0] in range(ground.townhall_ycor, ground.townhall_ycor + 3)):
                            if(self.x_balloon[0] < ground.townhall_xcor -1):
                                self.x_balloon[0] = self.x_balloon[0] + 1
                            elif(self.x_balloon[0] > ground.townhall_xcor + 4):
                                self.x_balloon[0] = self.x_balloon[0] - 1

                        if((self.x_balloon[0] in range(ground.townhall_xcor, ground.townhall_xcor + 4)) and (self.y_balloon[0] == ground.townhall_ycor - 1 or self.y_balloon[0] == ground.townhall_ycor + 3)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000
                        elif((self.y_balloon[0] in range(ground.townhall_ycor, ground.townhall_ycor + 3)) and (self.x_balloon[0] == ground.townhall_xcor - 1 or self.x_balloon[0] == ground.townhall_xcor + 4)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000
                else: 
                    if(min_hut_xcor[0] > self.x_balloon[0] + 1):
                        self.x_balloon[0] = self.x_balloon[0] + 1
                    elif(min_hut_xcor[0] < self.x_balloon[0] - 1):
                        self.x_balloon[0] = self.x_balloon[0] - 1
                    else:
                        if(min_hut_ycor > self.y_balloon[0]):
                            self.y_balloon[0] = self.y_balloon[0] + 1
                        elif(min_hut_ycor < self.y_balloon[0]):
                            self.y_balloon[0] = self.y_balloon[0] - 1
                        else:
                            self.changeColor(ground,min_hut_xcor[1])
        if(self.activate[1] == 0):
            if(ground.cx1 + ground.cx2 + ground.wtx1 + ground.wtx2 != -4000 or (ground.win >= 1 and ground.cx1 + ground.cx2 + ground.cx3 + ground.wtx1 + ground.wtx2 + ground.wtx3 != -6000) or(ground.win == 2 and ground.cx1 + ground.cx2 + ground.cx3 + ground.cx4 + ground.wtx1 + ground.wtx2 + ground.wtx3 + ground.wtx4 != -8000)):
                min_canon = self.find_min_defense(ground, 1)
                min_cannon = list(min_canon)
                if(min_cannon[0] > self.x_balloon[1] + 1):
                    self.x_balloon[1] = self.x_balloon[1] + 1
                elif(min_cannon[0] < self.x_balloon[1] - 1):
                    self.x_balloon[1] = self.x_balloon[1] - 1
                else:
                    if(min_cannon[1] > self.y_balloon[1]):
                        self.y_balloon[1] = self.y_balloon[1] + 1
                    elif(min_cannon[1] < self.y_balloon[1]):
                        self.y_balloon[1] = self.y_balloon[1] - 1
                    else:
                        self.changeCannonColor(ground, min_cannon[2])
            else: 
                min_hut_ycor = ground.huts_ycor
                min_hutxcor = self.find_min_dist(ground, 1)
                min_hut_xcor = list(min_hutxcor)
                if(min_hut_xcor[0] == 0):
                    if(self.y_balloon[1] > ground.townhall_ycor + 3): 
                        self.y_balloon[1] = self.y_balloon[1] - 1
                    elif(self.y_balloon[1] < ground.townhall_ycor - 1):
                        self.y_balloon[1] = self.y_balloon[1] + 1
                    else: 
                        if((self.y_balloon[1] == ground.townhall_ycor - 1 or self.y_balloon[1] == ground.townhall_ycor + 3) and not(self.x_balloon[1] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                            if(self.y_balloon[1] == ground.townhall_ycor - 1):
                                self.y_balloon[1] = self.y_balloon[1] + 1
                            elif(self.y_balloon[1] == ground.townhall_ycor + 3): 
                                self.y_balloon[1] = self.y_balloon[1] - 1

                        if(self.y_balloon[1] in range(ground.townhall_ycor, ground.townhall_ycor + 3)):
                            if(self.x_balloon[1] < ground.townhall_xcor -1):
                                self.x_balloon[1] = self.x_balloon[1] + 1
                            elif(self.x_balloon[1] > ground.townhall_xcor + 4):
                                self.x_balloon[1] = self.x_balloon[1] - 1

                        if((self.x_balloon[1] in range(ground.townhall_xcor, ground.townhall_xcor + 4)) and (self.y_balloon[1] == ground.townhall_ycor - 1 or self.y_balloon[1] == ground.townhall_ycor + 3)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000
                        elif((self.y_balloon[1] in range(ground.townhall_ycor, ground.townhall_ycor + 3)) and (self.x_balloon[1] == ground.townhall_xcor - 1 or self.x_balloon[1] == ground.townhall_xcor + 4)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000
                else: 
                    if(min_hut_xcor[0] > self.x_balloon[1] + 1):
                        self.x_balloon[1] = self.x_balloon[1] + 1
                    elif(min_hut_xcor[0] < self.x_balloon[1] - 1):
                        self.x_balloon[1] = self.x_balloon[1] - 1
                    else:
                        if(min_hut_ycor > self.y_balloon[1]):
                            self.y_balloon[1] = self.y_balloon[1] + 1
                        elif(min_hut_ycor < self.y_balloon[1]):
                            self.y_balloon[1] = self.y_balloon[1] - 1
                        else:
                            self.changeColor(ground,min_hut_xcor[1])
        if(self.activate[2] == 0):
            if(ground.cx1 + ground.cx2 + ground.wtx1 + ground.wtx2 != -4000 or (ground.win >= 1 and ground.cx1 + ground.cx2 + ground.cx3 + ground.wtx1 + ground.wtx2 + ground.wtx3 != -6000) or(ground.win == 2 and ground.cx1 + ground.cx2 + ground.cx3 + ground.cx4 + ground.wtx1 + ground.wtx2 + ground.wtx3 + ground.wtx4 != -8000)):
                min_canon = self.find_min_defense(ground, 2)
                min_cannon = list(min_canon)
                if(min_cannon[0] > self.x_balloon[2] + 1):
                    self.x_balloon[2] = self.x_balloon[2] + 1
                elif(min_cannon[0] < self.x_balloon[2] - 1):
                    self.x_balloon[2] = self.x_balloon[2] - 1
                else:
                    if(min_cannon[1] > self.y_balloon[2]):
                        self.y_balloon[2] = self.y_balloon[2] + 1
                    elif(min_cannon[1] < self.y_balloon[2]):
                        self.y_balloon[2] = self.y_balloon[2] - 1
                    else:
                        self.changeCannonColor(ground, min_cannon[2])
            else: 
                min_hut_ycor = ground.huts_ycor
                min_hutxcor = self.find_min_dist(ground, 2)
                min_hut_xcor = list(min_hutxcor)
                if(min_hut_xcor[0] == 0):
                    if(self.y_balloon[2] > ground.townhall_ycor + 3): 
                        self.y_balloon[2] = self.y_balloon[2] - 1
                    elif(self.y_balloon[2] < ground.townhall_ycor - 1):
                        self.y_balloon[2] = self.y_balloon[2] + 1
                    else: 
                        if((self.y_balloon[2] == ground.townhall_ycor - 1 or self.y_balloon[2] == ground.townhall_ycor + 3) and not(self.x_balloon[2] in range(ground.townhall_xcor, ground.townhall_xcor + 4))):
                            if(self.y_balloon[2] == ground.townhall_ycor - 1):
                                self.y_balloon[2] = self.y_balloon[2] + 1
                            elif(self.y_balloon[2] == ground.townhall_ycor + 3): 
                                self.y_balloon[2] = self.y_balloon[2] - 1

                        if(self.y_balloon[2] in range(ground.townhall_ycor, ground.townhall_ycor + 3)):
                            if(self.x_balloon[2] < ground.townhall_xcor -1):
                                self.x_balloon[2] = self.x_balloon[2] + 1
                            elif(self.x_balloon[2] > ground.townhall_xcor + 4):
                                self.x_balloon[2] = self.x_balloon[2] - 1

                        if((self.x_balloon[2] in range(ground.townhall_xcor, ground.townhall_xcor + 4)) and (self.y_balloon[2] == ground.townhall_ycor - 1 or self.y_balloon[2] == ground.townhall_ycor + 3)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000
                        elif((self.y_balloon[2] in range(ground.townhall_ycor, ground.townhall_ycor + 3)) and (self.x_balloon[2] == ground.townhall_xcor - 1 or self.x_balloon[2] == ground.townhall_xcor + 4)):
                            if(ground.townhall==self.gree):
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000
                else: 
                    if(min_hut_xcor[0] > self.x_balloon[2] + 1):
                        self.x_balloon[2] = self.x_balloon[2] + 1
                    elif(min_hut_xcor[0] < self.x_balloon[2] - 1):
                        self.x_balloon[2] = self.x_balloon[2] - 1
                    else:
                        if(min_hut_ycor > self.y_balloon[2]):
                            self.y_balloon[2] = self.y_balloon[2] + 1
                        elif(min_hut_ycor < self.y_balloon[2]):
                            self.y_balloon[2] = self.y_balloon[2] - 1
                        else:
                            self.changeColor(ground,min_hut_xcor[1])