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
            self.add_segment(position)
        # self.snake = Turtle("square")
        # self.color = self.snake.color('white')

    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.up()
        segment.goto(position)
        self.full_snake.append(segment)

    def move(self):
        for seg_num in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[seg_num - 1].xcor()
            new_y = self.full_snake[seg_num - 1].ycor()
            self.full_snake[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def add_to_tail(self):
        self.add_segment(self.full_snake[-1].position())
        # tail_position_x = self.full_snake[-1].xcor()
        # tail_position_y = self.full_snake[-1].ycor()
        # segment = Turtle('square')
        # segment.color('white')
        # segment.up()
        # segment.goto(tail_position_x - 20, tail_position_y)
        # self.full_snake.append(segment)

    def reset(self):
        for seg in self.full_snake:
            seg.goto(-1500, 0)
        self.full_snake.clear()
        self.create_snake()
        self.head = self.full_snake[0]

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
