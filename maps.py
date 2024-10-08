from guards import checkCaught
from winLossStatements import caughtLoseGame, loseGame


def getMap(mapNum):
    #returns the map and the starting position
    if(mapNum == "1"):
        map =   [
                [" "," "," ","_","_","_","_","_","_","_"," "," "," "," "," "," "," "," "," "," "],
                ["_","_","/"," "," "," "," "," "," "," ","\\"," "," "," "," "," "," "," "," "," "],
                ["|","1"," "," "," "," "," "," "," "," "," ","\\"," "," "," "," "," "," "," "," "],
                ["¯","¯","¯","¯","\\"," ","#","#","$"," "," "," ","\\"," "," "," "," "," "," "," "],
                [" "," "," "," "," ","\\"," "," "," "," "," "," "," ","\\"," "," "," "," "," "," "],
                [" "," "," "," "," "," ","¯","¯","¯"," "," "," "," "," ","\\"," "," "," "," "," "],
                [" "," "," "," "," "," "," "," ","|"," "," "," "," "," "," ","\\"," "," "," "," "],
                ["_","_","_","_","_","_","_","_","|"," ","|"," "," "," "," "," ","\\","_","_","_"],
                ["*"," "," "," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "," ","*"],
                ["¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯"]
                ]
        return(map, 2, 1)
    elif(mapNum == "2"):
        map =   [
                [" ","_","_","_"," "," "," "," ","_","_","_","_","_"," "," "," "," ","_","_","_"," "],
                ["/"," "," "," ","\\"," "," ","/"," "," "," "," "," ","\\"," "," ","/"," "," "," ","\\"],
                ["|"," ","*"," ","|"," "," ","|"," "," ","*"," "," ","|"," "," ","|"," ","*"," ","|"],
                ["|"," "," "," ","|"," "," ","|"," "," "," "," "," ","|"," "," ","|"," "," "," ","|"],
                ["|"," "," "," ","|"," "," ","|"," "," "," "," "," ","|"," "," ","|"," "," "," ","|"],
                ["|","#","$"," ","|"," "," ","|"," "," ","$","#","#","|"," "," ","|"," ","#"," ","|"],
                ["|"," "," "," ","|"," "," "," ","\\"," "," "," ","/"," "," "," ","|"," ","#"," ","|"],
                ["|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," ","$"," ","|"],
                ["|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"],
                ["|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"],
                ["|"," ","$","#","|"," "," "," ","|"," ","$"," ","|"," "," "," ","|"," "," "," ","|"],
                ["|"," "," "," ","\\"," "," "," ","/"," ","#"," ","\\"," "," "," ","/"," "," "," ","|"],
                ["|"," "," "," "," ","-","-","-"," "," ","#"," "," ","-","-","-"," "," "," "," ","|"],
                ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#","#","$"," "," ","|"],
                ["|"," "," "," "," "," "," "," "," "," ","1"," "," "," "," "," "," "," "," "," ","|"],
                [" ","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯","¯"," "],   
                ]
        return(map, 14, 10)
    else:
        map =   [
                [" "," "," "," "," "," "," "," ","_","_","_"," "," "," "," "," "," "],
                [" "," "," "," "," "," "," ","/"," "," "," ","\\"," "," "," "," "," "],
                [" "," "," "," "," "," ","/"," "," "," "," "," ","\\"," "," "," "," "],
                [" "," "," "," "," ","/"," "," "," "," "," "," "," ","\\"," "," "," "],
                [" "," "," "," ","/"," "," "," ","|","¯","|"," "," "," ","\\"," "," "],
                [" "," "," ","/"," "," "," "," ","|"," ","|"," "," "," "," ","\\"," "],
                [" "," ","|"," "," "," "," "," ","|","_","|"," "," "," "," "," |"," "],
                [" "," ","|"," "," ","$","#","#"," ","*"," ","#","#","$"," "," ","|"],
                [" "," ","|"," "," "," "," "," ","|","¯","|"," "," "," "," "," ","|"],
                [" "," "," ","\\"," "," "," "," ","|"," ","|"," "," "," "," ","/"," "],
                [" "," "," "," ","\\"," "," "," ","|"," ","|"," "," "," ","/"," "," "],
                [" "," "," "," "," ","\\"," "," "," ","¯"," "," "," ","/"," "," "," "],
                [" "," "," "," "," "," ","\\"," "," "," "," "," ","/"," "," "," "," "],
                [" "," "," "," "," "," "," ","\\"," ","1"," ","/"," "," "," "," "," "],
                [" "," "," "," "," "," "," "," ","¯","¯","¯"," "," "," "," "," "," "]
                ]
        return (map,13,9)

def updateMap(map, currentRow, currentColumn, input):
    from movement import validateBoundary
    #this is a god method. Needs refactored BAD. 
    #from this method all the validations get handled
    #this includes boundaries, win spots, gaurd triggers
    #boundary tiles
    map[currentRow][currentColumn] = " "

    rowUpdate = 0
    colUpdate = 0
    #find direction and update target
    if(input == 'w'):
        #up one
        rowUpdate -= 1
    elif(input == 'a'):
        #left one
        colUpdate -= 1
    elif(input == 's'):
        #down one
        rowUpdate += 1
    elif(input == 'd'):
        #right one
        colUpdate += 1

    #checks if the move is within the boundaries, if it is the move is recorded
    #if it returns true, you hit the boundary and the move is not recorded
    if(validateBoundary(map, currentRow, currentColumn, rowUpdate, colUpdate)):
        map[currentRow][currentColumn] = "1"
        return(map, currentRow, currentColumn)
    else:
        currentRow += rowUpdate
        currentColumn += colUpdate

    #check to see if a gaurd was triggered, true means the game is lost
    caughtFlag = checkCaught(map, currentRow, currentColumn)
    if(caughtFlag is True):
        caughtLoseGame(map)

    #update new and previous tile, return the map
    map[currentRow][currentColumn] = "1"
    return(map, currentRow, currentColumn)