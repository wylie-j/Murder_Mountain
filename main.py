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

# TODO:
# Figure out how to import modules
# Determine if entities will be able to draw themselves

VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 900, 500
WIN = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
pygame.display.set_caption("Murder Mountain Mystery")

WHITE = (255, 255 ,255)
FPS = 60
VELOCITY = 5

def imageFileLoader(character_name):
    images = [character_name + 'Front', character_name + 'Back', character_name + 'Left', character_name + 'Right']
    i = 0
    while i < len(images):
        images.insert(i + 1, images[i] + "Stepping.png")
        images[i] = images[i] + ".png"
        i += 2
    return images

def imageCreater(file_name, image_width, image_height):
    temp_img = pygame.image.load(os.path.join('Assets', file_name))
    return pygame.transform.scale(temp_img, (image_width, image_height))

def createPlayer():
    return Player(imageFileLoader('Gary'), 100, 100, 300, 100, 'Lana')

PERSON_HEIGHT = 100
PERSON_WIDTH = 100

PLAYER = imageCreater('dude.png', PERSON_WIDTH, PERSON_HEIGHT)




def drawFunction(character):
    # WIN.blit(PLAYER, (player.x, player.y))
    WIN.blit(character.image[0], (character.rect.x, character.rect.y))

def personAction(keys_pressed, person):
    # if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_s] or keys_pressed[pygame.K_d]:
    #     person.moving = True
    # else:
    #     person.moving = False
    if keys_pressed[pygame.K_w] and person.y > 0:
        person.rect.y -= VELOCITY

    if keys_pressed[pygame.K_s] and person.y < VIEWPORT_HEIGHT - PERSON_HEIGHT:
        person.rect.y += VELOCITY
    if keys_pressed[pygame.K_a] and person.x > 0:
        person.rect.x -= VELOCITY
    if keys_pressed[pygame.K_d] and person.x < VIEWPORT_WIDTH - PERSON_WIDTH:
        person.rect.x += VELOCITY

def main():
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
        drawFunction(character)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
