import random #Imports the ability to use the random function
g_rows = 8 #Grid rows
g_column = 8 #Grid columns
add_chests = 0 #Chest counter
add_bandits = 0 #Bandit counter
g_coins = 0 #Total coins
moves = 0 #Total moves
chestLocation = {} #Chest location dictionary
debug = False #Debug mode
pVerticalMove = 0 #Player vertical move
pHorizontalMove = 0 #Player horizontal move
pVerticalCopy = pVerticalMove #Player vertical move copy
pHorizontalCopy = pHorizontalMove #Player horizontal move copy


while True:
    #The while True lets the program loop back to the menu
    print("====TREASURE HUNT====")
    #Prints a title which indicates that this is the main menu
    print("1. Play Game")
    #The user is displayed with two options
    print("2. Quit")
    selection = (input("Please enter your choice: "))
    #The user's choice will be assigned to the selection variable
    
    if selection == "1" :
        print("====PLAY THE GAME====")
        #If the user chooses a 1, it will play the game
        print("Here are a list of possible grid sizes:")
        #The program prints a list of possible grids for the player to choose
        print("1. 5 x 5")
        print("2. 8 x 8")
        print("3. 10 x 10")
        print("4. 12 x 12")
        print("5. 15 x 15")
        while True:
        #A loop is run for the player to choose their grid
           try:
               gridChoice = int(input("Please select a grid 1-5: "))
        #The player will be asked to input their choice
           except ValueError:
               print("Please enter a valid number")
        #If it's not an integer, an error message is given
        #And the input for a valid number will loop
           else:
               if 1 <= gridChoice <= 5:
        #If the player's input is valid, it will break out the loop
                   break
               else:
                   print("Please enter a number between 1-5")
        #If its not between 1-5, the ask for input will loop
        if gridChoice == 1:
        #For each possible grid size, the program will set the grid values
            g_rows = 5
            g_column = 5
        elif gridChoice == 2:
            g_rows = 8
            g_column = 8
        elif gridChoice == 3:
            g_rows = 10
            g_column = 10
        elif gridChoice == 4:
            g_rows = 12
            g_column = 12
        elif gridChoice == 5:
            g_rows = 15
            g_column = 15
        else:
            print("Enter a number between 1-5")


        pStart_v = g_rows - 1 #Players vertical start position
        pStart_h = 0 #Players horizontal start position
        pInGame_v = pStart_v #Players in game vertical position
        pInGame_h = pStart_h #Players in game horizontal position
        gridSize = g_rows * g_column - 1
        #The size of the grid is determined for it to be used
        #In order to find fractions of it later on
        maxBC = gridSize /4
        #The maximum number of bandits & chests is one quarter of the grid size
        maxBandit = maxBC /3
        #The maximum number of bandits is one third of the possible quarter
        maxChest = maxBandit * 2
        #The maximum number of chests is two third of the possible quarter
        maxBandit = round(maxBandit)
        maxChest = round(maxChest)
        #The maximum chests & bandits are rounded to be whole numbers

        while True:
            try:
                print("Enter a number between 10 and", maxChest,"for the amount of chests")
                chests = int(input())
        #The program will ask for a number of chests between the calculated maximum chests
            except ValueError:
                print("Please enter a valid number")
        #Checks if the number is an integer
            else:
                if 10 <= chests <= maxChest:
        #Checks if the number is between 10 and the maximum number of chests
                    print("Chests valid")
        #Tells the player that it is valid
                    break
        #Breaks out of the loop to move onto the next loop
                else:
                    print("Please enter a number between 10 and", maxChest)
        #If its not between the right numbers, the ask for input will loop again
        while True:
            try:
                print("Enter a number between 5 and", maxBandit,"for the amount of bandits")
                bandits = int(input())
        #Program will ask for number of bandits between the calculated maximum number of bandits
            except ValueError:
                print("Please enter a valid number")
        #Gives error message if number is not an integer
            else:
                if 5 <= bandits <= maxBandit:
        #Checks if number is between 5 and maximum number of bandits
                    print("Bandits valid")
        #Tells the player that it is valid
                    break
        #Breaks out of the loop so it doesn't ask for a new input
                else:
                    print("Please enter a number between 5 and", maxBandit)
        #If its not between the right numbers, it will give an error message and loop

                    


        
        grid = [["⌂" for count in range(g_rows)] for column in range(g_column)]
        #⌂ will be printed for every number between the number of rows and columns
        grid [pInGame_v][pInGame_h] = "☺"
        #☺ will be printed for the players position
        
        while add_bandits != bandits :
        #This code will run if the bandits doesn't equal the set bandit number
            GridV = random.randrange(g_rows)
            #The bandit vertical position is random between the set number of grid rows
            GridH = random.randrange(g_column)
            #The bandit horizontal position is random between the set number of grid columns
            if grid [GridV][GridH] == "⌂" :
            #The bandit position will be created if it is on an empty space
                grid [GridV][GridH] = "B"
            #The bandits are represented as a 'B'
                add_bandits = add_bandits + 1
            #1 is added to the bandit count so that the loop can continue

        while add_chests != chests :
        #This code will run if the number of added chests doesn't equal the set chest number
            GridV = random.randrange(g_rows)
            #The chest vertical position is random between the set number of grid rows
            GridH = random.randrange(g_column)
            #The chest horizontal position is random between the set number of grid columns
            if grid [GridV][GridH] == "⌂" :
            #The chest position is created if it is on an empty space
                grid [GridV][GridH] = "C"
            #The chests are represented as a 'C'
                add_chests = add_chests + 1
            #1 is added to the chest count so that the loop can continue
                newChestLocation = (GridV,GridH)
            #The current chest position is assigned to a variable which holds the new location
                chestLocation[newChestLocation] = 0
            #This will add the new chest location to the dictionary and is then set to 0

        
        while True:
        #Before each turn, the program will check for...
            if chests == 0:
        #If all the chests are gone
                print("You have lost the game")
        #It will tell the player that they have lost
                print("Total Moves: ",moves)
        #Displays the number of moves made that game
                break
        #Break returns back to the main menu
            elif g_coins >= 100 :
        #Or if the number of coins is more than or equal to 100
                print("You have won the game!")
        #It will tell the player that they have won
                print("Total Moves: ",moves)
        #Displays the total moves made that game
                break
        #Then returns back to the main menu

        
            for listCount in grid,:
            #Will loop for every list in the grid
                for itemCount in listCount:
            #And then will loop for every item within the lists
                    if debug == True :
            #If debug mode is set to true, it will print the grid with the positions
            #of the bandits and chests shown
                        print(itemCount)
                    else:
            #If debug is not true, it will print the grid without the positions displayed
                        itemCount = ' '.join(itemCount)
            #This converts the lists into strings for the replace function to be used
                        print(itemCount.replace("B", "⌂").replace("C", "⌂"))
            #The bandit and chest symbols will be replaced with a blank space symbol

            move_true = False
            #A variable is set to be used in the while loop
            grid [pInGame_v][pInGame_h] = "⌂"
            #The players position is set to blank so it doesn't stay the same
            while move_true == False :
            #While the variable is false, the program will ask for an input
                
                pHorizontalMove = int(input("How many moves horizontally will you like to move? + right/- left"))
            #Asks the user for a horizontal move input
                pVerticalMove = int(input("How many moves vertically will you like to move? + down/- up"))
            #Asks the user for a vertical move input
                if pInGame_h + pHorizontalMove >= 0 and pInGame_h + pHorizontalMove <= g_column - 1:
                    if pInGame_v + pVerticalMove >= 0 and pInGame_v + pVerticalMove <= g_rows - 1:
            #Checking if the move is valid to see if it fits into the grid

                        hSave = pInGame_h
            #A copy of the players position is saved for layer use
                        vSave = pInGame_v
                        print("Valid Move")
            #Prints a message telling the user that their move is valid
                        moves = moves + 1
            #Adds 1 to the move counter
                        move_true = True
            #Sets the variable to true so the while loop won't continue to loop
                        pInGame_v = pInGame_v + pVerticalMove  
                        pInGame_h = pInGame_h + pHorizontalMove
            #Adds the users inputted move to the existing position
                        
                        if grid[pInGame_v][pInGame_h] == "C" :
                #If the user lands on a chest it will perform this code
                            g_coins += 10
                #10 is added to the total number of coins
                            if chestLocation[(pInGame_v,pInGame_h)] < 2 :
                #If the number of times the player has landed on the chest is less than 2...
                                chestLocation[(pInGame_v,pInGame_h)] += 1
                #The chest item for that coordinate will increase by 1
                                grid[vSave][hSave] = "⌂"
                #The space becomes blank for the player to not see
                            else:
                                grid[pInGame_v][pInGame_h] = "B"
                #If the player has landed ona chest 3 time it turns to a bandit
                                grid[vSave][hSave] = "⌂"
                #The space turn to a blank space
                                chests += -1
                                bandits += 1
                #The number of chests decreases and the bandits increase
                            pInGame_v = pStart_v
                            pInGame_h = pStart_h
                #The player's position is reset to the starting position

                            grid[pInGame_v][pInGame_h] = "☺"
                #The player symbol is displayed to the user

                        elif grid[pInGame_v][pInGame_h] == "B" :
                #If the player lands on a bandit...

                            grid[vSave][hSave] = "⌂"
                            print("You have landed on a bandit.")
                #The program indicates to the user that they have landed on one
                            g_coins = 0
                #The number of coins is resets to 0
                            pInGame_v = pStart_v
                            pInGame_h = pStart_h
                #Player returns back to the starting position
                            grid[pInGame_v][pInGame_h] = "☺"
                #The player symbol is displayed
                        else:
                #If the player lands on a blank space...
                            grid[vSave][hSave] = "⌂"
                            grid[pInGame_v][pInGame_h] = "☺"
                #The player just stays in the same position

                        print("Coins:" ,g_coins)
                        print("Bandits:" ,bandits)
                        print("Chests:" ,chests)
                #The number of total coins, bandits and chests are printed
                       

                         
                        
                else:
                    print("Invalid Move")
            
                

                                                   
              

    
    elif selection == "2" :
        #If the user chooses a 2, the program will exit
        exit()

    

else:
    #The else statement will run if a 1 or 2 is not entered
    print("Please enter a valid input")
    #The user will be displayed with an error message


