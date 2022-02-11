import pygame
import os
class Entity:
    def __init__(self, IMAGE_LOCATION, WIDTH, HEIGHT, X_COORD, Y_COORD):
        self.image = []
        self.x_coord = X_COORD
        self.y_coord = Y_COORD
        self.width = WIDTH
        self.height = HEIGHT
        for IMAGE in IMAGE_LOCATION:
            TEMP_IMAGE = pygame.image.load(os.path.join('Assets', IMAGE))
            self.image.append(pygame.transform.scale(TEMP_IMAGE, (WIDTH, HEIGHT)))
        self.rect = pygame.Rect(self.x_coord, self.y_coord, WIDTH, HEIGHT)
