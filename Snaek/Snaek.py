# A way to start / pause game       (DONE)

# Start player at origin position   (DONE)
# Set a direction                   (DONE)
# Draw a square in that direction   (DONE)
# Check for input                   (DONE)
# Change direction if nessesary     (DONE)

# Spawn 'apple'                     (DONE)
# Check if player runs over apple   (DONE)
# Make player longer                (DONE)
# Apple limit                       (DONE)

# If player runs over square, die   (DONE)
# If player runs into wall, die     (DONE)

# ---- Imports ---- #
from cProfile import label
from tkinter import font
import pygame, pygame_menu, time, random
from pygame.locals import *

# ---- Variables ---- #
black = (0, 0, 0)                                   # Calling colour variables up here for easier access
white = (255, 255, 255)
red = (255, 0, 0)
grey = (69, 69, 69)

snakelen = 3                                        # All the global variables (Types (In order): Int, List, Tuple, Bool, String)                                        
_time = 0                                           # If the variable has a value, that's the default value, either to avoid errors or for mandatory initial values
apples = 0
applescollected = 0
appcoords = []
dirlist = ["UP", "UP"]                              
poslist = []
coordlist = []
alive = False

# ---- Window Config ---- #
window = (500, 500)
(x, y) = window

# ---- Initializing ---- #
pygame.init()                                       # Initializes pygame and pygame.display
pygame.display.init()

pygame.display.set_caption("Snaek Gaem")            # Setting window name
screen = pygame.display.set_mode(window)            # Setting window size
surface = pygame.Surface((500, 500))

# ---- Writing down the score ---- #
def scorewriting():
    global highscore

    try:                                            # If the file doesn't exist, create it and write '0' to it for default new score
        score_file = open("score.txt", "x")         # Creates new text file named score
        score_file = open("score.txt", "w")         # Prepares file for writing
        score_file.write('0')
    except:
        pass

    score_file = open("score.txt", "r")             # Prepares the file for reading
    highscore = score_file.read()                   # Reads the file

    if int(highscore) < applescollected:            # If the already written highscore is less than the score after the player dies,
        score_file = open("score.txt", "w")         # overwrite the previous score with the current one
        score_file.write(str(applescollected))
        score_file = open("score.txt", "r")
        highscore = score_file.read()

    score_file.close()                              # Closes file as I don't need it anymore and for security(?) reasons (not like I need it but good practice)

# ---- Changing the Difficulty ---- #
def change_speed(selected_value, speed, **kwargs): # Calls function off of the difficulty menu (Line 271)
    global speed_tuple
    speed_tuple, index = selected_value

def change_apples(selected_value, apples, **kwargs):
    global apple_tuple
    apple_tuple, index = selected_value

# ---- Apple Coordinates ---- #
def AppleSpawn():                                  

    global appcoords                                # Makes sure the variables can be accessed by other functions
    global apples
    global applemaximum

    if apples < applemaximum:                       # Enables me to set a limit of the number of apples on screen at once 
        xappgrid = random.randint(0, 19)            # Generates two random numbers for the grid squares (Tuples on Line 83-84 as reference)
        yappgrid = random.randint(0, 19)

        xappcoord = xappgrid * 25                   # Takes the grid coordinates and translates them into pixel coordinates for drawing
        yappcoord = yappgrid * 25
        xycoords = (xappcoord, yappcoord)           # Packs those into a tuple for use in the rect part of the draw method
        appcoords.append(xycoords)                  # Appends the packed coordinates into a list that's later used on Line 196

        pygame.draw.rect(screen, red, (xappcoord, yappcoord, 25, 25)) # Draws a red square on the randomly selected coordinates
        apples += 1                                                   # Integer counting number of apples on screen is added to

    else:
        pass

# ---- Main Function ---- #
def main():                                         # Handles all of the gameplay
    # ---- Setup ---- #
    screen.fill(black)                              # Fills the screen black for the game space
                                                     
    global alive                                    # Global variables 
    global dirlist                                  
    global poslist                                  
    global coordlist
    global snakelen
    global _time
    global appcoords
    global apples
    global applescollected
    global speed_tuple
    global apple_tuple
    global applemaximum

    Xtuple = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T")
    Ytuple = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")

    # The range of the board is 20x20 grid, which means the coords are in range A-T and 1-20
    # The two lists of tuples used to get the coordinates on a square grid
    
    # ---- Resetting Variables on Game Start ---- #
    xx = 12                                             # Index in Xtuple (XAxis on Grid)
    yy = 12                                             # Index in Ytuple (YAxis on Grid)

    poslist = []                                        # List of Grid Coordinates
    coordlist = []                                      # List of Pixel Coordinates for the grid spaces

    direction = "UP"                                    # Current Direction
    prevdir = "UP"                                      # Previous Direction
    dirlist = ["UP", "UP"]                              # List for the current diretion and previous direction

    alive = True                                        # Bool for determining wether the snake is alive or not
    snakelen = 3                                        # Default Length of the Snake  
    
    _time = 0                                           # Time passed
    delaytime = 3                                       # Integer for the Delay between the Spawning of Apples
    apples = 0                                          # Integer for Number of Apples Currently On-Screen
    applescollected = 0                                 # Integer for Number of Apples Collected
    appcoords = []                                      # List of Apple Coordinates

    try:
        delay = speed_tuple[1]                          # Integer for how long between checks for movement are made
    except:
        delay = 0.1                                     # Default Value
        # Lower = Faster, More responsive  
        # Higher = Slower, Less responsive
    try:
        applemaximum = apple_tuple[1]                   # Integer for Maximum Number of Apples Allowed On-Screen
    except:
        applemaximum = 3

    # ---- Main Loop ---- #
    running = True                                      # Game loop started
    while running:

        for event in pygame.event.get():                # Exits the game loop if game is exited
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()                         # Updates the screen with the visuals

        # ---- Time ---- #
        _time += 0.1                                    # Every time it loops, adds 0.1 to the time
        if _time > delaytime:                           # Checks if the current time is greater than the wished delay time
            AppleSpawn()                                # Calls AppleSpawn function (Line 49)
            _time = 0                                   # Resets time to 0 to repeat
        else:                                           # If the time is less than the delay time, it adds 0.1 to the time
            _time += 0.1                                # Wait this is actually 0.2 seconds per loop?? (look into later)

        # ---- User Input ---- #
        key = pygame.key.get_pressed()                  # Variable for easier calling

        if key[pygame.K_UP] or key[pygame.K_w] and dirlist[0] != "UP":          # Checks which key was pressed and disallows backwards keypresses (No up -> down)
            dirlist.insert(0, "UP")                                             # Inserts whatever direction was pressed into a list
            dirlist.pop(2)                                                      # Deletes the 3rd direction in the direction list (anything after the first two is unnessesary

        elif key[pygame.K_DOWN] or key[pygame.K_s] and dirlist[0] != "DOWN":
            dirlist.insert(0, "DOWN")
            dirlist.pop(2)

        elif key[pygame.K_LEFT] or key[pygame.K_a] and dirlist[0] != "LEFT":
            dirlist.insert(0, "LEFT")
            dirlist.pop(2)

        elif key[pygame.K_RIGHT] or key[pygame.K_d] and dirlist[0] != "RIGHT":
            dirlist.insert(0, "RIGHT")
            dirlist.pop(2)

        direction = dirlist[0]                          # Direction is the current moving direction                    
        prevdir = dirlist[1]                            # Prevdir is the last direction you were moving in

        # ---- Grid Movement ---- #
        if direction == "UP":                           # Constantly moving the snake on the coordinates logic (delay so it's managable and more like snake)
            if prevdir == "DOWN":                       # If up and if prevdir doesnt equal down go up
                yy += 1
            else:
                yy -= 1
                
        elif direction == "DOWN":                   
            if prevdir == "UP":                         # If the pressed direction is down and the previous direction is up, keep going up
                yy -=1                              
            else:
                yy += 1                             

        elif direction == "LEFT":                  
            if prevdir == "RIGHT":
                xx += 1                                 # Right (stops player from going back on themselves)
            else:
                xx -= 1                                 # Left (direction they will go if not going backwards)

        elif direction == "RIGHT":                
            if prevdir == "LEFT":
                xx -= 1                             
            else:
                xx += 1                             

        time.sleep(delay)

        # ---- Position Storing ---- #
        xcoord = (xx * 25)                                          # Calculates the position on the screen in pixels based off the grid potition
        ycoord = (yy * 25)
        coords = (xcoord, ycoord)                                   # Packs them into a tuple for inserting into a pixel coordinate list

        coordlist.insert(0, coords)                                 # Inserts the pixel coordinates into a list (coordlist)
        try:                                                        # Temporary Try Except statement to prevent crashes
            poslist.insert(0, Xtuple[xx] + Ytuple[yy])              # Gets a list of all the positions of the snake squares
        except:
            alive = False

        sizetup = (25, 25)                                          # Tuple for rect argument completion
        try:
            head = coordlist[0]                                     # Grabs the tuple of coords from the first position in the coordinate list
            tail = coordlist[snakelen]                              # Grabs the tuple of coords from the last position in the coordinate list
            head = head + sizetup                                   # Completes the rect argument with the last two arguments in sizetup
            tail = tail + sizetup

            for x in poslist:                                       # For every square in the snake:
                xindex = poslist.index(x)                           # Takes the index of the current element in the position list
                if xindex > snakelen:                               # If the index is greater than the set length of the snake
                    pygame.draw.rect(screen, white, head)           # Draw the square in the designated position
                    poslist.pop(snakelen)                           # Delete the position list entry and coordinate list entry of the max set length of the snake 
                    coordlist.pop(snakelen)                         # (ex. max snake length = 2 so both lists have 3 entries in them)
                elif xindex <= snakelen:                            # If none of that shenanigains happens:
                    pygame.draw.rect(screen, white, head)           # Draw head position white and draw tail position black
                    pygame.draw.rect(screen, black, tail)           # rect(surface, colour, rect(dist from top, dist from left, pixels down, pixels left)) (I think)

            if poslist[0] in poslist[1:]:                           # Poslist is the coordinate position on the grid and coordlist is those positions translated
                alive = False                                       # into pixel coordinates
            if coordlist[0][0] < 0 or coordlist[0][1] < 0:
                alive = False

        except:                                                     
            pass
        
        # ---- Apple Spawning ---- #
        if coordlist[0] in appcoords:                               # If the snake head ends up in the same spot as an apple:
            apple = appcoords.index(coordlist[0])                   # Grabs the coordinates that matched the head and apple placement
            appcoords.pop(apple)                                    # Deletes those coordinates from the list of apples
            apples -= 1                                             # Decreases the apples integer by one so more apples can spawn (Line 57)
            snakelen += 1                                           # Increases the maximum set length of the snake by 1
            applescollected += 1

        if alive == False:
            scorewriting()
            menu()

        try:
            # Draws rectangle on "dead pixel" *ba dum shh*
            pygame.draw.rect(screen, grey, (coordlist[-1][0], coordlist[-1][1], 25, 25)) # For some reason M11 stays in list and also kills the player and i do not know why
        except:
            pass

# ---- Quit Button Function ---- #
def quitf():                                                        # When you press quit on the game menu, the game quits
    pygame.quit()

def contmenu():
    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    customtheme.background_color = black

    cmenu = pygame_menu.Menu('How to Play', x, y, theme = customtheme)

    cmenu.add.label('How to Play:', font_size=36, underline=True)
    cmenu.add.label('Use the W A S D KEYS  or ARROW KEYS to move.', font_size=16)
    cmenu.add.label('You cannot go backwards on yourself or run into yourself, you will die.', font_size=14)
    cmenu.add.label('You are consistently moving, so stay on your toes.', font_size=16)
    cmenu.add.label('Oh also avoid the grey square, it will kill you as well.', font_size=16)
    cmenu.add.label('Have fun!', font_size=20)

    cmenu.add.button('Back', menu, font_size=24)

    cmenu.mainloop(screen)


def settingsmenu():
    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    customtheme.background_color = black

    smenu = pygame_menu.Menu('Settings', x, y, theme = customtheme)

    smenu.add.label('Press Enter to Confirm', font_size=24)
    smenu.add.selector( title = "Speed: ", font_size=20,
                       items = [('Snake', 0.1), ('Hawk', 0.05), ('Snail', 0.25)],
                       onchange = change_speed,
                       onreturn = change_speed
                     )
    smenu.add.selector( title = "Apple Density: ", font_size=20,
                       items = [('Dinner', 3), ('Snack', 1), ('Buffet', 5)],
                       onchange = change_apples,
                       onreturn = change_apples
                     )

    smenu.add.button('Back', menu) 
    smenu.mainloop(screen)

# ---- Main Menu Function ---- #
def menu():
    global highscore

    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    customtheme.background_color = black

    menu = pygame_menu.Menu('Snaek', x, y, theme = customtheme)

    menu.add.label(f'Most Apples Collected: {highscore}')
    menu.add.button('Play', main, font_size=24)
    menu.add.button('How to Play', contmenu, font_size=24)
    menu.add.button('Settings', settingsmenu, font_size=24)
    menu.add.button('Quit', quitf, font_size=24)
    menu.mainloop(screen)

# Function calling
scorewriting()
menu()

pygame.quit()
