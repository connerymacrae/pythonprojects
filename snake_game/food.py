from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("green")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x_coord = random.randint(-260, 260)
        random_y_coord = random.randint(-260, 260)
        self.teleport(random_x_coord, random_y_coord)
