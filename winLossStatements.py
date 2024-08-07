from colorist import *

def setCursor(flag, map):
    rows = len(map)
    LINE_CLEAR = '\x1b[2k'
    if(flag == True):
        #moves cursor up, game continues
        print('\033[{}A'.format(rows), end=LINE_CLEAR)
    else:
        #moves cursor down, game ends
        print('\033[{}E'.format(rows), end=LINE_CLEAR)

def loseGame(map):
    setCursor(False, map)
    bright_red("You quit the game!")
    quit()

def caughtLoseGame(map):
    setCursor(False, map)
    bright_red("You got cuaght, try again!")
    quit()

def winGame(map):
    setCursor(False, map)
    bright_yellow("Congrats you win!")
    quit()