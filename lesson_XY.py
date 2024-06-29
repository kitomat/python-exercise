
pygame.init()
import pygame
star =  pygame.Pygame()
star.filcolor("black")
star.right(75)
star.forward(100)
star.begin_fill()
for i in range(4):
    star.right(144)
    star.forward(100)
star.end_fill()
pygame.done()
