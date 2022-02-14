from Entity import Entity
# from Object import Object

class Person(Entity):
    def __init__(self, IMAGE_LOCATION, WIDTH, HEIGHT, X_COORD, Y_COORD, name):
        Entity.__init__(self, IMAGE_LOCATION, WIDTH, HEIGHT, X_COORD, Y_COORD)
        self.name = name
        # self.objects = []
        self.facing = ""

    def direction():
        pass