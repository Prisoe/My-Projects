import random
from turtle import Turtle
COLORS = ["red", "yellow", "green", "blue", "purple", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        car_no = random.randint(1, 6)
        if car_no == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car.append(new_car)

    def move(self):
        for car in self.car:
            # new_x = car.xcor() - STARTING_MOVE_DISTANCE
            # car.goto(new_x, car.ycor())
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
