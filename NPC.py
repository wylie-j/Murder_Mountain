from Person import Person

class NPC(Person):
    def __init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME):
        Person.__init__(self, WIDTH, HEIGHT, X_COORD, Y_COORD, NAME)

    def speak():
        print("yo")