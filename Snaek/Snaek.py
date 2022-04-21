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
import pygame, sys, os, pygame_menu, time
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)

snake = white #?

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

    direction = "UP"
    position = Xtuple[xx] + Ytuple[yy]

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] or key[pygame.K_w]:
            direction = "UP"

        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            direction = "DOWN"

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            direction = "LEFT"

        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            direction = "RIGHT"

        delay = 0.2

        if direction == "UP":
            yy -= 1
            try:
                print(Xtuple[xx] + Ytuple[yy])
            except:
                print("death")
                pass
            time.sleep(delay)

        elif direction == "DOWN":
            yy += 1
            try:
                print(Xtuple[xx] + Ytuple[yy])
            except:
                print("death")
                pass
            time.sleep(delay)

        elif direction == "LEFT":
            xx -= 1
            try:
                print(Xtuple[xx] + Ytuple[yy])
            except:
                print("death")
                pass
            time.sleep(delay)

        elif direction == "RIGHT":
            xx += 1
            try:
                print(Xtuple[xx] + Ytuple[yy])
            except:
                print("death")
                pass
            time.sleep(delay)

# hear me out, variable * 25 + 1 (for calculating square coords) (ex. xx = 7 so 7 * 25 is 175 + 1 = 176) (then just add 25 to coords to make square)
        xcoord = (xx * 25 + 1)
        ycoord = (yy * 25 + 1)

        coords = (xcoord, ycoord)

        pygame.draw.rect(screen, white, (xcoord, ycoord, 25, 25))

        

def menu():

    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    customtheme.background_color = black

    menu = pygame_menu.Menu('Python', x, y, theme = customtheme)

    menu.add.button('Play', main)
    menu.mainloop(screen)

    
menu()

pygame.quit()
