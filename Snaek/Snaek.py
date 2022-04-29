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

# If player runs over square, die   (Not implemented)
# If player runs into wall, die     (Partially done)

# ---- Imports ---- #
import pygame, sys, os, pygame_menu, time, random
from pygame.locals import *
from pygame_menu.widgets.core.widget import Widget
from pygame_menu._types import EventVectorType

# ---- Variables ---- #
black = (0, 0, 0)                                   # Calling colour variables up here for easier access
white = (255, 255, 255)
red = (255, 0, 0)
grey = (69, 69, 69)

snakelen = 3                                        # All the global variables (Types (In order): Int, List, Tuple)                                        
_time = 0                                           # If the variable has a value, that's the default value, either to avoid errors or for mandatory initial values
apples = 0
appcoords = []
colpair = ["", ""]
dirlist = ["UP", "UP"]                              
poslist = []
coordlist = []
c1 = (255, 255, 255)
c2 = (0, 0, 0)

drawsquare1 = False

# ---- Window Config ---- #
window = (500, 500)
(x, y) = window

# ---- Initializing ---- #
pygame.init()                                       # Initializes pygame and pygame.display
pygame.display.init()

pygame.display.set_caption("Snaek Gaem")            # Setting window name
screen = pygame.display.set_mode(window)            # Setting window size

# ---- Apple Coordinates ---- #
def AppleSpawn():

    global appcoords                                # Makes sure the variables can be accessed by other functions
    global apples

    if apples < 5:                                  # Enables me to set a limit of the number of apples on screen at once 
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

    global dirlist                                  # Global variables
    global poslist                                  # There is a lot of them as this is the main game loop
    global coordlist
    global snakelen
    global _time
    global appcoords
    global apples
    global colpair
    global drawsquare1

    Xtuple = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T")
    Ytuple = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")

    # The range of the board is 20x20 grid, which means the coords are in range A-T and 1-20
    # The two lists of tuples used to get the coordinates on a square grid
    
    xx = 12                                             # Index in Xtuple
    yy = 12                                             # Index in Ytuple

    direction = "UP"                                    # Default Direction
    position = Xtuple[xx] + Ytuple[yy]                  # Outputs coord on grid (ex. M12)

    # ---- Main Loop ---- #
    running = True                                      # Game loop started
    while running:

        for event in pygame.event.get():                # Exits the game loop if game is exited
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()                         # Updates the screen with the visuals

        # ---- Time ---- #
        _time += 0.1                                    # Every time it loops, adds 0.1 to the time
        delaytime = 3                                   # The amount of seconds wished to delay the apple spawn
        if _time > delaytime:                           # Checks if the current time is greater than the wished delay time
            AppleSpawn()                                # Calls AppleSpawn function (Line 49)
            _time = 0                                   # Resets time to 0 to repeat
        else:                                           # If the time is less than the delay time, it adds 0.1 to the time
            _time += 0.1                                # Wait this is actually 0.2 seconds per loop?? (look into later)

        # ---- User Input ---- #
        key = pygame.key.get_pressed()                                          # Variable for easier calling

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
        delay = 0.1                                     # How long between checks for movement are made 
                                                        # Lower = Faster, More responsive  
                                                        # Higher = Slower, Less responsive
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

        coordlist.insert(0, coords)                                 # Inserts the pixel coordinates into a list
        try:                                                        # Temporary Try Except statement to prevent crashes
            poslist.insert(0, Xtuple[xx] + Ytuple[yy])              # Gets a list of all the positions of the snake squares
        except:
            print("death")
            menu()                                                  # Placeholder game over for now (need to make game over screen)

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
        except:                                                     
            print('Not lengthy enough')                             # Fallback for first three ticks
        
        # ---- Apple Spawning ---- #
        if coordlist[0] in appcoords:                               # If the snake head ends up in the same spot as an apple:
            print('Apple gained!')                                  # Maybe play a sound once I implement them
            apple = appcoords.index(coordlist[0])                   # Grabs the coordinates that matched the head and apple placement
            appcoords.pop(apple)                                    # Deletes those coordinates from the list of apples
            apples -= 1                                             # Decreases the apples integer by one so more apples can spawn (Line 57)
            snakelen += 1                                           # Increases the maximum set length of the snake by 1




# ---- Quit Button Function ---- #
def quitf():                                                        # When you press quit on the game menu, the game quits
    pygame.quit()

# ---- Colour Selection Menu Function ---- #
def colourmenu():                                                   # Colour menu function (supposed to be sub menu of main menu) (research that)

    #---- Input Function ---- #
    def color1(c):                                                  # Takes the value from the input text and assigns it to c1
        global colpair 
        global drawsquare1

        if len(c) <= 7:                                             # Checks for hex value in text input
            # Type is hex value
            if '#' in c:
                i = pygame.Color(c)                                 # Converts hex value to RGBA
                i = i[:3]                                           # Removes opacity value
                colpair[0] = i
                print('hex')
            elif '#' not in c:                                      # Same functionality just adds a hashtag so that the conversion works
                # Type is hex value without hash
                i = c
                i = '#' + i
                try:                                                
                    i = pygame.Color(i)
                    i = i[:3]
                    colpair[0] = i
                    print('hex without hash')
                except:                                             
                    # Fallback for invalid colour / input
                    print('Invalid Colour')

        elif ',' in c:                                              # Checks for brackets in RGB
           # Type is RGB value
           if '(' and ')' in c:
                # Type is RGB value with brackets
                i = c
                colpair[0] = i
                print('rgb w/ brackets')                            # If no # or () then assume RGB
           elif '(' or ')' not in c:                                # Currently the difference doesn't do anything as I havent implemented the draw feature yet
               # Type is RGB value without brackets
               i = c
               colpair[0] = i
               print('rgb w/o brackets')
        else:
            # Fallback if neither Hex nor RGB
            print('Not valid input')                                # For copy paste functionality use pywin32 and win32clipboard
        print(colpair)

        print("funcfin")
        drawsquare1 = True

    # ---- Second Input Function (copy paste later) ---- #                             # Duplicate function for second text input

    # ---- Menu setup ---- #
    global snakecolour
    global c1
    # global c2
    global drawsquare1

    ccustomtheme = pygame_menu.themes.THEME_SOLARIZED.copy()                        # Copies the solarized theme and assigns it to a variable (cause I don't know how to do from scratch)
    ccustomtheme.background_color = black                                           # Sets the background of the theme variable to black

    cmenu = pygame_menu.Menu('Colour Select', x, y, theme = ccustomtheme)           
    widg = pygame_menu.widgets.core.widget.Widget

    cmenu.add.text_input('Colour 1: ', 
                            default = '', 
                            input_underline = '.', 
                            maxwidth_dynamically_update = True, 
                            copy_paste_enable = True, 
                            cursor_selection_enable = True,
                            onreturn = color1         
                            )   

    cmenu.add.text_input('Colour 2: ',
                            default = '', 
                            input_underline = '.', 
                            maxwidth_dynamically_update = True, 
                            copy_paste_enable = True, 
                            cursor_selection_enable = True,
                            # onreturn = color2
                            )

    cmenu.add.button('Back', menu)
    cmenu.mainloop(screen)
  
# ---- Main Menu Function ---- #
def menu():

    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    customtheme.background_color = black

    menu = pygame_menu.Menu('Snaek', x, y, theme = customtheme)

    menu.add.button('Play', main)
    menu.add.button('Colour Select', colourmenu)
    menu.add.button('Quit', quitf)
    menu.mainloop(screen)

# Function calling
    
menu()

pygame.quit()
