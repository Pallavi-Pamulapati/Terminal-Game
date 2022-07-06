# 2D game in Python 3

## Description 
This is a basic version of clash of clans. Initially the Village here contains townhall, townwall, huts, cannons, wizard towers and a king or queen (based on the input given). The king can move using the keys w/a/s/d (up/down/left/right) and attack on the defences using space key. The troops of the king (Barbarians, balloons and Archers) are called using the keys (z/x/c, i/o/p, j/k/l) and try to destroy as many buildings as possible. If the king and his troops destroys all the buildings in all the levels then the user has won the game.

## Rules and Functionalities
### Movement and attack by King 
- King can move UP/DOWN/LEFT/RIGHT using the keys W/A/S/D and can attack the defences using space key.
- King can move in to the place of the defences only after defeating them. 
- Barbarians, ballons and archers can enter the village from 9 spawning points by pressing the keys z/x/c, i/o/p and j/k/l. And Only one troop can come from a spawning point.
- Movement of the queen is same as movement of the king and queen attacks the distant defences or buildings when space key is pressed.

## Buildings 
- Huts, TownWalls and TownHall are to be destroyed by the King and his troops. Each building has a certain life and based on the damaged caused by the king or his troops the color of the buildings changes.
    1. Green - if the damged caused by the king and army is less than 50%
    2. Yellow - If the damged caused is greater than 50% and less than 80%
    3. Red - If the damage caused is greater than 80%
    4. Bulding vanishes if the damage level is 100%

## cannons
- Canons have a ceratin range of attacking where the king and troops when enetered in that ranged will be damaged by certain number of damage points
- Cannons are destroyed by queen and balloons

## Features
- Life of the building is indicated by its color.
- Sound effects are added to the movement of the king. 
- The movements and attack of the barbarians are automated. 
- If all the buildings in 3 levels are destroyed then game ends by displaying "Victory" 
- If the troops and king are dead without destroying the bulidings then game ends by displaying "Defeat"
- Life of the king is dispalyed as health bar on the top.
- Replay feature is implemented where upon running the replay.py and giving the input as i, the ith previous game would be played on the screen
- Health bar of the king is displayed at the bottom left corner of the screen indicating the health of the king
- Archers and Balloons are implemented 
- Archer Queen is implemented 
- Levels are implemented 
- Wizard Towers are implemented and are increased after every level
- Balloons can be attacked by the wizard tower
- Queen can destroy the wizard towers and cannons