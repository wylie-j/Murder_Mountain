# from Person import Person
# from Player import Player
from Entity import imageMaker
from Entity import Entity
class Room(Entity):
    def __init__(self, WIDTH, HEIGHT, NAME):
        Entity.__init__(self, WIDTH, HEIGHT, 0, 0, NAME)
        self.person_list = []
        
    def topOrLeftOf(self, entity1, entity2):
        if entity1 <= entity2:
            return True
        else:
            return False

    def bottomOrRightOf(self, entity1, entity2):
        if entity1 >= entity2:
            return True
        else:
            return False

    def getImage(self):
        return self.images[0]

    def collisionDetected(self, entity_edges):
        available_velocity = self.inBounds(entity_edges)
        if available_velocity != 0:
            for person in self.person_list:
                temp_velocity = self.collides(entity_edges, person.getEdges("", ""))
                if temp_velocity == 0:
                    return temp_velocity
                elif temp_velocity < available_velocity:
                    available_velocity = temp_velocity
        return available_velocity

    def inBounds(self, entity_edges):
        VELOCITY = entity_edges[5]
        DIRECTION = entity_edges[4]
        if entity_edges[0] >= 0 and entity_edges[1] <= self.width and entity_edges[2] <= self.height and entity_edges[3] >= 0:
            if DIRECTION == "up" and entity_edges[0] - VELOCITY > VELOCITY * -1:
                if entity_edges[0] - VELOCITY >= 0:
                    return -VELOCITY
                else:
                    return -entity_edges[0]
            if DIRECTION == "right" and entity_edges[1] + VELOCITY < self.width + VELOCITY :
                if entity_edges[1] + VELOCITY <= self.width:
                    return VELOCITY
                else:
                    return self.width - entity_edges[1]
            if DIRECTION == "down" and entity_edges[2] + VELOCITY < self.height + VELOCITY:
                if entity_edges[2] + VELOCITY <= self.height:
                    return VELOCITY
                else:
                    return self.height - entity_edges[2]
            if DIRECTION == "left" and entity_edges[3] - VELOCITY > VELOCITY * -1:
                if entity_edges[3] - VELOCITY >= 0:
                    return -VELOCITY
                else:
                    return -entity_edges[3]
            return 0
        else:
            return 0

    def collides(self, entity1_edges, entity2_edges):
        # if entity1_edges[0] >= entity2_edges[2] or entity1_edges[1] <= entity2_edges[3] or entity1_edges[2] <= entity2_edges[0] or entity1_edges[3] >= entity2_edges[1]:
        #     return 0
        # else:
        #     return 1
        top_of = self.topOrLeftOf(entity1_edges[2], entity2_edges[0])
        right_of = self.bottomOrRightOf(entity1_edges[3], entity2_edges[1])
        bottom_of = self.bottomOrRightOf(entity1_edges[0], entity2_edges[2])
        left_of = self.topOrLeftOf(entity1_edges[1], entity2_edges[3])
        VELOCITY = entity1_edges[5]
        DIRECTION = entity1_edges[4]
        if DIRECTION == "up":
            if (top_of  or right_of or left_of) or entity1_edges[0] - VELOCITY >= entity2_edges[2]:
                return -VELOCITY
            elif bottom_of and entity1_edges[0] - entity2_edges[2] < VELOCITY :
                return entity2_edges[2] - entity1_edges[0]
        elif DIRECTION == "right" :
            if (top_of  or right_of or bottom_of) or entity1_edges[1] + VELOCITY <= entity2_edges[3]:
                return VELOCITY
            elif left_of and entity2_edges[3] - entity1_edges[1] < VELOCITY:
                return entity2_edges[3] - entity1_edges[1]
        elif DIRECTION == "down":
            if (bottom_of  or right_of or left_of) or entity1_edges[2] + VELOCITY <= entity2_edges[0]:
                return VELOCITY
            elif top_of and entity2_edges[0] - entity1_edges[2] < VELOCITY:
                return entity2_edges[0] - entity1_edges[2]
        elif DIRECTION == "left":
            if (top_of  or left_of or bottom_of) or entity1_edges[3] - VELOCITY >= entity2_edges[1]:
                return -VELOCITY
            elif right_of and entity1_edges[3] - entity2_edges[1] < VELOCITY:
                return entity2_edges[1] - entity1_edges[3]
        return 0
