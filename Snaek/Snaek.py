# A way to start / pause game

# Start player at origin position
# Set a direction
# Draw a square in that direction
# Check for input
# Change direction if nessesary

# Spawn 'apple'
# Check if player runs over apple
# Make player longer

# If player runs over square, die
# If player runs into wall, die
import pygame, sys, os, pygame_menu, time, random
from pygame.locals import *
from pygame_menu.widgets.core.widget import Widget
from pygame_menu._types import EventVectorType

# ---- Variables ---- #
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (69, 69, 69)

snakelen = 3
_time = 0
appcoords = []
apples = 0
c1 = (255, 255, 255)
c2 = (0, 0, 0)
colpair = []


dirlist = ["UP", "UP"]                            # assigning list and default value
poslist = []
coordlist = []

window = (500, 500)
(x, y) = window

# ---- Initializing ---- #
pygame.init()
pygame.display.init()

pygame.display.set_caption("Snaek Gaem")
screen = pygame.display.set_mode(window)

def AppleSpawn():

    global appcoords
    global apples

    if apples < 5:
        xappgrid = random.randint(0, 19)
        yappgrid = random.randint(0, 19)

        xappcoord = xappgrid * 25
        yappcoord = yappgrid * 25
        xycoords = (xappcoord, yappcoord)
        appcoords.append(xycoords)

        pygame.draw.rect(screen, red, (xappcoord, yappcoord, 25, 25))
        apples += 1
    else:
        pass

    


# ---- Main Function ---- #
def main():
    screen.fill(black)

    global dirlist
    global poslist
    global coordlist
    global snakelen
    global _time
    global appcoords
    global apples

    Xtuple = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T")
    Ytuple = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")

    # The range of the board is 20x20 grid, which means the coords are in range A-T and 1-20
    
    xx = 12
    yy = 12

    direction = "UP"                                    # Default Direction
    position = Xtuple[xx] + Ytuple[yy]                  # Outputs coord on grid (ex. M12)

# ---- Main gameloop ---- #
    running = True                                      # Game loop started
    while running:

        for event in pygame.event.get():                # Exits the game loop if game is exited
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()                         # Updates the screen with the visuals
        
        _time += 0.1
        delaytime = 3
        if _time > delaytime:
            AppleSpawn()
            _time = 0
        else: 
            _time += 0.1

# ---- Input ---- #
        key = pygame.key.get_pressed()                  # Variable for easier calling

        if key[pygame.K_UP] or key[pygame.K_w] and dirlist[0] != "UP":         # Stores the last direction pressed
            dirlist.insert(0, "UP")
            direction = "UP"
            dirlist.pop(2)

        elif key[pygame.K_DOWN] or key[pygame.K_s] and dirlist[0] != "DOWN":
            dirlist.insert(0, "DOWN")
            direction = "DOWN"
            dirlist.pop(2)

        elif key[pygame.K_LEFT] or key[pygame.K_a] and dirlist[0] != "LEFT":
            dirlist.insert(0, "LEFT")
            direction = "LEFT"
            dirlist.pop(2)

        elif key[pygame.K_RIGHT] or key[pygame.K_d] and dirlist[0] != "RIGHT":
            dirlist.insert(0, "RIGHT")
            direction = "RIGHT"
            dirlist.pop(2)

        direction = dirlist[0]
        prevdir = dirlist[1]

# ---- Movement On Grid ---- #
        delay = 0.1

        if direction == "UP":                       # Constantly moving the snake on the coordinates logic (delay so it's managable and more like snake)
            if prevdir == "DOWN":                   # If up and if prevdir doesnt equal down go up
                yy += 1
            else:
                yy -= 1
                
        elif direction == "DOWN":                   
            if prevdir == "UP":                     # If the pressed direction is down and the previous direction is up, keep going up
                yy -=1                              
            else:
                yy += 1                             

        elif direction == "LEFT":                  
            if prevdir == "RIGHT":
                xx += 1                             # Right (stops player from going back on themselves)
            else:
                xx -= 1                             # Left (direction they will go if not going backwards)

        elif direction == "RIGHT":                
            if prevdir == "LEFT":
                xx -= 1                             
            else:
                xx += 1                             

        time.sleep(delay)

# ---- Position Storing ---- #
        xcoord = (xx * 25)
        ycoord = (yy * 25)
        coords = (xcoord, ycoord)

        coordlist.insert(0, coords)
        poslist.insert(0, Xtuple[xx] + Ytuple[yy])

        sizetup = (25, 25)
        try:
            head = coordlist[0]                                     # Grabs the tuple of coords from the first position in the coordlist
            tail = coordlist[snakelen]
            head = head + sizetup                                   # Completes the rect argument
            tail = tail + sizetup

            for x in poslist:
                xindex = poslist.index(x)
                if xindex > snakelen:
                    pygame.draw.rect(screen, white, head)
                    poslist.pop(snakelen)
                    coordlist.pop(snakelen)
                elif xindex <= snakelen:
                    pygame.draw.rect(screen, white, head)
                    pygame.draw.rect(screen, black, tail)           # Screen, colour, rect
        except:
            print('ass')
        
        poslist = poslist[0:snakelen]

        if coordlist[0] in appcoords:
            print('Apple gained!')
            apple = appcoords.index(coordlist[0])
            appcoords.pop(apple)
            apples -= 1
            snakelen += 1

            # Takes most recently added apple as the coords, basically its impossible to grow cause there's only one set of coordinates
            # Make a list with all apple positions and then delete the ones that get grabbed
def quitf():
    pygame.quit()

def colourmenu():

    def color1(colour):
        global c1
        c1 = colour

    def color2(colour):
        global c2
        c2 = colour

    def colcheck(c):
        global colpair
        global i
        if '#' in c and len(c) <= 6:
            # Type is hex value
            i = pygame.Color(c)
            colpair.append(i)
        elif '(' and ')' in c:
            # Type is RGB value
            i = c.strip('()')
            colpair.append(i)
        else:
            i = c
            colpair.append(i)
            print(colpair)


    global snakecolour
    global c1
    global c2

    # need a way to input rgb / hex values

    ccustomtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    ccustomtheme.background_color = black

    cmenu = pygame_menu.Menu('Colour Select', x, y, theme = ccustomtheme)
    widg = pygame_menu.widgets.core.widget.Widget

    cmenu.add.text_input('Colour 1: ', 
                         default = '', 
                         input_underline = '.', 
                         maxwidth_dynamically_update = True, 
                         copy_paste_enable = True, 
                         cursor_selection_enable = True,
                         onchange = color1
                         
                         )   

    cmenu.add.text_input('Colour 2: ',
                         default = '', 
                         input_underline = '.', 
                         maxwidth_dynamically_update = True, 
                         copy_paste_enable = True, 
                         cursor_selection_enable = True,
                         onchange = color2
                         )
    
    cmenu.add.button('Back', menu)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        print('space!')
        try:
            colcheck(c1)
            colcheck(c2)
        except:
            print('bitches')


    cmenu.mainloop(screen)



  

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
