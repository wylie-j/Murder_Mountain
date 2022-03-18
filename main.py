# Naming Conventions:
# CamelCase for classes
# lower_case_with_underscores for variables
# ALL_CAPS for constant variables
# mixedCase for functions (camel case but the first letter is lowercase)

from pydoc import doc
import pygame
import os
import time
from Entity import Entity
from Person import Person
from NPC import NPC
from Player import Player
from Room import Room
from Controller import Controller

pygame.font.init()
# VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 1250, 720
VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 700, 500

WIN = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
pygame.display.set_caption("Murder Mountain Mystery")

WHITE = (255, 255 ,255)
green = (0, 255, 0)
blue = (0, 0, 128)
FPS = 60

DIALOGUE_FONT = pygame.font.SysFont('arial', 30)

# def imageCreater(file_name, image_width, image_height):
#     temp_img = pygame.image.load(os.path.join('Assets', file_name))
#     return pygame.transform.scale(temp_img, (image_width, image_height))

def createPlayer():
    return Player(100, 100, 200, 100, 'Gary')

def createRoom():
    room = Room(VIEWPORT_WIDTH, VIEWPORT_HEIGHT, "ParkingLot")
    room.NPC_list.append(NPC(100, 100, 600, 300, 'Gary'))
    return room

PERSON_HEIGHT = 100
PERSON_WIDTH = 100

def drawFunction(room, character):
    #draw the room
    WIN.blit(room.getImage(), (0,0))
    # draw all the people in the room
    for person in room.NPC_list:
        WIN.blit(person.getImage(), person.getCoords())
    # Every 15 frames the character will change their image to look like they're stepping
    WIN.blit(character.getImage(), character.getCoords())
    # font = pygame.font.Font('freesansbold.ttf', 32)
    # text = font.render('GeeksForGeeks', True, green, blue)
    # textRect = text.get_rect()

def main():
    room = createRoom() 
    character = createPlayer()
    controller = Controller([room], character)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
        # This is the list of all keys pressed since the last iteration of the while loop
        keys_pressed = pygame.key.get_pressed()
        talkingTo = controller.checkForActions(keys_pressed)
        if type(talkingTo) != type(None):
            # print("sdfl")talkingTo.dialogue.runDialogue()
            dialogueText = DIALOGUE_FONT.render("waffles", 1, WHITE)
            WIN.blit(dialogueText, (VIEWPORT_WIDTH//2, VIEWPORT_HEIGHT-50))
            pygame.display.update()
            time.sleep(.5)
        drawFunction(room, character)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
