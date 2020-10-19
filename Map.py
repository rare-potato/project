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
class Map: manages the entire map, assigns values to cells, reports status of map cells

Data:
    self.grid

Methods:
    __init__(self)
    onGrid(self, r, c)
    offGrid(self, r, c)
    reset(self)
    isBreezy(self, r, c)
    isSmelly(self, r, c)
    isGlinty(self, r, c)
    hasWumpus(self, r, c)
    hasPit(self, r, c)
"""
""" Game facts:
    Pits == 5 && != 0,0
    Wumpus == 1 && != 0,0
    5 <= Breeze <= 12
    Gold == 1 && != 0,0
    Glint == Gold
    2 <= Stench <= 4
    Ladder == 0, 0
    25 total "squares"
"""
import random

#An Error used to catch if a player attempts to go off the map
class OffMapError(Exception):
    def __init__(self):
        Off_map = True
#Contains the values for each characteristic for the cells
class Cell(object):
    def __init__(self):
        self.hasWumpus = False
        self.hasGold = False
        self.hasPit = False
        self.hasBreeze = False
        self.hasStench = False
#Creates the play field and holds the information of each cell
class Map:
    def __init__(self):
        #Defines the Grid width
        self.width = 5
        self.height = 5

        self.grid = {}
        #creates the grid
        for row in range(self.height):
            for col in range(self.width):
                self.grid[(row, col)] = Cell()

        g_row = 0
        g_col = 0
        w_row = 0
        w_col = 0
        #generates the coordinates for the gold and the wumpus and then adds them to the grid.
        while g_row == 0 and g_col == 0:
            g_row = random.randint(0, 4)
            g_col = random.randint(0, 4)

        while w_row == 0 and w_col == 0:
            w_row = random.randint(0,4)
            w_col = random.randint(0,4)

        self.grid[(g_row, g_col)].hasGold = True
        self.grid[(w_row, w_col)].hasWumpus = True

        #Generates the coordinates for the 5 pits.
        pits_dict = {}
        for pit in range(5):
            p_row = 0
            p_col = 0

            while p_row == 0 and p_col == 0:
                p_row = random.randint(0,4)
                p_col = random.randint(0,4)
                if not(p_row == 0) or not(p_col == 0):
                    if not((p_row,p_col) in pits_dict.keys()):
                        pits_dict[(p_row,p_col)] = pit
                    else:
                        p_row = 0
                        p_col = 0

        #Takes the coordinates for the pits and adds them to the grid.
        for pit in pits_dict.keys():
            self.grid[pit].hasPit = True

        self.stench_dict = {}

        #Creates the coordinates for all possible points to have a stench
        s_up = (w_row + 1, w_col)
        s_down = (w_row - 1, w_col)
        s_east = (w_row, w_col + 1)
        s_west = (w_row, w_col - 1)
        #Check to see if the points are in the area of the grid and if they are add them to the dictionary
        if s_up in self.grid.keys():
            self.stench_dict[s_up] = 1
        if s_down in self.grid.keys():
            self.stench_dict[s_down] = 1
        if s_east in self.grid.keys():
            self.stench_dict[s_east] = 1
        if s_west in self.grid.keys():
            self.stench_dict[s_west] = 1
        #Add the points from the dictionary into the grid
        for stench in self.stench_dict.keys():
            self.grid[stench].hasStench = True

        breezy_dict ={}
        #Calculate all the possible locations for a breeze and check to see if they are on the graph
        #Also does not add the breeze characteristic if it overlaps with a pit
        for pit in pits_dict:
            x_row, y_col = pit

            b_up = (x_row + 1, y_col)
            b_down = (x_row - 1, y_col)
            b_east = (x_row, y_col + 1)
            b_west = (x_row, y_col - 1)

            if not(b_up in pits_dict.keys()):
                if b_up in self.grid.keys():
                    breezy_dict[b_up] = 1

            if not(b_down in pits_dict.keys()):
                if b_down in self.grid.keys():
                    breezy_dict[b_down] = 1

            if not(b_east in pits_dict.keys()):
                if b_east in self.grid.keys():
                    breezy_dict[b_east] = 1

            if not(b_west in pits_dict.keys()):
                if b_west in self.grid.keys():
                    breezy_dict[b_west] = 1


        #Add the hasBreeze attribute to all of the Cells that should have a Breeze
        for breeze in breezy_dict.keys():
            self.grid[breeze].hasBreeze = True

    # r == row, c == col
    def onGrid(self, r, c):
        #Checks to see if the coordinates are on the grid
        if (r,c) in self.grid.keys():
            return True

    def offGrid(self, r, c):
        #Checks to see if the coordinates are not on the grid
        if not((r,c) in self.grid.keys()):
            raise OffMapError

    def reset(self):
        #Resets the grid
        self.grid = {}
        # creates the grid
        for row in range(self.height):
            for col in range(self.width):
                self.grid[(row, col)] = Cell()

        g_row = 0
        g_col = 0
        w_row = 0
        w_col = 0
        # generates the coordinates for the gold and the wumpus and then adds them to the grid.
        while g_row == 0 and g_col == 0:
            g_row = random.randint(0, 4)
            g_col = random.randint(0, 4)

        while w_row == 0 and w_col == 0:
            w_row = random.randint(0, 4)
            w_col = random.randint(0, 4)

        self.grid[(g_row, g_col)].hasGold = True
        self.grid[(w_row, w_col)].hasWumpus = True

        # Generates the coordinates for the 5 pits.
        pits_dict = {}
        for pit in range(5):
            p_row = 0
            p_col = 0

            while p_row == 0 and p_col == 0:
                p_row = random.randint(0, 4)
                p_col = random.randint(0, 4)
                if not (p_row == 0) or not (p_col == 0):
                    if not ((p_row, p_col) in pits_dict.keys()):
                        pits_dict[(p_row, p_col)] = pit
                    else:
                        p_row = 0
                        p_col = 0

        # Takes the coordinates for the pits and adds them to the grid.
        for pit in pits_dict.keys():
            self.grid[pit].hasPit = True

        self.stench_dict = {}

        # Creates the coordinates for all possible points to have a stench
        s_up = (w_row + 1, w_col)
        s_down = (w_row - 1, w_col)
        s_east = (w_row, w_col + 1)
        s_west = (w_row, w_col - 1)
        # Check to see if the points are in the area of the grid and if they are add them to the dictionary
        if s_up in self.grid.keys():
            self.stench_dict[s_up] = 1
        if s_down in self.grid.keys():
            self.stench_dict[s_down] = 1
        if s_east in self.grid.keys():
            self.stench_dict[s_east] = 1
        if s_west in self.grid.keys():
            self.stench_dict[s_west] = 1
        # Add the points from the dictionary into the grid
        for stench in self.stench_dict.keys():
            self.grid[stench].hasStench = True

        breezy_dict = {}
        # Calculate all the possible locations for a breeze and check to see if they are on the graph
        # Also does not add the breeze characteristic if it overlaps with a pit
        for pit in pits_dict:
            x_row, y_col = pit

            b_up = (x_row + 1, y_col)
            b_down = (x_row - 1, y_col)
            b_east = (x_row, y_col + 1)
            b_west = (x_row, y_col - 1)

            if not (b_up in pits_dict.keys()):
                if b_up in self.grid.keys():
                    breezy_dict[b_up] = 1

            if not (b_down in pits_dict.keys()):
                if b_down in self.grid.keys():
                    breezy_dict[b_down] = 1

            if not (b_east in pits_dict.keys()):
                if b_east in self.grid.keys():
                    breezy_dict[b_east] = 1

            if not (b_west in pits_dict.keys()):
                if b_west in self.grid.keys():
                    breezy_dict[b_west] = 1

        # Add the hasBreeze attribute to all of the Cells that should have a Breeze
        for breeze in breezy_dict.keys():
            self.grid[breeze].hasBreeze = True

    def isBreezy(self, r, c):
        #Checks to see if the coordinates have a Breeze
        if self.grid[r,c].hasBreeze == True:
            return True
        else:
            return False

    def isSmelly(self, r, c):
        #Checks to see if the cell is Smelly
        if self.grid[r,c].hasStench == True:
            return True
        else:
            return False

    def isGlinty(self, r, c):
        #Checks to see if the coordinates have the gold
        if self.grid[r,c].hasGold == True:
            return True
        else:
            return False
    def removeGlint(self, r, c):
        self.grid[r,c].hasGold = False

    def hasWumpus(self, r, c):
        #Checks to see if the coordinates have the Wumpus
        if self.grid[r,c].hasWumpus == True:
            return True
        else:
            return False

    def hasPit(self, r, c):
        #Checks the coordinates to see if it has a pit
        if self.grid[r,c].hasPit == True:
            return True
        else:
            return False
