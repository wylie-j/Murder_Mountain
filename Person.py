from Entity import Entity
# from Object import Object

class Person(Entity):
    def __init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME):
        Entity.__init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME)
        self.name = NAME
        # self.objects = []
        self.moving = 0

    def getImage(self):
        image_number = 0
        if self.facing == "up":
            image_number = 0
        elif self.facing == "right":
            image_number = 2
        elif self.facing == "down":
            image_number = 4
        elif self.facing == "left":
            image_number = 6
        if self.moving >= 15:
            image_number += 1
        return self.images[image_number]