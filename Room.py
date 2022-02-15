# from Person import Person
# from Player import Player
from Entity import imageMaker
class Room:
    def __init__(self, IMAGE, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self.images = imageMaker(IMAGE, WIDTH, HEIGHT)
        self.image = self.images[0]
