# Naming Conventions:
# CamelCase for classes
# lower_case_with_underscores for variables
# ALL_CAPS for constant variables
# mixedCase for functions (camel case but the first letter is lowercase)

from pydoc import doc
import pygame
import os
from Entity import Entity
from Person import Person
from NPC import NPC
from Player import Player
from Room import Room

VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 1250, 720
WIN = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
pygame.display.set_caption("Murder Mountain Mystery")

WHITE = (255, 255 ,255)
FPS = 60

# def imageCreater(file_name, image_width, image_height):
#     temp_img = pygame.image.load(os.path.join('Assets', file_name))
#     return pygame.transform.scale(temp_img, (image_width, image_height))

def createPlayer():
    return Player(100, 100, 300, 100, 'Gary')

def createRoom():
    room = Room(VIEWPORT_WIDTH, VIEWPORT_HEIGHT, "ParkingLot")
    room.person_list.append(NPC(100, 100, 600, 100, 'Gary'))
    return room

PERSON_HEIGHT = 100
PERSON_WIDTH = 100

def drawFunction(room, character):
    #draw the room
    WIN.blit(room.getImage(), (0,0))
    # draw all the people in the room
    for person in room.person_list:
        WIN.blit(person.images[0], (person.rect.x, person.rect.y))
    # Every 15 frames the character will change their image to look like they're stepping
    if character.moving < 15:
        WIN.blit(character.images[character.current_image], (character.rect.x, character.rect.y))
    elif character.moving >= 15:
        WIN.blit(character.images[character.current_image +1], (character.rect.x, character.rect.y))

def main():
    room = createRoom() 
    character = createPlayer()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
        # This is the list of all keys pressed since the last iteration of the while loop
        keys_pressed = pygame.key.get_pressed()
        character.move(keys_pressed, room)
        drawFunction(room, character)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
