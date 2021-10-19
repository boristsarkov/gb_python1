class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Warning! Your speed is more than max!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Белая', 'Спорткар', False)
town_car = TownCar(140, 'Серебристая', 'Городской автомобиль', False)
work_car = WorkCar(90, 'Черная', 'Рабочая машина', False)
police_car = PoliceCar(210, 'Сине-белая', 'Плицейский автомобиль', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('right')