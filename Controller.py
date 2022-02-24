import imp
import pygame
from Room import Room
from CollisionDetector import CollisionDetector

class Controller:
    def __init__(self, ROOM_LIST, PLAYER):
        self.player = PLAYER
        self.room_list = ROOM_LIST
        self.current_room = self.room_list[0]
        self.collision_detector = CollisionDetector()

    def checkForActions(self, keys_pressed):
        # Running
        if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
            VELOCITY = 10
        else:
            VELOCITY = 5

        # Counter used for stepping animation
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_s] or keys_pressed[pygame.K_d]:
            if VELOCITY > 5:
               self.player.moving = (self.player.moving + 2) % 30
            else:
                self.player.moving = (self.player.moving + 1) % 30
        else:
            self.player.moving = 0
        
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
            velocity = self.checkCollisions(self.player.getEdges(key, velocity))
            self.player.look(key)
            self.player.move(key, velocity)

        if keys_pressed[pygame.K_e]:
            pass
            # self.isLookingAt(self.player)

    def checkCollisions(self, entity_edges):
        available_velocity = self.collision_detector.inBounds(entity_edges, self.current_room.getEdges())
        if available_velocity != 0:
            for entity in self.current_room.getEntities():
                temp_velocity = self.collision_detector.collides(entity_edges, entity.getEdges("", ""))
                if temp_velocity == 0:
                    return temp_velocity
                elif abs(temp_velocity) < abs(available_velocity):
                    available_velocity = temp_velocity
        return available_velocity

    def isLookingAt(self):
        for entity in self.current_room.getEntities():
            pass
            # if self.collision_detector.collides()