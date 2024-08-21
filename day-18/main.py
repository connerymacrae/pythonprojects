import turtle
import random
from turtle import Turtle, Screen


def square(cursor, length):
    for step in range(4):
        cursor.forward(length)
        cursor.left(90)


def change_color():
    return tuple(random.randint(0, 255) for _ in range(3))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def dashes(steps, cursor, length):
    for step in range(steps):
        cursor.forward(length)
        cursor.up()
        cursor.forward(length)
        cursor.down()


def draw_shape(sides, cursor, length, ):
    cursor.color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    angle = 360/sides
    for side in range(sides):
        cursor.forward(length)
        cursor.left(angle)


def random_walk(num_steps, cursor, speed):
    cursor.pen(pensize=10, speed=speed)
    directions = [0, 90, 180, 270]
    for step in range(num_steps):
        cursor.color(random_color())
        cursor.setheading(random.choice(directions))
        cursor.forward(20)


def spirograph(cursor, radius, deg_turn):
    for i in range(360):
        cursor.color(change_color())
        cursor.circle(radius)
        cursor.setheading(cursor.heading() + deg_turn)
        if cursor.heading() == 0.0:
            return



jeorje_turtle = Turtle()
jeorje_turtle.shape("turtle")
jeorje_turtle.color('firebrick1')
turtle.colormode(255)
# square(jeorje_turtle, 180)
# jeorje_turtle.clear()
#
# jeorje_turtle.up()
# jeorje_turtle.bk(300)
# jeorje_turtle.down()
# dashes(50, jeorje_turtle, 10)
#
# jeorje_turtle.clear()
# jeorje_turtle.up()
# jeorje_turtle.home()
# jeorje_turtle.right(90)
# jeorje_turtle.forward(200)
# jeorje_turtle.left(90)
# jeorje_turtle.down()
#
# for i in range(3, 11):
#     draw_shape(i, jeorje_turtle, 150)


# random_walk(100, jeorje_turtle, 5)

jeorje_turtle.speed(0)
spirograph(jeorje_turtle, 100, 2)









screen = Screen()
screen.exitonclick()
