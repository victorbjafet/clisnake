import os # to clear the screen
from random import randint # to generate random numbers
from pytimedinput import timedInput # to manage keyboard input 
import sqlite3
sqliteConnection = sqlite3.connect('database.db')
sqliteCursor = sqliteConnection.cursor()


# array of characters to be displayed
visualCharArr = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                 ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

snakeArr = [(5,5)] # array of snake body parts, coordinates in tuples form (y,x) yes ik its backwards idc
snakeDir = 0 # direction of snake, 0 = right, 90 = up, 180 = left, 270 = down
newApple = False # if true, generate new apple
apple = (randint(1,14),randint(1,30)) # generates first apple


while True: # main loop that runs forever
    txt,_ = timedInput( 'input: ' , timeout = 0.1) # gets keyboard input every 0.1 seconds

    if txt == "w": # if w is pressed, change direction to up if not already going down
        if snakeDir != 270:
            snakeDir = 90
    elif txt == "a": # if a is pressed, change direction to left if not already going right
        if snakeDir != 0:
            snakeDir = 180
    elif txt == "s": # if s is pressed, change direction to down if not already going up
        if snakeDir != 90:
            snakeDir = 270
    elif txt == "d": # if d is pressed, change direction to right if not already going left
        if snakeDir != 180:
            snakeDir = 0


    if snakeDir == 90: # if snake is going up
        if (snakeArr[-1][0]-1,snakeArr[-1][1]) == apple: # if snake is going to eat apple
            newApple = True # set new apple to true
        elif visualCharArr[snakeArr[-1][0]-1][snakeArr[-1][1]] == "#" or visualCharArr[snakeArr[-1][0]-1][snakeArr[-1][1]] == "O": # if snake is going to hit wall or itself
            break # break out of loop (TRIGGER)
        snakeArr.append((snakeArr[-1][0]-1,snakeArr[-1][1])) # add new body part to snake

    elif snakeDir == 180: # if snake is going left
        if (snakeArr[-1][0],snakeArr[-1][1]-1) == apple: # if snake is going to eat apple
            newApple = True # set new apple to true
        elif visualCharArr[snakeArr[-1][0]][snakeArr[-1][1]-1] == "#" or visualCharArr[snakeArr[-1][0]][snakeArr[-1][1]-1] == "O": # if snake is going to hit wall or itself
            break # break out of loop (TRIGGER)
        snakeArr.append((snakeArr[-1][0],snakeArr[-1][1]-1)) # add new body part to snake

    elif snakeDir == 270:  # if snake is going down
        if (snakeArr[-1][0]+1,snakeArr[-1][1]) == apple: # if snake is going to eat apple
            newApple = True # set new apple to true
        elif visualCharArr[snakeArr[-1][0]+1][snakeArr[-1][1]] == "#" or visualCharArr[snakeArr[-1][0]+1][snakeArr[-1][1]] == "O": # if snake is going to hit wall or itself
            break # break out of loop (TRIGGER)
        snakeArr.append((snakeArr[-1][0]+1,snakeArr[-1][1])) # add new body part to snake

    elif snakeDir == 0: # if snake is going right
        if (snakeArr[-1][0],snakeArr[-1][1]+1) == apple: # if snake is going to eat apple
            newApple = True # set new apple to true
        elif visualCharArr[snakeArr[-1][0]][snakeArr[-1][1]+1] == "#" or visualCharArr[snakeArr[-1][0]][snakeArr[-1][1]+1] == "O": # if snake is going to hit wall or itself
            break # break out of loop (TRIGGER)
        snakeArr.append((snakeArr[-1][0],snakeArr[-1][1]+1)) # add new body part to snake

    if newApple != True: # if snake did not eat apple
        snakeArr.pop(0) # remove last body part of snake
    else: # if snake did eat apple
        apple = (randint(1,14),randint(1,30)) # generate new apple
        newApple = False # set new apple to false


    os.system('cls' if os.name == 'nt' else 'clear') # clear screen


    # configure array based on current state of snake and apple (does not change the outside walls, hence the 1,15 and 1,31)
    for i in range(1,15): # for each row
        for j in range(1,31): # for each column
            if (i,j) in snakeArr: # if coordinate is in snake array
                visualCharArr[i][j] = "O" # set character to O
            elif (i,j) == apple: # if coordinate is apple
                visualCharArr[i][j] = "A" # set character to A
            else: # if coordinate is empty
                visualCharArr[i][j] = " " # set character to space
    

    for list in visualCharArr: # for each row
        for character in list: # for each column
            print(character,end="") # print character without newline
        print("") # newline at end of row




#out of loop
################################

#LEAVING THE GAME LOOP MEANS YOU DIED, IT IS THE TRIGGER FOR ALL THE SQL CODE BELOW WHICH IS THE STORED PROCEDURE
#TRIGGERS: LINES 54, 61, 68, 75
#STORED PROCEDURE: LINES 121 AND 122

############################
os.system('cls' if os.name == 'nt' else 'clear') # clears screen

print("You died!\nYou ate " + str(len(snakeArr) - 1) + " apples.") # print game over

appleCount = len(snakeArr) - 1 # get apple count

sqliteCursor.execute('INSERT INTO games (appleCount) VALUES (?);',(appleCount,)) # insert apple count into database (STORED PROCEDURE)
sqliteCursor.execute("SELECT appleCount FROM games;") # get all apple counts (STORED PROCEDURE)
ans = sqliteCursor.fetchall() # store all apple counts in ans 

totalApples = 0
for i in ans: # add all apple counts
    totalApples += int(str(i).strip("(),")) # strip tuple from string plus accumulate total apples eaten all time

print("Total games played all time: " + str(len(ans))) # print games played
print("Total apples eaten all time: " + str(totalApples)) # print total apples eaten
print("Average apples eaten per game: " + str(totalApples/len(ans)).strip("0.")) # print average apples eaten
print("Most apples eaten: " + str(max(ans)).strip("(),")) # print most apples eaten

sqliteConnection.commit() # commit changes to database
sqliteConnection.close() # close connection to database

