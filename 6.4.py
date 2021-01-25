# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name}. The car drives.")

    def stop(self):
        print(f"{self.name}. The car has stopped.")

    def turn(self, direction):
        print(f"{self.name}. The car has turned {'left' if direction == 'left' else 'right'}.")

    def show_speed(self):
        print(f"{self.name}. Vehicle's speed is {self.speed} km.")


    def special(self):
        if self.is_police is True:
            print(f"{self.name}. This is a police car!")


class Sport(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}. Slow down! Your speed is over limit!")
        else:
            print(f"{self.name}. Vehicle's speed is {self.speed} km.")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}. Slow down! Your speed is over limit!")
        else:
            print(f"{self.name}. Vehicle's speed is {self.speed} km.")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True
# полицейская машина


audi = Sport(120, "red", "Audi", False)
audi.go()
audi.stop()
audi.show_speed()
audi.turn("left")
audi.special()
ford = PoliceCar(100, "blue", "Ford", True)
ford.stop()
ford.go()
ford.special()
mini = TownCar(70, "green", "MiniCooper", False)
mini.go()
mini.show_speed()
renault = TownCar(40, "Yellow", "Taxi", False)
renault.turn("right")
jeep = WorkCar(30, "black", "4x4", False)
jeep.stop()

