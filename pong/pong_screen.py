import turtle


SCREENHEIGHT = 800
SCREENWIDTH = 1200


class PongScreen(turtle.Screen):
    def __init__(self):
        super().__init__()
        self.bgcolor('black')
        self.setup(height=SCREENHEIGHT, width=SCREENWIDTH)
        self.title("Pongy McPongface")
        # self.tracer(0)
        # self.make_court()
        # self.exitonclick()

    def make_court(self):
        board_turtle = turtle.Turtle()
        board_turtle.pencolor('white')
        board_turtle.up()
        board_turtle.goto(0, SCREENHEIGHT/2)
        board_turtle.setheading(270)
        while board_turtle.ycor() > -SCREENHEIGHT/2:
            board_turtle.down()
            board_turtle.fd(20)
            board_turtle.up()
            board_turtle.fd(20)
