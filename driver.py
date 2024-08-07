from sqlite3 import Row
from movement import *
from maps import *
from guards import *
from winLossStatements import *

def mapSelect():
    bright_cyan("At anytime press \"q\" to quit and \"h\" for help")
    bright_cyan("What map would you like to play? (1,2, or 3)")
    input = getInput()
    return(input)

def printMap(map):
    for x in map:
        print(''.join(x))

    #more jank. This function is neccessary to keep the game in place while moving   
    setCursor(True, map)

def run(mapNum):
    map, currentRow, currentColumn = getMap(mapNum)
    guardList = getGuards(mapNum)
    printMap(map)
    while(True):
        input = getInput()
        if(input == "q"):
            loseGame(map)
        elif(input == "h"):
            #this jank is becuase of how the map is being overwritten
            #moving the cursor does not delete everything, so without the
            #spaces you will still be able to see parts of the old map
            print("Help Menu:                                             \n"+
                  "w -> move up                                           \n"+
                  "a -> move left                                         \n"+
                  "s -> move down                                         \n"+
                  "d ->move right                                         \n"+
                  "Try to reach the \"*\" on the map,                     \n"+
                  "and make sure to avoid the guards.                       ")
        else:
            #main gameplay loop
            map, currentRow, currentColumn = updateMap(map, currentRow, currentColumn, input)
            updateGuard(guardList, map)
            
        printMap(map)
        

if __name__ == "__main__":
    mapNum = mapSelect()
    run(mapNum)