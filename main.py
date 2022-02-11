# Naming Conventions:
# CamelCase for classes
# lower_case_with_underscores for variables
# ALL_CAPS for constant variables
# mixedCase for functions (camel case but the first letter is lowercase)

import pygame
import os
from Entity import Entity

# TODO:
# Figure out how to import modules
# Determine if entities will be able to draw themselves

VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 900, 500
WIN = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
pygame.display.set_caption("Murder Mountain Mystery")

WHITE = (255, 255 ,255)
FPS = 60
VELOCITY = 5

PERSON_HEIGHT = 100
PERSON_WIDTH = 100
PLAYER_IMG = pygame.image.load(os.path.join('Assets', 'dude.png'))
PLAYER = pygame.transform.scale(PLAYER_IMG, (PERSON_WIDTH, PERSON_HEIGHT))


def drawWindow(player, character):
    WIN.fill(WHITE)
    WIN.blit(PLAYER, (player.x, player.y))
    WIN.blit(character.image[0], (character.x_coord, character.y_coord))
    pygame.display.update()

def playerAction(keys_pressed, player):
    if keys_pressed[pygame.K_w] and player.y > 0:
        player.y -= VELOCITY
    if keys_pressed[pygame.K_s] and player.y < VIEWPORT_HEIGHT - PERSON_HEIGHT:
        player.y += VELOCITY
    if keys_pressed[pygame.K_a] and player.x > 0:
        player.x -= VELOCITY
    if keys_pressed[pygame.K_d] and player.x < VIEWPORT_WIDTH - PERSON_WIDTH:
        player.x += VELOCITY

def main():
    player = pygame.Rect(800, 200, PERSON_WIDTH, PERSON_HEIGHT)
    idfk = []
    idfk.append("dude.png")
    character = Entity(idfk, 100, 100, 300, 100)
    # bob = Player.Player("Bitches")
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        playerAction(keys_pressed, player)
        drawWindow(player, character)

    pygame.quit()

if __name__ == "__main__":
    main()
