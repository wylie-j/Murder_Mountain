from email.mime import image
import pygame
import os

# This function creates a list of strings with the names of all the images for a character
# The order is back, back stepping, right, right stepping, front, front stepping, left, left stepping
def imageFileLoader(entity_name):
    if os.path.exists('Assets/' + entity_name + 'Front.png'):
        images = [entity_name + 'Back', entity_name + 'Right', entity_name + 'Front', entity_name + 'Left']
        i = 0
        while i < len(images):
            images.insert(i + 1, images[i] + "Stepping.png")
            images[i] = images[i] + ".png"
            i += 2
    else:
        images = [entity_name + '.png']
    return images

# This function creates a list of images with a specified height & width given a list of image file names
def imageMaker(IMAGE_LIST, WIDTH, HEIGHT):
    image_list = []
    for IMAGE in IMAGE_LIST:
        TEMP_IMAGE = pygame.image.load(os.path.join('Assets', IMAGE))
        image_list.append(pygame.transform.scale(TEMP_IMAGE, (WIDTH, HEIGHT)))
    return image_list

class Entity:
    def __init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME):
        self.width = WIDTH
        self.height = HEIGHT
        IMAGE_LIST = imageFileLoader(NAME)
        self.images = imageMaker(IMAGE_LIST, WIDTH, HEIGHT)
        self.rect = pygame.Rect(X_COORD, Y_COORD, WIDTH, HEIGHT)
        self.current_image = 0
        self.facing = "down"

    # Top, Right, Down, Left (like a clock)
    def getEdges(self, direction, velocity):
        return (self.rect.y, self.rect.x + self.width, self.rect.y + self.height, self.rect.x, direction, velocity)

    def getCoords(self):
        return (self.rect.x, self.rect.y)

    def move(self, direction, velocity):
        if direction == "up" or direction == "down":
            self.rect.y += velocity
        if direction == "right" or direction == "left":
            self.rect.x += velocity

    def look(self, direction):
        if direction == "up" or direction == "right" or direction == "down" or direction == "left":
            self.facing = direction
        else:
            self.facing = "down"
    
    def interact(self):
        print("you are interacting with an entity")
