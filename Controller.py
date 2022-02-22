import pygame
from Room import Room

class Controller:
    def __init__(self, ROOM_LIST, PLAYER):
        self.player = PLAYER
        self.room_list = ROOM_LIST
        self.current_room = self.room_list[0]

    def checkForActions(self, keys_pressed):
        # Counter used for stepping animation
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_s] or keys_pressed[pygame.K_d]:
            self.player.moving = (self.player.moving + 1) % 30
        else:
            self.player.moving = 0

        # Running
        if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
            VELOCITY = 10
        else:
            VELOCITY = 5
        
        direction = []
        if keys_pressed[pygame.K_w]:
            direction.append("up")
        if keys_pressed[pygame.K_d]:
            direction.append("right")
        if keys_pressed[pygame.K_s]:
            direction.append("down")
        if keys_pressed[pygame.K_a]:
            direction.append("left")
        for key in direction:
            velocity = VELOCITY
            velocity = self.current_room.collisionDetected(self.player.getEdges(key, velocity))
            self.player.look(key)
            self.player.move(key, velocity)