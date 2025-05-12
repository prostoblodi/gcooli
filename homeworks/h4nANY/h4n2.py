class Person:
    def __init__(self):
        self.birthYear = 0
        self.name = "Anatoly"

    def calculate_age(self, year):
        age = year - self.birthYear
        return age

class Driver(Person):
    def __init__(self):
        super().__init__()
        self.licenseNumber = 512355