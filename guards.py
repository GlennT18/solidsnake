def getGuards(mapNum):
    #creates guard list and fills it depending on the map
    #the matrices are predetermined since I manually built the 
    #maps but there is a helper method at the bottom of this
    #file to find where the guards are
    guards = []
    if(mapNum == "1"):
        guard1 = [3,8]
        guards.append(guard1)
    elif(mapNum == "2"):
        #center column guards
        guard1 = [5, 10]
        guard2 = [10,10]
        guards.append(guard1)
        guards.append(guard2)

        #left column guards
        guard3 = [10, 2]
        guard4 = [5, 2]
        guards.append(guard3)
        guards.append(guard4)

        #right column guards
        guard5 = [13, 17]
        guard6 = [7, 18]
        guards.append(guard5)
        guards.append(guard6)
    else:
        guard7 = [7,5]
        guard8 = [7,13]
        guards.append(guard7)
        guards.append(guard8)
    return guards

def updateGuard(guards, map):
    #figure out what way they are currently looking
    #spin them clockwise 
    for guard in guards:
        x = guard[0]
        y = guard[1]
        if(map[x+1][y] == "#"):
            #down
            removeLight(map, (x+1), y)
            removeLight(map, (x+2), y)
            moveFlashlight(map, (x+1), (y-1), (x+2), (y-2))
        elif(map[x+1][y-1] == "#"):
            #down left
            removeLight(map, (x+1), (y-1))
            removeLight(map, (x+2), (y-2))
            moveFlashlight(map, x, (y-1), x, (y-2))
        elif(map[x][y-1] == "#"):
            #left
            removeLight(map, (x), (y-1))
            removeLight(map, (x), (y-2))
            moveFlashlight(map, (x-1), (y-1), (x-2), (y-2))
        elif(map[x-1][y-1] == "#"):
            #up left
            removeLight(map, (x-1), (y-1))
            removeLight(map, (x-2), (y-2))
            moveFlashlight(map, (x-1), y, (x-2), y)
        elif(map[x-1][y] == "#"):
            #up
            removeLight(map, (x-1), y)
            removeLight(map, (x-2), y)
            moveFlashlight(map, (x-1), (y+1), (x-2), (y+2))
        elif(map[x-1][y+1] == "#"):
            #up right
            removeLight(map, (x-1), (y+1))
            removeLight(map, (x-2), (y+2))
            moveFlashlight(map, x, (y+1), x, (y+2))
        elif(map[x][y+1] == "#"):
            #right
            removeLight(map, x, (y+1))
            removeLight(map, x, (y+2))
            moveFlashlight(map, (x+1), (y+1), (x+2), (y+2))
        else:
            #down right
            removeLight(map, (x+1), (y+1))
            removeLight(map, (x+2), (y+2))
            moveFlashlight(map, (x+1), y, (x+2), y)

def moveFlashlight(map, x1, y1, x2, y2):
    #moves the # intot he correct location 
    boundarySet = {"-", "|", "\\", "/", "_","¯"}
    if(map[x1][y1] not in boundarySet):
        map[x1][y1] = "#"
    if(map[x2][y2] not in boundarySet):
        map[x2][y2] = "#"

def removeLight(map, x, y):
    #removes the # once the guard turns and replaces it with 0
    boundarySet = {"-", "|", "\\", "/", "_", " ", "¯"}
    if(map[x][y] not in boundarySet):
        map[x][y] = " "
    elif(map[x][y] == "#"):
        map[x][y] = " "

def checkCaught(map, row, column):
    #checks to see if the user got cuaght
    if(map[row][column] == "#" or map[row][column] == "$"):
        return True
    else:
        return False

#helper method for finding the guards non-manually
    #row = 0
    #col = 0
    #for x in map:
    #    for chara in x:
    #        if chara == "$":
    #            print(row, col)
    #        col += 1
    #    row += 1
    #    col = 0
    