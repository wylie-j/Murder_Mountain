# from Person import Person
# from Player import Player
from Entity import imageMaker
from Entity import Entity
class Room(Entity):
    def __init__(self, WIDTH, HEIGHT, NAME):
        Entity.__init__(self, WIDTH, HEIGHT, 0, 0, NAME)
        self.NPC_list = []
        self.object_list = []
        
    def getEdges(self):
        return (self.rect.y, self.rect.x + self.width, self.rect.y + self.height, self.rect.x, "", "")

    def getImage(self):
        return self.images[0]

    def getEntities(self):
        return self.NPC_list + self.object_list