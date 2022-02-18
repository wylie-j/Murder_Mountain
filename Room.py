# from Person import Person
# from Player import Player
from Entity import imageMaker
from Entity import Entity
class Room(Entity):
    def __init__(self, WIDTH, HEIGHT, NAME):
        Entity.__init__(self, WIDTH, HEIGHT, 0, 0, NAME)
        self.person_list = []

    def getImage(self):
        return self.images[0]

    def collisionDetected(self, entity_edges):
        if not self.inBounds(entity_edges):
            return True
        for person in self.person_list:
            if self.collides(entity_edges, person.getEdges(0, 0, 0, 0)):
                return True
        return False

    def inBounds(self, entity_edges):
        print(entity_edges)
        if entity_edges[0] >= 0 and entity_edges[1] <= self.width and entity_edges[2] <= self.height and entity_edges[3] >= 0:
            return True
        else:
            return False

    def collides(self, entity1_edges, entity2_edges):
        if entity1_edges[0] >= entity2_edges[2] or entity1_edges[1] <= entity2_edges[3] or entity1_edges[2] <= entity2_edges[0] or entity1_edges[3] >= entity2_edges[1]:
            return False
        else:
            return True

