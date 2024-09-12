from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color('white')
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed -= 0.02

    def reset(self):
        self.teleport(0, 0)
        self.paddle_hit()
        self.move_speed = 0.1
