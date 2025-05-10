import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.1
        self.gladness -= 3
        self.money -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 5

    def to_chill(self):
        print("Rest time")
        self.gladness += 8
        self.progress -= 0.05
        self.money -= 10

    def to_work(self):
        print("Working...")
        self.money += 50
        self.gladness -= 2

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money < 0:
            print("Bankruptcy…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def choose_activity(self):
        if self.gladness < 20:
            self.to_chill()
        elif self.money < 20:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        else:
            activity = random.choice(["study", "sleep", "chill", "work"])
            if activity == "study":
                self.to_study()
            elif activity == "sleep":
                self.to_sleep()
            elif activity == "chill":
                self.to_chill()
            elif activity == "work":
                self.to_work()

    def live(self, day):
        day = f"Day {day} of {self.name}'s life"
        print(f"{day:*^50}")
        self.choose_activity()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)
