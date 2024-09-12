from turtle import Screen
# from pong_screen import PongScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

"""
1. Create screen with dashes down the middle
2. create pong paddle
    a. 3 turtles
    b. move up and down
3. create ball
    a. one turtle
    b. bounce off paddle and y 400, y -400
    c. score if x 600, x -600
4. create score board
    a. left and right

screen class
paddle class
ball class
scoreboard class
"""

pong_screen = Screen()
pong_screen.bgcolor('black')
pong_screen.setup(height=800, width=1200)
pong_screen.title("Pongy McPongface")
pong_screen.tracer(0)

r_paddle = Paddle(560, 0)
l_paddle = Paddle(-560, 0)
ball = Ball()
l_score = Scoreboard(-100, 300)
r_score = Scoreboard(100, 300)

pong_screen.listen()
pong_screen.onkey(r_paddle.move_up, "Up")
pong_screen.onkey(r_paddle.move_down, "Down")
pong_screen.onkey(l_paddle.move_up, "w")
pong_screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    pong_screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detect Collision with Ceiling/Floor
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce()

    # Detect collision with r_paddle
    if ball.xcor() > 530 and ball.distance(r_paddle) < 50 or ball.xcor() < -530 and ball.distance(l_paddle) < 50:
        ball.paddle_hit()

    if ball.xcor() > 590:
        l_score.increase_score()
        ball.reset()
    
    if ball.xcor() < -590:
        r_score.increase_score()
        ball.reset()


pong_screen.exitonclick()

# pong_screen = PongScreen()

# pong_screen.exitonclick()
