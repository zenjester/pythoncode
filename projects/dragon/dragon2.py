#dragon2.py dragon.py modularised
#andyp 23.03.13

import random
import time
import dragonMod

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    dragonMod.displayIntro()

    caveNumber = dragonMod.chooseCave()

    dragonMod.checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
