import pygame
from Person import Person
# from main import VIEWPORT_HEIGHT, VIEWPORT_WIDTH

class Player(Person):
    def __init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME):
        Person.__init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME)

