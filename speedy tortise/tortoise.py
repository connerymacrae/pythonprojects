from turtle import Turtle


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.up()
        self.setheading(90)
        self.color('green')
        self.goto(0, -220)

    def move_up(self):
        self.fd(10)

    def next_level(self):
        self.teleport(0, -220)

    def tort_spin(self):
        for num in range(12):
            self.heading() + 30
