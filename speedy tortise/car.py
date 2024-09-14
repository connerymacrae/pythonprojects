from turtle import Turtle
import random

CAR_COLORS = ('red', "orange", 'yellow', 'blue',
              'violet', 'hotpink', 'purple', 'pink', 'magenta', 'turquoise',)


class Car:
    def __init__(self):
        self.car_list = []
        self.car_speed = 5
        # self.pos_list = []

    def new_car(self):
        car = Turtle('square')
        car.shapesize(1, 2)
        car.setheading(180)
        car.up()
        car.color(random.choice(CAR_COLORS))
        # car.color(CAR_COLORS[random.randrange(len(CAR_COLORS))])
        car.goto(220, random.randint(-150, 150))
        self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.fd(self.car_speed)
            # new_x = car.xcor() - 5
            # car.goto(new_x, car.ycor())
        if len(self.car_list) < 1:
            pass
        elif self.car_list[-1].xcor() < 180:
            self.new_car()

    # def possible_collisions(self):
    #     for car in self.car_list:
    #         self.pos_list.append(car.pos())

    def speed_up(self):
        self.car_speed += 1.5

    def speed_reset(self):
        self.car_speed = 5
