#Translates slide puzzle solutions from one format to another
#
#Input format is a list of directions from a black tile
#Output format is a list of tiles to move based on an initial tile numbering
#  -This list is then put into java script commands that can be used on a particular slide puzzle website (https://puzzles.getbackup.tv/)
#
#
#Program simulates the solution being played out according to the commands "up", "down", "left, "right"
#The commands are carried out on a numbered tile set(Array), the tiles moved with each commands are recorded
#Recorded list of acted upon tile numbers are then output as java commands enterable here: (https://puzzles.getbackup.tv/)


#Determined Move pattern collected prior
FileWithMovePattern = ".\PuzzlePatterns\Pattern3"

#Starting Conditions
#Tile Array holding Tile numbers in location
TArray = [[0,1,2,3],[4,5,6,7],[8,-1,9,10],[11,12,13,14]]

blankRow = 2
blankCol = 1

maxRow = 3
maxCol = 3

#Array for output command string
FinalMoveTileArray = []

#Checks if Input command is valid under the current puzzle state
def MoveDirValid(d):
    if(d == "right"):
        if(blankCol >= maxCol):
            return False
        else:
            return True
        print("r")
    elif (d == "left"):
        if(blankCol <= 0):
            return False
        else:
            return True
        print("l")
    elif (d == "up"):
        if(blankRow <= 0):
            return False
        else:
            return True
        print("u")
    elif (d == "down"):
        if(blankRow >= maxRow):
            return False
        else:
            return True
        print("d")
    else:
        print("Error: Invalid Direction String : ",d)
        return False

#Takes a command and changes the puzzle state and Tile Array accordingly
def MoveDir(d):
    #Blank Tile location stored and changed over each move
    global blankRow
    global blankCol

    #Position to move into blank position(Action Tile), set to current blank position
    newCol = blankCol
    newRow = blankRow

    #Tile number to "move" blank tile tile to, initialized to -1
    swapTile = -1
    if(MoveDirValid(d) == False):
        print("Error: Invalid Move")
        return -1
    else:
        #Determine Action Tile based on input command
        if(d == "right"):
            newCol = blankCol + 1
        elif (d == "left"):
            newCol = blankCol - 1
        elif (d == "up"):
            newRow = blankRow - 1
        elif (d == "down"):
            newRow = blankRow + 1
        #print(newRow,", ",newCol)
        #Determine tile number that is moved, and simulate movement in array
        swapTile = TArray[newRow][newCol]
        TArray[newRow][newCol] = -1
        TArray[blankRow][blankCol] = swapTile
        #Record Tile number moved in array
        FinalMoveTileArray.append(swapTile)
        #track new blank tile position
        blankRow = newRow
        blankCol = newCol

def main():
    #Open file containing move commands, Simulate each command
    with open(FileWithMovePattern, "r") as f:
        for line in f:
            line = line.rstrip()
            #print(line)
            MoveDir(line)
    #Based on tiles moved, output java commands
    outString = ''
    for tile in FinalMoveTileArray:
        addString = "puzzle.moveTile(TL[" + str(tile) + "]);"
        outString += addString
    print(outString)

if __name__ == "__main__":
    main()


