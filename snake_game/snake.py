from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.up()
            segment.goto(position)
            self.full_snake.append(segment)
        # self.snake = Turtle("square")
        # self.color = self.snake.color('white')

    def move(self):
        for seg_num in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[seg_num - 1].xcor()
            new_y = self.full_snake[seg_num - 1].ycor()
            self.full_snake[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
