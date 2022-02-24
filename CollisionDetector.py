class CollisionDetector:
    def __init__(self):
        pass
    
    # def collisionDetected(self, entity_edges):
    #         available_velocity = self.inBounds(entity_edges)
    #         if available_velocity != 0:
    #             for person in self.person_list:
    #                 temp_velocity = self.collides(entity_edges, person.getEdges("", ""))
    #                 if temp_velocity == 0:
    #                     return temp_velocity
    #                 elif abs(temp_velocity) < abs(available_velocity):
    #                     available_velocity = temp_velocity
    #         return available_velocity

    def inBounds(self, entity_edges, container_edges):
        VELOCITY = entity_edges[5]
        DIRECTION = entity_edges[4]
        # if entity_edges[0] >= 0 and entity_edges[1] <= self.width and entity_edges[2] <= self.height and entity_edges[3] >= 0:
        if DIRECTION == "up" and entity_edges[0] > container_edges[0]:
            if entity_edges[0] - VELOCITY >= container_edges[0]:
                return -VELOCITY
            else:
                return -entity_edges[0]
        if DIRECTION == "right" and entity_edges[1] < container_edges[1]:
            if entity_edges[1] + VELOCITY <= container_edges[1]:
                return VELOCITY
            else:
                return container_edges[1] - entity_edges[1]
        if DIRECTION == "down" and entity_edges[2] < container_edges[2]:
            if entity_edges[2] + VELOCITY <= container_edges[2]:
                return VELOCITY
            else:
                return container_edges[2] - entity_edges[2]
        if DIRECTION == "left" and entity_edges[3] > container_edges[3]:
            if entity_edges[3] - VELOCITY >= container_edges[3]:
                return -VELOCITY
            else:
                return -entity_edges[3]
        return 0

    def collides(self, entity1_edges, entity2_edges):
        VELOCITY = entity1_edges[5]
        DIRECTION = entity1_edges[4]
        # Check to see if its the same entity
        if entity1_edges[0] == entity2_edges[0] and entity1_edges[1] == entity2_edges[1] and entity1_edges[2] == entity2_edges[2] and entity1_edges[3] == entity2_edges[3]:
            if DIRECTION == "up" or DIRECTION == "left":
                return -VELOCITY
            else:
                return VELOCITY

        top_of = self.topOrLeftOf(entity1_edges[2], entity2_edges[0])
        right_of = self.bottomOrRightOf(entity1_edges[3], entity2_edges[1])
        bottom_of = self.bottomOrRightOf(entity1_edges[0], entity2_edges[2])
        left_of = self.topOrLeftOf(entity1_edges[1], entity2_edges[3])
        
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