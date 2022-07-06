from colorama import Back, Style
from src.input_ import get_input
from os import system
from time import time
# from src.Ground import Village

class king():
    def __init__(self, kx, ky):
        self.king_xcor = kx
        self.king_ycor = ky
        self.gree = Back.GREEN + ' ' + Style.RESET_ALL
        self.yell = Back.YELLOW + ' ' + Style.RESET_ALL
        self.blak = Back.BLACK + ' ' + Style.RESET_ALL
        self.rd = Back.RED + ' ' + Style.RESET_ALL
        self.blu = Back.BLUE + ' ' + Style.RESET_ALL

    def modify(self, kx, ky):
        self.king_xcor = kx
        self.king_ycor = ky

    def motion(self, ground, Attacker):
        direction = get_input()
        if(direction == 'w' or direction == 'a' or direction == 's' or direction == 'd'):
            system("aplay -q ./src/strike.wav &")

        if(direction == 'w'):
            ground.prev_pos = direction
            ground.king_xcor = ground.king_xcor-1
            if(ground.king_ycor == ground.huts_ycor):
                if(ground.king_xcor == ground.huts_xcor1):
                    ground.king_xcor = ground.king_xcor + 1
                elif(ground.king_xcor == ground.huts_xcor2):
                    ground.king_xcor = ground.king_xcor + 1
                elif(ground.king_xcor == ground.huts_xcor3):
                    ground.king_xcor = ground.king_xcor + 1
                elif(ground.king_xcor == ground.huts_xcor4):
                    ground.king_xcor = ground.king_xcor + 1
                elif(ground.king_xcor == ground.huts_xcor5):
                    ground.king_xcor = ground.king_xcor + 1
                elif(ground.king_xcor == ground.huts_xcor6):
                    ground.king_xcor = ground.king_xcor + 1
        elif(direction == 'a'):
            ground.prev_pos = direction
            ground.king_ycor = ground.king_ycor - 1
            if(ground.king_ycor == ground.huts_ycor):
                if(ground.king_xcor == ground.huts_xcor1):
                    ground.king_ycor = ground.king_ycor + 1
                elif(ground.king_xcor == ground.huts_xcor2):
                    ground.king_ycor = ground.king_ycor + 1
                elif(ground.king_xcor == ground.huts_xcor3):
                    ground.king_ycor = ground.king_ycor + 1
                elif(ground.king_xcor == ground.huts_xcor4):
                    ground.king_ycor = ground.king_ycor + 1
                elif(ground.king_xcor == ground.huts_xcor5):
                    ground.king_ycor = ground.king_ycor + 1
                elif(ground.king_xcor == ground.huts_xcor6):
                    ground.king_ycor = ground.king_ycor + 1
        elif(direction == 's'):
            ground.prev_pos = direction
            ground.king_xcor = 1 + ground.king_xcor
            if(ground.king_ycor == ground.huts_ycor):
                if(ground.king_xcor == ground.huts_xcor1):
                    ground.king_xcor = ground.king_xcor - 1
                elif(ground.king_xcor == ground.huts_xcor2):
                    ground.king_xcor = ground.king_xcor - 1
                elif(ground.king_xcor == ground.huts_xcor3):
                    ground.king_xcor = ground.king_xcor - 1
                elif(ground.king_xcor == ground.huts_xcor4):
                    ground.king_xcor = ground.king_xcor - 1
                elif(ground.king_xcor == ground.huts_xcor5):
                    ground.king_xcor = ground.king_xcor - 1
                elif(ground.king_xcor == ground.huts_xcor6):
                    ground.king_xcor = ground.king_xcor - 1 
        elif(direction == 'd'): 
            ground.prev_pos = direction
            ground.king_ycor = 1 + ground.king_ycor
            if(ground.king_ycor == ground.huts_ycor):
                if(ground.king_xcor == ground.huts_xcor1):
                    ground.king_ycor = ground.king_ycor - 1
                elif(ground.king_xcor == ground.huts_xcor2):
                    ground.king_ycor = ground.king_ycor - 1
                elif(ground.king_xcor == ground.huts_xcor3):
                    ground.king_ycor = ground.king_ycor - 1
                elif(ground.king_xcor == ground.huts_xcor4):
                    ground.king_ycor = ground.king_ycor - 1
                elif(ground.king_xcor == ground.huts_xcor5):
                    ground.king_ycor = ground.king_ycor - 1
                elif(ground.king_xcor == ground.huts_xcor6):
                    ground.king_ycor = ground.king_ycor - 1            
        elif(direction == ' ' and Attacker == 'k'):
            if(ground.king_xcor==ground.townhall_xcor+5 or ground.king_xcor==ground.townhall_xcor+7):
                if ground.king_ycor in range(ground.townhall_ycor-4,ground.townhall_ycor+5):
                        ground.wall1_col[-ground.townhall_ycor+4+ground.king_ycor]=self.blak

            if(ground.king_xcor==ground.townhall_xcor-5 or ground.king_xcor==ground.townhall_xcor-3):
                if ground.king_ycor in range(ground.townhall_ycor-4,ground.townhall_ycor+5):
                        ground.wall2_col[-ground.townhall_ycor+4+ground.king_ycor]=self.blak

            if(ground.king_ycor==ground.townhall_ycor-5 or ground.king_ycor==ground.townhall_ycor-3):
                if ground.king_xcor in range(ground.townhall_xcor-4,ground.townhall_xcor+6):
                        ground.wall3_col[-ground.townhall_xcor+4+ground.king_xcor]=self.blak

            if(ground.king_ycor==ground.townhall_ycor+3 or ground.king_ycor==ground.townhall_ycor+5):
                if ground.king_xcor in range(ground.townhall_xcor-4,ground.townhall_xcor+6):
                        ground.wall4_col[-ground.townhall_xcor+4+ground.king_xcor]=self.blak

            if(ground.king_xcor+1==ground.townhall_xcor or ground.king_xcor==ground.townhall_xcor+4):
                if(ground.king_ycor in range(ground.townhall_ycor,ground.townhall_ycor+3)):
                          if(ground.townhall==self.gree):
                              ground.townhall=self.yell
                          elif(ground.townhall==self.yell):
                              ground.townhall=self.rd
                          elif(ground.townhall==self.rd):
                              ground.townhall=self.blak
                              ground.townhall_xcor=-1000

            elif(ground.king_ycor+1==ground.townhall_ycor or ground.king_ycor==ground.townhall_ycor+3):
                if(ground.king_xcor in range(ground.townhall_xcor,ground.townhall_xcor+4)):
                          if(ground.townhall==self.gree):
                              ground.townhall=self.yell
                          elif(ground.townhall==self.yell):
                              ground.townhall=self.rd
                          elif(ground.townhall==self.rd):
                              ground.townhall=self.blak
                              ground.townhall_xcor=-1000

            if(ground.king_ycor == ground.huts_ycor):
                if(ground.king_xcor == ground.huts_xcor1 + 1 or ground.king_xcor == ground.huts_xcor1 - 1):
                    if(ground.king_life >= ground.hut1_life):
                        ground.hut1_life = ground.hut1_life - ground.king_damage
                        if(ground.hut1_life >= 10 and ground.hut1_life <= 20):
                            ground.hut1_color = self.gree
                        elif(ground.hut1_life >= 4 and ground.hut1_life <= 10):
                            ground.hut1_color = self.yell
                        elif(ground.hut1_life >= 0 and ground.hut1_life <= 4):
                            ground.hut1_color = self.rd
                        else: 
                            ground.king_xcor = ground.huts_xcor1
                            ground.hut1_color = self.blak
                            ground.huts_xcor1 = -1000
                elif(ground.king_xcor == ground.huts_xcor2 + 1 or ground.king_xcor == ground.huts_xcor2 - 1):
                    if(ground.king_life >= ground.hut2_life):
                        ground.hut2_life = ground.hut2_life - ground.king_damage
                        if(ground.hut2_life >= 10 and ground.hut2_life <= 20):
                            ground.hut2_color = self.gree
                        elif(ground.hut2_life >= 4 and ground.hut2_life <= 10):
                            ground.hut2_color = self.yell
                        elif(ground.hut2_life >= 0 and ground.hut2_life <= 4):
                            ground.hut2_color = self.rd
                        else:
                            ground.king_xcor = ground.huts_xcor2
                            ground.hut2_color = self.blak
                            ground.huts_xcor2 = -1000
                elif(ground.king_xcor == ground.huts_xcor3 + 1 or ground.king_xcor == ground.huts_xcor3 - 1):
                    if(ground.king_life >= ground.hut3_life):
                        ground.hut3_life = ground.hut3_life - ground.king_damage
                        if(ground.hut3_life >= 10 and ground.hut3_life <= 20):
                            ground.hut3_color = self.gree
                        elif(ground.hut3_life >= 4 and ground.hut3_life <= 10):
                            ground.hut3_color = self.yell
                        elif(ground.hut3_life >= 0 and ground.hut3_life <= 4):
                            ground.hut3_color = self.rd
                        else:
                            ground.king_xcor = ground.huts_xcor3
                            ground.hut3_color = self.blak
                            ground.huts_xcor3 = -1000
                elif(ground.king_xcor == ground.huts_xcor4 + 1 or ground.king_xcor == ground.huts_xcor4 - 1):
                    if(ground.king_life >= ground.hut4_life):
                        ground.hut4_life = ground.hut4_life - ground.king_damage
                        if(ground.hut4_life >= 10 and ground.hut4_life <= 20):
                            ground.hut4_color = self.gree
                        elif(ground.hut4_life >= 4 and ground.hut4_life <= 10):
                            ground.hut4_color = self.yell
                        elif(ground.hut4_life >= 0 and ground.hut4_life <= 4):
                            ground.hut4_color = self.rd
                        else:
                            ground.king_xcor = ground.huts_xcor4
                            ground.hut4_color = self.blak
                            ground.huts_xcor4 = -1000
                elif(ground.king_xcor == ground.huts_xcor5 + 1 or ground.king_xcor == ground.huts_xcor5 - 1):
                    if(ground.king_life >= ground.hut5_life):
                        ground.hut5_life = ground.hut5_life - ground.king_damage
                        if(ground.hut5_life >= 10 and ground.hut5_life <= 20):
                            ground.hut5_color = self.gree
                        elif(ground.hut5_life >= 4 and ground.hut5_life <= 10):
                            ground.hut5_color = self.yell
                        elif(ground.hut5_life >= 0 and ground.hut5_life <= 4):
                            ground.hut5_color = self.rd
                        else:
                            ground.king_xcor = ground.huts_xcor5
                            ground.hut5_color = self.blak
                            ground.huts_xcor5 = -1000
                elif(ground.king_xcor == ground.huts_xcor6 + 1 or ground.king_xcor == ground.huts_xcor6 - 1):
                    if(ground.king_life >= ground.hut6_life):
                        ground.hut6_life = ground.hut6_life - ground.king_damage
                        if(ground.hut6_life >= 10 and ground.hut6_life <= 20):
                            ground.hut6_color = self.gree
                        elif(ground.hut6_life >= 4 and ground.hut6_life <= 10):
                            ground.hut6_color = self.yell
                        elif(ground.hut6_life >= 0 and ground.hut6_life <= 4):
                            ground.hut6_color = self.rd
                        else:
                            ground.king_xcor = ground.huts_xcor6
                            ground.hut6_color = self.blak
                            ground.huts_xcor6 = -1000
            elif(ground.king_ycor == ground.huts_ycor + 1 or ground.king_ycor == ground.huts_ycor - 1):
                if(ground.king_xcor == ground.huts_xcor1):
                    if(ground.king_life >= ground.hut1_life):
                        ground.hut1_life = ground.hut1_life - ground.king_damage
                        if(ground.hut1_life >= 10 and ground.hut1_life <= 20):
                            ground.hut1_color = self.gree
                        elif(ground.hut1_life >= 4 and ground.hut1_life <= 10):
                            ground.hut1_color = self.yell
                        elif(ground.hut1_life >= 0 and ground.hut1_life <= 4):
                            ground.hut1_color = self.rd
                        else: 
                            ground.king_ycor = ground.huts_ycor
                            ground.hut1_color = self.blak
                            ground.huts_xcor1 = -1000
                elif(ground.king_xcor == ground.huts_xcor2):
                    if(ground.king_life >= ground.hut2_life):
                        ground.hut2_life = ground.hut2_life - ground.king_damage
                        if(ground.hut2_life >= 10 and ground.hut2_life <= 20):
                            ground.hut2_color = self.gree
                        elif(ground.hut2_life >= 4 and ground.hut2_life <= 10):
                            ground.hut2_color = self.yell
                        elif(ground.hut2_life >= 0 and ground.hut2_life <= 4):
                            ground.hut2_color = self.rd
                        else:
                            ground.king_ycor = ground.huts_ycor
                            ground.hut2_color = self.blak
                            ground.huts_xcor2 = -1000
                elif(ground.king_xcor == ground.huts_xcor3):
                    if(ground.king_life >= ground.hut3_life):
                        ground.hut3_life = ground.hut3_life - ground.king_damage
                        if(ground.hut3_life >= 10 and ground.hut3_life <= 20):
                            ground.hut3_color = self.gree
                        elif(ground.hut3_life >= 4 and ground.hut3_life <= 10):
                            ground.hut3_color = self.yell
                        elif(ground.hut3_life >= 0 and ground.hut3_life <= 4):
                            ground.hut3_color = self.rd
                        else:
                            ground.king_ycor = ground.huts_ycor
                            ground.hut3_color = self.blak
                            ground.huts_xcor3 = -1000
                elif(ground.king_xcor == ground.huts_xcor4):
                    if(ground.king_life >= ground.hut4_life):
                        ground.hut4_life = ground.hut4_life - ground.king_damage
                        if(ground.hut4_life >= 10 and ground.hut4_life <= 20):
                            ground.hut4_color = self.gree
                        elif(ground.hut4_life >= 4 and ground.hut4_life <= 10):
                            ground.hut4_color = self.yell
                        elif(ground.hut4_life >= 0 and ground.hut4_life <= 4):
                            ground.hut4_color = self.rd
                        else:
                            ground.king_ycor = ground.huts_ycor
                            ground.hut4_color = self.blak
                            ground.huts_xcor4 = -1000
                elif(ground.king_xcor == ground.huts_xcor5):
                    if(ground.king_life >= ground.hut5_life):
                        ground.hut5_life = ground.hut5_life - ground.king_damage
                        if(ground.hut5_life >= 10 and ground.hut5_life <= 20):
                            ground.hut5_color = self.gree
                        elif(ground.hut5_life >= 4 and ground.hut5_life <= 10):
                            ground.hut5_color = self.yell
                        elif(ground.hut5_life >= 0 and ground.hut5_life <= 4):
                            ground.hut5_color = self.rd
                        else:
                            ground.king_ycor = ground.huts_ycor
                            ground.hut5_color = self.blak
                            ground.huts_xcor5 = -1000
                elif(ground.king_xcor == ground.huts_xcor6):
                    if(ground.king_life >= ground.hut6_life):
                        ground.hut6_life = ground.hut6_life - ground.king_damage
                        if(ground.hut6_life >= 10 and ground.hut6_life <= 20):
                            ground.hut6_color = self.gree
                        elif(ground.hut6_life >= 4 and ground.hut6_life <= 10):
                            ground.hut6_color = self.yell
                        elif(ground.hut6_life >= 0 and ground.hut6_life <= 4):
                            ground.hut6_color = self.rd
                        else:
                            ground.king_ycor = ground.huts_ycor
                            ground.hut6_color = self.blak
                            ground.huts_xcor6 = -1000
        elif(direction == ' ' and Attacker == 'q'):
            # ground.kingcolor = self.yell
            x_target = ground.king_xcor
            y_target = ground.king_ycor

            if(ground.prev_pos == 'w'): 
                x_target = ground.king_xcor - 8
            elif(ground.prev_pos == 'a'):
                y_target = ground.king_ycor - 8
            elif(ground.prev_pos == 's'):
                x_target = ground.king_xcor + 8
            elif(ground.prev_pos == 'd'):
                y_target = ground.king_ycor + 8
            
            for i in range(0, 9):
                if((ground.copyx + 6 in range(x_target - 2, x_target + 3)) and (ground.copyy - 4 + i in range(y_target - 2, y_target + 3))):
                    ground.wall1_col[i] = self.blak
                    
                if((ground.copyx - 4 in range(x_target - 2, x_target + 3)) and (ground.copyy - 4 + i in range(y_target - 2, y_target + 3))):
                    ground.wall2_col[i] = self.blak

            for i in range(0, 10):
                if((ground.copyx - 4 + i in range(x_target - 2, x_target + 3)) and (ground.copyy - 4 in range(y_target - 2, y_target + 3))):
                    ground.wall3_col[i] = self.blak
                if((ground.copyx - 4 + i in range(x_target - 2, x_target + 3)) and (ground.copyy + 4 in range(y_target - 2, y_target + 3))):
                    ground.wall4_col[i] = self.blak
            
            for i in range(0, 4):
                c = 0
                for j in range(0, 3):
                    if(ground.townhall_xcor != -1000):
                        if((ground.copyx + i in range(x_target - 2, x_target + 3)) and (ground.copyy + j in range(y_target - 2, y_target + 3))):
                            if(ground.townhall==self.gree): 
                                ground.townhall=self.yell
                            elif(ground.townhall==self.yell):
                                ground.townhall=self.rd
                            elif(ground.townhall==self.rd):
                                ground.townhall=self.blak
                                ground.townhall_xcor=-1000
                            c = 1
                            break
                if(c == 1):
                    break
                    
            if((ground.cx1 in range(x_target - 2, x_target + 3)) and (ground.cy1 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.chealth):
                    ground.chealth = ground.chealth - ground.queen_damage
                    if(ground.chealth >= 5 and ground.chealth <= 10):
                        ground.cannon = self.blu
                    elif(ground.chealth >= 0 and ground.chealth <= 4):
                        ground.cannon = self.rd
                    else: 
                        ground.cannon = self.blak
                        ground.cx1 = -1000
            
            if((ground.cx2 in range(x_target - 2, x_target + 3)) and (ground.cy2 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.chealth1):
                    ground.chealth1 = ground.chealth1 - ground.queen_damage
                    if(ground.chealth1 >= 5 and ground.chealth1 <= 10):
                        ground.cannon1 = self.blu
                    elif(ground.chealth1 >= 0 and ground.chealth1 <= 4):
                        ground.cannon1 = self.rd
                    else: 
                        ground.cannon1 = self.blak
                        ground.cx2 = -1000
            
            if((ground.win >=1 and (ground.cx3 in range(x_target - 2, x_target + 3))) and (ground.cy3 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.chealth2):
                    ground.chealth2 = ground.chealth2 - ground.queen_damage
                    if(ground.chealth2 >= 5 and ground.chealth2 <= 10):
                        ground.cannon2 = self.blu
                    elif(ground.chealth2 >= 0 and ground.chealth2 <= 4):
                        ground.cannon2 = self.rd
                    else: 
                        ground.cannon2 = self.blak
                        ground.cx3 = -1000

            if(ground.win == 2 and ((ground.cx4 in range(x_target - 2, x_target + 3))) and (ground.cy4 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.chealth3):
                    ground.chealth3 = ground.chealth3 - ground.queen_damage
                    if(ground.chealth3 >= 5 and ground.chealth3 <= 10):
                        ground.cannon3 = self.blu
                    elif(ground.chealth3 >= 0 and ground.chealth3 <= 4):
                        ground.cannon3 = self.rd
                    else: 
                        ground.cannon3 = self.blak
                        ground.cx4 = -1000

            if((ground.wtx1 in range(x_target - 2, x_target + 3)) and (ground.wty1 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.wt_health1):
                    ground.wt_health1 = ground.wt_health1 - ground.queen_damage
                    if(ground.wt_health1 >= 5 and ground.wt_health1 <= 10):
                        ground.wt_color1 = self.blu
                    elif(ground.wt_health1 >= 0 and ground.wt_health1 <= 4):
                        ground.wt_color1 = self.rd
                    else: 
                        ground.wt_color1 = self.blak
                        ground.wtx1 = -1000
            
            if((ground.wtx2 in range(x_target - 2, x_target + 3)) and (ground.wty2 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.wt_health2):
                    ground.wt_health2 = ground.wt_health2 - ground.queen_damage
                    if(ground.wt_health2 >= 5 and ground.wt_health2 <= 10):
                        ground.wt_color2 = self.blu
                    elif(ground.wt_health2 >= 0 and ground.wt_health2 <= 4):
                        ground.wt_color2 = self.rd
                    else: 
                        ground.wt_color2 = self.blak
                        ground.wtx2 = -1000
            
            if((ground.win >=1 and (ground.wtx3 in range(x_target - 2, x_target + 3))) and (ground.wty3 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.wt_health3):
                    ground.wt_health3 = ground.wt_health3 - ground.queen_damage
                    if(ground.wt_health3 >= 5 and ground.wt_health3 <= 10):
                        ground.wt_color3 = self.blu
                    elif(ground.wt_health3 >= 0 and ground.wt_health3 <= 4):
                        ground.wt_color3 = self.rd
                    else: 
                        ground.wt_color3 = self.blak
                        ground.wtx3 = -1000

            if(ground.win == 2 and ((ground.wtx4 in range(x_target - 2, x_target + 3))) and (ground.wty4 in range(y_target - 2, y_target + 3))):
                if(ground.king_life >= ground.wt_health4):
                    ground.wt_health4 = ground.wt_health4 - ground.queen_damage
                    if(ground.wt_health4 >= 5 and ground.wt_health4 <= 10):
                        ground.wt_color4 = self.blu
                    elif(ground.wt_health4 >= 0 and ground.wt_health4 <= 4):
                        ground.wt_color4 = self.rd
                    else: 
                        ground.wt_color4 = self.blak
                        ground.wtx4 = -1000

            if(ground.huts_ycor in range(y_target - 2, y_target + 3)):
                if(ground.huts_xcor1 in range(x_target - 2, x_target + 3)):
                    if(ground.king_life >= ground.hut1_life):
                        ground.hut1_life = ground.hut1_life - ground.queen_damage
                        if(ground.hut1_life >= 10 and ground.hut1_life <= 20):
                            ground.hut1_color = self.gree
                        elif(ground.hut1_life >= 4 and ground.hut1_life <= 10):
                            ground.hut1_color = self.yell
                        elif(ground.hut1_life >= 0 and ground.hut1_life <= 4):
                            ground.hut1_color = self.rd
                        else: 
                            ground.hut1_color = self.blak
                            ground.huts_xcor1 = -1000
                elif(ground.huts_xcor2 in range(x_target - 2, x_target + 3)):
                    if(ground.king_life >= ground.hut2_life):
                        ground.hut2_life = ground.hut2_life - ground.queen_damage
                        if(ground.hut2_life >= 10 and ground.hut2_life <= 20):
                            ground.hut2_color = self.gree
                        elif(ground.hut2_life >= 4 and ground.hut2_life <= 10):
                            ground.hut2_color = self.yell
                        elif(ground.hut2_life >= 0 and ground.hut2_life <= 4):
                            ground.hut2_color = self.rd
                        else:
                            ground.hut2_color = self.blak
                            ground.huts_xcor2 = -1000
                elif(ground.huts_xcor3 in range(x_target - 2, x_target + 3)):
                    if(ground.king_life >= ground.hut3_life):
                        ground.hut3_life = ground.hut3_life - ground.queen_damage
                        if(ground.hut3_life >= 10 and ground.hut3_life <= 20):
                            ground.hut3_color = self.gree
                        elif(ground.hut3_life >= 4 and ground.hut3_life <= 10):
                            ground.hut3_color = self.yell
                        elif(ground.hut3_life >= 0 and ground.hut3_life <= 4):
                            ground.hut3_color = self.rd
                        else:
                            ground.hut3_color = self.blak
                            ground.huts_xcor3 = -1000
                elif(ground.huts_xcor4 in range(x_target - 2, x_target + 3)):
                    if(ground.king_life >= ground.hut4_life):
                        ground.hut4_life = ground.hut4_life - ground.queen_damage
                        if(ground.hut4_life >= 10 and ground.hut4_life <= 20):
                            ground.hut4_color = self.gree
                        elif(ground.hut4_life >= 4 and ground.hut4_life <= 10):
                            ground.hut4_color = self.yell
                        elif(ground.hut4_life >= 0 and ground.hut4_life <= 4):
                            ground.hut4_color = self.rd
                        else:
                            ground.hut4_color = self.blak
                            ground.huts_xcor4 = -1000
                elif(ground.huts_xcor5 in range(x_target - 2, x_target + 3)):
                    if(ground.king_life >= ground.hut5_life):
                        ground.hut5_life = ground.hut5_life - ground.queen_damage
                        if(ground.hut5_life >= 10 and ground.hut5_life <= 20):
                            ground.hut5_color = self.gree
                        elif(ground.hut5_life >= 4 and ground.hut5_life <= 10):
                            ground.hut5_color = self.yell
                        elif(ground.hut5_life >= 0 and ground.hut5_life <= 4):
                            ground.hut5_color = self.rd
                        else:
                            ground.hut5_color = self.blak
                            ground.huts_xcor5 = -1000
                elif(ground.huts_xcor6 in range(x_target - 2, x_target + 3)):
                    if(ground.king_life >= ground.hut6_life):
                        ground.hut6_life = ground.hut6_life - ground.queen_damage
                        if(ground.hut6_life >= 10 and ground.hut6_life <= 20):
                            ground.hut6_color = self.gree
                        elif(ground.hut6_life >= 4 and ground.hut6_life <= 10):
                            ground.hut6_color = self.yell
                        elif(ground.hut6_life >= 0 and ground.hut6_life <= 4):
                            ground.hut6_color = self.rd
                        else:
                            ground.hut6_color = self.blak
                            ground.huts_xcor6 = -1000

        if(ground.king_xcor == ground.columns or ground.king_xcor==ground.rows):
            ground.king_xcor = 20
            ground.king_ycor = 150

        return direction