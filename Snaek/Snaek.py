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
import pygame, sys, os, pygame_menu
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

   # unsure if there is a better way to do this
   snakemap = {
       "A1": {
           "occupied": False,
           "coordinates": (0, 0)                     # Taking top left of every square (squares are 25x25)
           },
       "A2": {
           "occupied": False,
           "coordinates": (26, 0)                     # Taking top left of every square (squares are 25x25)
           },
       "A3": {
           "occupied": False,
           "coordinates": (52, 0)                     # Taking top left of every square (squares are 25x25)
           },
       "A4": {
           "occupied": False,
           "coordinates": (78, 0)                     # Taking top left of every square (squares are 25x25)
           },
       "A5": {
           "occupied": False,
           "coordinates": (104, 0)                     # Taking top left of every square (squares are 25x25)
           },
       }

   # The range of the board is 20x20 grid, which means the coords are in range A-T and 1-20

   # 25 pixel squares?
   # getting a feel for the data
   for s in range(20): # x axis
        pygame.draw.rect(screen, white, (0, n, y, 1))
        n += 25

   for m in range(20): # y axis
        pygame.draw.rect(screen, white, (f, 0, 1, x))
        f += 25

   running = True
   while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

def menu():

    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    customtheme.background_color = black

    menu = pygame_menu.Menu('Python', x, y, theme = customtheme)

    menu.add.button('Play', main)
    menu.mainloop(screen)

    
menu()

pygame.quit()
