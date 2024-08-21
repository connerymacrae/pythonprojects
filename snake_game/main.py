from turtle import Screen, Turtle
from snake import Snake
import time


my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(height=600, width=600)
my_screen.title("Snakey McSnakeface")
my_screen.tracer(0)


snake = Snake()
# full_snake = []
# x_spot = 0
# for i in range(3):
#     snake_segment = Turtle('square')
#     snake_segment.color('white')
#     snake_segment.up()
#     snake_segment.goto(x_spot, 0)
#     x_spot -= 20
#     full_snake.append(snake_segment)

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.2)

    snake.move()
    # for seg_num in range(len(full_snake) - 1, 0, -1):
    #     new_x = full_snake[seg_num - 1].xcor()
    #     new_y = full_snake[seg_num - 1].ycor()
    #     full_snake[seg_num].goto(new_x, new_y)
    # full_snake[0].fd(20)


my_screen.exitonclick()