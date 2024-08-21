from turtle import Turtle, Screen
import random


def start_race(num_turts, color_list, turtle_list):
    starting_y = -120.0
    for i in range(num_turts):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(color_list[i])
        new_turtle.up()
        new_turtle.goto(-230, starting_y)
        starting_y += 50
        turtle_list.append(new_turtle)


colors = ['red', 'blue', 'orange', 'purple', 'green', 'pink']
racers = []

is_race_on = False

screen = Screen()
screen.setup(500, 400)


start_race(6, colors, racers)

user_bet = screen.textinput("Make Your Bet", "Which turtle will win? Enter a color:")

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                racer.goto(0, 0)
                racer.down()
                racer.circle(100)
            else:
                racer.goto(0, 0)
                racer.down()
                racer.left(225)
                racer.fd(225)

        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)


screen.exitonclick()
