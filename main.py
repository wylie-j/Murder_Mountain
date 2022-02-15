# Naming Conventions:
# CamelCase for classes
# lower_case_with_underscores for variables
# ALL_CAPS for constant variables
# mixedCase for functions (camel case but the first letter is lowercase)

from pydoc import doc
import pygame
import os
from Entity import Entity
from Player import Player
from Room import Room

# TODO:
# Figure out how to import modules
# Determine if entities will be able to draw themselves

VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 1250, 720
WIN = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
pygame.display.set_caption("Murder Mountain Mystery")

WHITE = (255, 255 ,255)
FPS = 60
VELOCITY = 5


def imageCreater(file_name, image_width, image_height):
    temp_img = pygame.image.load(os.path.join('Assets', file_name))
    return pygame.transform.scale(temp_img, (image_width, image_height))

def createPlayer():
    return Player(100, 100, 300, 100, 'Gary')

PERSON_HEIGHT = 100
PERSON_WIDTH = 100

def drawFunction(room, character):
    # Every 15 frames the character will change their image to look like they're stepping
    WIN.blit(room.image, (0,0))
    if character.moving < 15:
        WIN.blit(character.images[character.current_image], (character.rect.x, character.rect.y))
    elif character.moving >= 15:
        WIN.blit(character.images[character.current_image +1], (character.rect.x, character.rect.y))

def personAction(keys_pressed, person):
    # Counter used for stepping animation
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_s] or keys_pressed[pygame.K_d]:
        person.moving = (person.moving + 1) % 30
    else:
        person.moving = 0

    # Running
    if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
        VELOCITY = 10
    else:
        VELOCITY = 5

    # This section is dependant on how we loaded the images
    # The order is front(0), front stepping(1), back(2), 
    # back stepping(3), left(4), left stepping(5), right(6), right stepping(7)
    if keys_pressed[pygame.K_w] and person.rect.y > 0:
        person.rect.y -= VELOCITY
        person.current_image = 2
    if keys_pressed[pygame.K_s] and person.rect.y < VIEWPORT_HEIGHT - PERSON_HEIGHT:
        person.rect.y += VELOCITY
        person.current_image = 0
    if keys_pressed[pygame.K_a] and person.rect.x > 0:
        person.rect.x -= VELOCITY
        person.current_image = 4
    if keys_pressed[pygame.K_d] and person.rect.x < VIEWPORT_WIDTH - PERSON_WIDTH:
        person.rect.x += VELOCITY
        person.current_image = 6

def main():
    room = Room(['ParkingLot.jpg'], VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
    character = createPlayer()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        personAction(keys_pressed, character)    
        WIN.fill(WHITE)
        drawFunction(room, character)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
