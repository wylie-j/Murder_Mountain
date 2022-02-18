import pygame
from Person import Person
# from main import VIEWPORT_HEIGHT, VIEWPORT_WIDTH

class Player(Person):
    def __init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME):
        Person.__init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME)

    def move(self, keys_pressed, room):
        # Counter used for stepping animation
        VIEWPORT_HEIGHT = 720
        VIEWPORT_WIDTH = 1250
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_s] or keys_pressed[pygame.K_d]:
            self.moving = (self.moving + 1) % 30
        else:
            self.moving = 0

        # Running
        if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
            self.velocity = 10
        else:
            self.velocity = 5

        # This section is dependant on how we loaded the images
        # The order is front(0), front stepping(1), back(2), 
        # back stepping(3), left(4), left stepping(5), right(6), right stepping(7)
        if keys_pressed[pygame.K_w]:
            self.current_image = 2 
            if not room.collisionDetected(self.getEdges(self.velocity, 0, 0, 0)):
                self.rect.y -= self.velocity
        if keys_pressed[pygame.K_s]:
            self.current_image = 0
            if not room.collisionDetected(self.getEdges(0, 0, self.velocity, 0)): 
                self.rect.y += self.velocity
        if keys_pressed[pygame.K_a]:
            self.current_image = 4
            if not room.collisionDetected(self.getEdges(0, 0, 0, self.velocity)): 
                self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d]:
            self.current_image = 6
            if not room.collisionDetected(self.getEdges(0, self.velocity, 0, 0)): 
                self.rect.x += self.velocity

