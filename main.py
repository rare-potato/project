########################################################################
## PROBLEM : Create a text based game that is based off of Hunt the Wumpus
##
## ALGORITHM :
##      1. Magic
##
## ERROR HANDLING:
##      Checks to see if the person has valid inputs
##	    Checks to see if the person attempts to go off of the map and stops them from doing so
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
# Main program: Handles all user interactions, gets input, checks it for validity, passes valid input to methods of
# WumpusWorld object, provides user feedback based on results, computes final score.


import Wumpus

def move(action):
    """Takes the player's input and performs the transformation"""
    global climb
    #If the person asks for help they will be displayed a list of possible commands
    if action == "help" or action == "h":
        print("""A list of possible commands (not case sensitive):
    Cardinal Directions (each command can be abbreviated by using the first letter):
        north: move one cell north
        south: move one cell south
        east: move one cell east
        west: move one cell west
    Other Commands (each command can be abbreviated by using the first letter):
        fire [direction]: fire an arrow in one of the four previously defined directions
            example: "fire north" is equivalent "f n"
        grab: attempt to pick up gold
        climb: if the player is at (0,0) this takes the player out of Wumpus World and ends the game
        help: show this help screen

    """)
    #If the person attempts to move east the program checks if they can move east, then check the Cell for it's contents
    if action == "east" or action == "e":
        game.stepEast()
        report_count = 0
        if game.seeGlint():
            print("You see a glint of something that looks like gold.")
            report_count += 1

        if game.feelBreeze():
            print("You feel a breeze.")
            report_count += 1

        if game.smellStench():
            print("You smell a stench.")
            report_count += 1

        if game.hasWumpus():
            report_count += 1
            if game.WumpusAlive:
                print("There is a live Wumpus here!")
                print("Your final score is 0.\n")
                return False
            else:
                print("There is a dead Wumpus here.")

        if game.hasPit():
            report_count += 1
            print("You have fallen into a pit.")
            print("Your final score is 0.\n")

        if report_count < 1:
            print("It is dark.")
    #If the person attempts to move west the program checks if they can move west, then check the Cell for it's contents
    if action == "west" or action == "w":
        game.stepWest()
        report_count = 0
        if game.seeGlint():
            print("You see a glint of something that looks like gold.")
            report_count += 1

        if game.feelBreeze():
            print("You feel a breeze.")
            report_count += 1

        if game.smellStench():
            print("You smell a stench.")
            report_count += 1

        if game.hasWumpus():
            report_count += 1
            if game.WumpusAlive:
                print("There is a live Wumpus here!")
                print("Your final score is 0.\n")
                return False
            else:
                print("There is a dead Wumpus here.")

        if game.hasPit():
            report_count += 1
            print("You have fallen into a pit.")
            print("Your final score is 0.\n")

        if report_count < 1:
            print("It is dark.")
    #If the person attempts to move south the program checks if they can move south, then check the Cell for it's contents
    if action == "south" or action == "s":
        game.stepSouth()
        report_count = 0
        if game.seeGlint():
            print("You see a glint of something that looks like gold.")
            report_count += 1

        if game.feelBreeze():
            print("You feel a breeze.")
            report_count += 1

        if game.smellStench():
            print("You smell a stench.")
            report_count += 1

        if game.hasWumpus():
            report_count += 1
            if game.WumpusAlive:
                print("There is a live Wumpus here!")
                print("Your final score is 0.\n")
                return False
            else:
                print("There is a dead Wumpus here.")

        if game.hasPit():
            report_count += 1
            print("You have fallen into a pit.")
            print("Your final score is 0.\n")

        if report_count < 1:
            print("It is dark.")
    #If the person attempts to move north the program checks if they can move north, then check the Cell for it's contents
    if action == "north" or action == "n":
        game.stepNorth()
        report_count = 0
        if game.seeGlint():
            print("You see a glint of something that looks like gold.")
            report_count += 1

        if game.feelBreeze():
            print("You feel a breeze.")
            report_count += 1

        if game.smellStench():
            print("You smell a stench.")
            report_count += 1

        if game.hasWumpus():
            report_count += 1
            if game.WumpusAlive:
                print("There is a live Wumpus here!")
                print("Your final score is 0.\n")
                return False
            else:
                print("There is a dead Wumpus here.")

        if game.hasPit():
            report_count += 1
            print("You have fallen into a pit.")
            print("Your final score is 0.\n")
        if report_count < 1:
            print("It is dark.")

    #If the person tries to grab the gold it checks to see if they can, and if they can it "picks" it up
    if action == "grab" or action == "g":
        game.grabGold()
    #Checks if the person can climb out, and if they can it will calculate and display their score.
    if action == "climb" or action == "c":
        if game.canClimb():
            score = 0
            if game.playerHasGold:
                score += 1000
                score -= game.playerMoves
                if not(game.playerHasArrow):
                    score -= 10
            else:
                score += 100
                score -= game.playerMoves
                if not(game.playerHasArrow):
                    score -= 10
            print("You climb out of Wumpus World.")
            print("Your final score is {}.".format(str(score)))
            climb = False
        else:
            report_count = 0
            if game.feelBreeze():
                print("You feel a breeze.")
                report_count += 1

            if game.smellStench():
                print("You smell a stench.")
                report_count += 1
            print("You cannot climb up from here.")
            if report_count < 1:
                print("It is dark.")
    #Changes the input into a list / tuple, and checks to see if it is too long or not, if it is it raises and index error
    action_split = action.split()
    if len(action_split) > 2:
        raise IndexError
    #Runs the fire command.
    if action_split[0] == "fire" or action_split[0] == "f":
        game.fire(action_split[1])
#Initialize global variables
playing = True
climb = True
game = Wumpus.WumpusWorld()
#Main loop for the game
while playing:
    #As long as the play is alive and you can climb out it will continue
    while game.playerAlive and climb:
        #Check if the origin has a stench or a breeze
        print("It is dark.")

        if game.feelBreeze():
            print("You feel a breeze.")

        if game.smellStench():
            print("You smell a stench.")

        #Gets the user input then puts it through the move function
        while game.playerAlive:
            action = input("")
            try:
                move(action.strip().lower())
            except(IndexError):
                print("Please enter a valid command.")

    play_check = True

    while play_check:
        #Continues asking if they would like to play again until they answer correctly.
        ask = input("Would you like to play again? ")
        if ask.strip().lower() == "yes" or ask.strip().lower() == "y":
            game.playAgain()
            playing = True
            climb = True
            play_check = False

        elif ask.strip().lower() == "no" or ask.strip().lower() == "n":
            playing = False
            play_check = False

        else:
            print("Please enter yes, no, y, or n.")
            play_check = True
