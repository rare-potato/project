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
"""File Requirements
class WumpusWorld: contains a map, records player movement & current game state
Data:
self.worldmap
self.WumpusAlive
self.playerAlive
self.playerHasGold
self.playerHasArrow
self.playerMoves
self.playerRow
self.playerCol
Methods:
__init__(self)
# most of these use current player location
stepEast(self)
stepWest(self)
stepSouth(self)
stepNorth(self)
grab(self, r, c)
grabGold(self) # checks current r, c, calls grab(self, r, c)
fire(self, direction)
canClimb(self)
feelBreeze(self)
smellStench(self)
seeGlint(self)
hasWumpus(self)
hasPit(self)"""

import Map

class WumpusWorld(object):
    #Initializes the variables for the Class
    def __init__(self):
        self.worldmap = Map.Map()
        self.WumpusAlive = True
        self.playerAlive = True
        self.playerHasGold = False
        self.playerHasArrow = True
        self.playerMoves = 0
        self.playerRow = 0
        self.playerCol = 0

    def stepEast(self):
        #Checks to see if the player can move to the east
        try:
            east = self.playerCol + 1
            self.worldmap.onGrid(self.playerRow, east)
            self.worldmap.offGrid(self.playerRow, east)
            self.playerCol = east
            self.playerMoves += 1
        except(Map.OffMapError):
            print("You feel a bump as you walk into a wall")

    def stepWest(self):
        #Checks to see if the player can move to the west
        try:
            west = self.playerCol - 1
            self.worldmap.onGrid(self.playerRow, west)
            self.worldmap.offGrid(self.playerRow, west)
            self.playerCol = west
            self.playerMoves += 1
        except(Map.OffMapError):
            print("You feel a bump as you walk into a wall")

    def stepSouth(self):
        #Checks to see if the player can move to the south
        try:
            south = self.playerRow - 1
            self.worldmap.onGrid(south, self.playerCol)
            self.worldmap.offGrid(south, self.playerCol)
            self.playerRow = south
            self.playerMoves += 1
        except(Map.OffMapError):
            print("You feel a bump as you walk into a wall")

    def stepNorth(self):
        #Checks to see if the player can move to the south
        try:
            north = self.playerRow + 1
            self.worldmap.onGrid(north, self.playerCol)
            self.worldmap.offGrid(north, self.playerCol)
            self.playerRow = north
            self.playerMoves += 1
        except(Map.OffMapError):
            print("You feel a bump as you walk into a wall")

    def grab(self, r, c):
        #"Picks" up the gold and tells they player that they picked up the gold.
        self.playerHasGold = True
        self.worldmap.removeGlint(self.playerRow, self.playerCol)
        print("You picked up a pile of gold.")

    def grabGold(self):# checks current r, c, calls grab(self, r, c)
        #Checks if the player can pick up the gold based off of their position and then does if they can
        if self.worldmap.isGlinty(self.playerRow, self.playerCol):
            self.grab(self.playerRow, self.playerCol)
        else:
            print("You do not pick up anything.")

    def fire(self, direction):
        #Checks if the player still has an arrow and informs them if they do not.
        if self.playerHasArrow:
            if direction == "east" or direction == "e":
                #Calculates all positions to the east of the player where the arrow will go
                print("You fire an arrow east.")
                for col in range(self.playerCol, 5):
                    #Checks to see if the Wumpus is in any of the spaces to the east and informs them if they kill it
                    if self.worldmap.hasWumpus(self.playerRow, col):
                        self.WumpusAlive = False
                        print("You hear a horrible scream.")
                        break

            elif direction == "west" or direction == "w":
                #Calculates all positions to the west of the player where the arrow will go
                print("You fire an arrow west.")
                for col in range(0, self.playerCol):
                    #Checks to see if the Wumpus is in any of the spaces to the west and informs them if they kill it
                    if self.worldmap.hasWumpus(self.playerRow, col):
                        self.WumpusAlive = False
                        print("You hear a horrible scream.")
                        break

            elif direction == "south" or direction == "s":
                # Calculates all positions to the south of the player where the arrow will go
                print("You fire an arrow south.")
                for row in range(0, self.playerRow):
                    #Checks to see if the Wumpus is in any of the spaces to the south and informs them if they kill it
                    if self.worldmap.hasWumpus(row, self.playerCol):
                        self.WumpusAlive = False
                        print("You hear a horrible scream.")
                        break

            elif direction == "north" or direction == "n":
                #Calculates all positions to the north of the player where the arrow will go
                print("You fire an arrow north")
                for row in range(self.playerRow, 5):
                    #Checks to see if the Wumpus is in any of the spaces to the south and informs them if they kill it
                    if self.worldmap.hasWumpus(row, self.playerCol):
                        self.WumpusAlive = False
                        print("You hear a horrible scream.")
                        break
            self.playerMoves += 1
            self.playerHasArrow = False
        else:
            self.playerMoves += 1
            print("You try to fire but are out of arrows.")
        #if the Wumpus is somewhere between the wall and the player in the specified direction the Wumpus will die

    def canClimb(self):
        #Checks if the player is at the origin and if they are informs the main program that they can exit the map
        if (self.playerRow, self.playerCol) == (0,0):
            return True
        else:
            return False

    def feelBreeze(self):
        #Checks to see if the current position is next to a pit
        if self.worldmap.isBreezy(self.playerRow, self.playerCol):
            return True
        else:
            return False

    def smellStench(self):
        #Checks to see if the current position is next to the Wumpus
        if self.worldmap.isSmelly(self.playerRow, self.playerCol):
            return True
        else:
            return False

    def seeGlint(self):
        #Checks to see if the current position has the Gold
        if self.worldmap.isGlinty(self.playerRow, self.playerCol):
            return True
        else:
            return False

    def hasWumpus(self):
        #Checks if the Wumpus is located at the player position and whether or not it is dead, and kills they player
        # if the Wumpus is alive. It also clears the stench if the Wumpus is dead.
        if self.worldmap.hasWumpus(self.playerRow, self.playerCol):
            if self.WumpusAlive:
                self.playerAlive = False
            else:
                self.playerAlive = True
            return True
        else:
            return False

    def hasPit(self):
        #Checks to see if the player falls into a pit
        if self.worldmap.hasPit(self.playerRow, self.playerCol):
            self.playerAlive = False
            return True
        else:
            return False

    def playAgain(self):
        #Reinitializes all of the variables and resets the playing field
        self.worldmap.reset()
        self.WumpusAlive = True
        self.playerAlive = True
        self.playerHasGold = False
        self.playerHasArrow = True
        self.playerMoves = 0
        self.playerRow = 0
        self.playerCol = 0