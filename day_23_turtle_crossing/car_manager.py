from car import Car
import math

CAR_AMOUNT = 30


class CarManager:

    def __init__(self):
        self.cars = []
        self._create_cars()

    def _create_cars(self):
        while len(self.cars) < CAR_AMOUNT:
            car = Car()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()
        self._update_cars()

    def _update_cars(self):
        for car in self.cars:
            if car.xcor() < - 325:
                car.reset()

    def check_collision(self, turtle):
        if any(car.distance(turtle) < 40 and math.fabs(car.ycor() - turtle.ycor()) < 20 for car in self.cars):
            return True
        return False

    def increase_speed(self):
        for car in self.cars:
            car.increase_speed()
