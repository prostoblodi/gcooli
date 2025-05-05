from random import randint

class Cat:
    def __init__(self, satiety=100, purity=100, fatigue=0, happiness=30):
        self.satiety = satiety # сытость
        self.purity = purity # чистота
        self.fatigue = fatigue # усталость
        self.happiness = happiness # уровень счастья
        self.isEnd = False

    def eat(self):
        self.satiety += randint(17, 30)
        print(f"Котик поел, теперь его сытость {self.satiety} единиц")

    def play(self):
        if 0 <= self.fatigue < 50:
            self.fatigue += 8
            self.satiety -= 5
            self.happiness += randint(10,14)
        elif 50 <= self.fatigue < 80:
            self.fatigue += 14
            self.satiety -= 15
            self.happiness += randint(5,11)
        elif 80 <= self.fatigue <= 100:
            self.fatigue += 9
            self.satiety -= 24
            self.happiness += randint(3,9)
        print(f"Г Котик поиграл, теперь он счастлив на {self.happiness} единиц, но \n"
              f"L его сытость теперь {self.satiety} единиц, а усталость - {self.fatigue} единиц")

    def sleep(self):
        self.fatigue = 0
        self.happiness += randint(-4, 6)
        print(f"Котик поспал, теперь его усталость - 0, а счастье {self.happiness} единиц.")

    def life(self):
        self.fatigue += randint(1,35)
        self.happiness -= randint(3,15)
        if self.happiness <= 100:
            self.play()
        if self.satiety < 20:
            self.eat()
        if self.fatigue >= 90:
            self.sleep()
        if self.satiety < 20:
            print(f"Котик остался без еды(его сытость {self.satiety} единиц), конец симуляции :(")
            self.isEnd = True
        if self.happiness <= 0:
            print(f"Котик впал в депрессию({self.happiness} единиц счастья), конец симуляции :(")
            self.isEnd = True

cat = Cat()
for i in range(0,101):
    if not cat.isEnd:
        day = f"День {i} суровой симуляции жизни котика"
        print("\n", f"{day:=^50}")
        cat.life()
if not cat.isEnd:
    print("Котик прожил все 100 дней!")