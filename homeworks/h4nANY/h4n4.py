class Device:
    def __init__(self):
        self.isActivated = False

    def on(self):
        self.isActivated = True

    def off(self):
        self.isActivated = False

class Phone(Device):
    def __init__(self):
        super().__init__()
        self.mobility = "very"

class PC(Device):
    def __init__(self):
        super().__init__()
        self.power = "many"

class Laptop(Device):
    def __init__(self):
        super().__init__()
        self.cool = True