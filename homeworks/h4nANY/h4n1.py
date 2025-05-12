class Animal:
    def __init__(self):
        self.height = 100
        self.width = 25
        self.length = 60
        self.cuteness = 100
        self.satiety = 100
        self.vigor = 100

    def eat(self):
        self.satiety += 5

    def sleep(self):
        self.vigor += 100


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.height = 60
        self.cuteness = 80
        self.width = 40
        self.length = 90

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.height = 35
        self.cuteness = 80
        self.width = 30
        self.length = 60