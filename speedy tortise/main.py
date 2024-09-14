from turtle import Screen
from tortoise import Tortoise
from car import Car
from scoreboard import Scoreboard
import time


turtle_screen = Screen()
turtle_screen.setup(500, 500)
turtle_screen.title("Run, Tortoise, Run!")
turtle_screen.tracer(0)

tortoise = Tortoise()
car = Car()
scoreboard = Scoreboard()
car.new_car()

turtle_screen.listen()
turtle_screen.onkey(tortoise.move_up, "Up")
# turtle_screen.onkey(turtle.move_down, "Down")
# turtle_screen.onkey(turtle.move_up, "w")
# turtle_screen.onkey(turtle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    turtle_screen.update()

    car.move()

    if tortoise.ycor() > 180:
        scoreboard.increase_score()
        tortoise.next_level()
        car.speed_up()

    for mover in car.car_list:
        if tortoise.distance(mover) < 20:
            game_is_on = False
            scoreboard.game_over_message()










turtle_screen.exitonclick()
