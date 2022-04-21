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

black = (0, 0, 0)
white = (255, 255, 255)

snake = white # potential color swap feature implementation

dirlist = ["UP", "UP"]                            # assigning list and default value

window = (500, 500)
(x, y) = window

print(x)
print(y)

pygame.init()
pygame.display.init()

pygame.display.set_caption("Snaek Gaem")
screen = pygame.display.set_mode(window)


def main():
    print('Balls')
    screen.fill(black)

    global dirlist

    n = 25
    f = 25

    Xtuple = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T")
    Ytuple = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")

    print(Xtuple[12] + Ytuple[12]) # THIS WORKS!

    # The range of the board is 20x20 grid, which means the coords are in range A-T and 1-20

    # 25 pixel squares?
    # getting a feel for the data
    for s in range(20): # x axis
        pygame.draw.rect(screen, white, (0, n, y, 1))
        n += 25

    for m in range(20): # y axis
        pygame.draw.rect(screen, white, (f, 0, 1, x))
        f += 25

    xx = 12
    yy = 12

    direction = "UP"                                    # Default Direction
    position = Xtuple[xx] + Ytuple[yy]                  # Outputs coord on grid (ex. M12)

    testl = []
    testl.append("bitches")
    testl.append("and bros")
    testl.append("and non binary hoes")

    print(testl)

    testl.insert(0, "women")
    testl.pop(2)

    print(testl)

    running = True                                      # Game loop started
    while running:

        for event in pygame.event.get():                # Exits the game loop if game is exited
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()                         # Updates the screen with the visuals

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
        print(dirlist)

        delay = 0.2

        if direction == "UP":                       # Constantly moving the snake on the coordinates logic (delay so it's managable and more like snake)
            if prevdir == "DOWN":                   # If up and if prevdir doesnt equal down go up
                yy += 1
                time.sleep(delay)
            else:
                yy -= 1
                time.sleep(delay)
            #try:
                #print(Xtuple[xx] + Ytuple[yy])     # Debug and also OOB ( indicator
           # except:
               # print("death")
               # pass
                
        elif direction == "DOWN":                   # If down and prevdir doesnt equal up go down
            if prevdir == "UP":
                yy -=1
                time.sleep(delay)
            else:
                yy += 1
                time.sleep(delay)

        elif direction == "LEFT":                   # If left and prevdir doesnt equal right go left
            if prevdir == "RIGHT":
                xx += 1
                time.sleep(delay)
            else:
                xx -= 1
                time.sleep(delay)

        elif direction == "RIGHT":                  # If right and prevdir doesnt equal left go right
            if prevdir == "LEFT":
                xx -= 1
                time.sleep(delay)
            else:
                xx += 1
                time.sleep(delay)

        '''
        try:
            if dirlist[0] != dirlist[1]:
                R = random.randrange(0, 255)
                G = random.randrange(0, 255)
                B = random.randrange(0, 255)

                colour = (R, G, B)
        except:
            colour = white
        '''

# hear me out, variable * 25 + 1 (for calculating square coords) (ex. xx = 7 so 7 * 25 is 175 + 1 = 176) 
# (then just add 25 to coords to make square)
        xcoord = (xx * 25 + 1)
        ycoord = (yy * 25 + 1)

        coords = (xcoord, ycoord)

        pygame.draw.rect(screen, white, (xcoord, ycoord, 25, 25))

        # make some form of list that tracks (Xtuple[xx] + Ytuple[yy}) (ex. M12, M13, L13, etc.)
        # storing the values that the snaek moved essentially

        

def menu():

    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    customtheme.background_color = black

    menu = pygame_menu.Menu('Python', x, y, theme = customtheme)

    menu.add.button('Play', main)
    menu.mainloop(screen)

# Function calling
    
menu()

pygame.quit()
