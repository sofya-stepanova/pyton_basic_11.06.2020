class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


    def go(self):
        print('автомобиль начал движение')

    def stop(self):
        print('автомобиль остановился')

    def turn(self, direction):
        print(f'автомобиль повернул {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('превышение скорости')
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('превышение скорости')
        else:
            print(self.speed)


class SportCar(Car):
    def __init__(self, price):
        self.price = price


class PoliceCar(Car):
    is_police = True


a = WorkCar(60, 'red', 'mazda')
b = SportCar(30000)
c = PoliceCar(80, 'blue', 'toyota')
print(c.is_police)
print(b.price)
a.go()
a.turn('направо')
a.stop()
a.show_speed()
print(a.color)
print(a.is_police)