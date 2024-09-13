from turtle import Turtle


class PongScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.up()
        self.goto(0, 400)
        self.pencolor('white')
        self.setheading(270)
        self.make_court()

    def make_court(self):
        while self.ycor() > -400:
            self.down()
            self.fd(20)
            self.up()
            self.fd(20)
