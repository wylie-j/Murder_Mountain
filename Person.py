from Entity import Entity
# from Object import Object

class Person(Entity):
    def __init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME):
        Entity.__init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME)
        self.name = NAME
        # self.objects = []
        self.moving = 0
        self.velocity = 5

    def direction():
        pass