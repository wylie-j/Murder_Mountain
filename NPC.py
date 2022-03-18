from Person import Person
from Dialogue import Dialogue

class NPC(Person):
    def __init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME):
        self.dialogue = Dialogue()
        Person.__init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME)

    def interact(self):
        self.speak()

    def speak(self):
        print("yo")
        return self