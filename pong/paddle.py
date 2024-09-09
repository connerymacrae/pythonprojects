from turtle import Turtle


STARTING_POSITIONS = [(550, 20), (550, 0), (550, -20)]
MOVE_DISTANCE = 30
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.shape('square')
        self.setheading(UP)
        self.shapesize(1, 5)
        self.color('white')
        self.up()
        self.goto(x_coord, y_coord)


    #     self.full_paddle = []
    #     self.create_paddle()
    #
    # def create_paddle(self):
    #     for position in STARTING_POSITIONS:
    #         segment = Turtle('square')
    #         segment.color('white')
    #         segment.up()
    #         segment.goto(position)
    #         self.full_paddle.append(segment)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def move_down(self):
        self.bk(MOVE_DISTANCE)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)