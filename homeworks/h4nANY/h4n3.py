class Transport:
    def __init__(self):
        self.speed = 100
        self.xCoordinate = 0

    def move(self):
        self.xCoordinate += self.speed

class Car(Transport):
    def __init__(self):
        super().__init__()
        self.speed = 120

class Plane(Transport):
    def __init__(self):
        super().__init__()
        self.speed = 550

class Train(Transport):
    def __init__(self):
        super().__init__()
        self.speed = 70