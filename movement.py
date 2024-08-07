import msvcrt
from driver import winGame

def getInput():
    #get user input without enter from msvcrt and clean the b tag from string(byte)
    userInput = ""

    #loop while the input is not valid
    validateFlag = False
    while(validateFlag is False):
        userInput = str(msvcrt.getch())
        userInput = userInput[2]
        validateFlag = validateMovement(userInput)
    
    return(userInput)

def validateMovement(input):
    #check if wasd
    inputSet = {"w","a","s","d","q"}
    if(input in inputSet):
        return True

def validateBoundary(map, currentRow, currentColumn, rowUpdate, colUpdate):
    #super jank win condition. Update this in the future
    if(map[(currentRow+rowUpdate)][(currentColumn+colUpdate)] == "*"):
        #update spot
        map[(currentRow+rowUpdate)][(currentColumn+colUpdate)] = "1"
        winGame(map)

    boundarySet = {"-", "|", "\\", "/", "_", "¯"}

    if(map[(currentRow+rowUpdate)][(currentColumn+colUpdate)] in boundarySet):
        return True
    else:
        return False



