# import colorgram
#
# colors = colorgram.extract('image.jpg', 24)
#
# extracted_colors = []
#
# for color in colors:
#     color_choice = (color.rgb.r, color.rgb.g, color.rgb.b)
#     extracted_colors.append(color_choice)
#
# print(extracted_colors)
import random
import turtle
from turtle import Turtle, Screen

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49),
              (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
              (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216)]

''' 10 x 10 dot painting
    each dot is 20 and spaced 50 apart,
    '''


def make_dots(num_rows, num_dots, cursor, list_of_colors):
    while num_rows > 0:
        for i in range(num_dots):
            cursor.fd(50)
            cursor.dot(20, random.choice(list_of_colors))
        num_rows -= 1
        cursor.teleport(-275, (cursor.ycor() + 50))


turtle.colormode(255)
hirst = Turtle()
hirst.hideturtle()
hirst.up()
hirst.teleport(-275, -275)
make_dots(12, 8, hirst, color_list)
# for num in range(10):
#     make_dots(10, 10, hirst, color_list)
#     hirst.teleport(-275, (hirst.ycor() + 50))


screen = Screen()
screen.screensize(300, 300)
screen.exitonclick()


""" this is the code challenge solution"""

# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()

# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124),
# (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35),
# (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50),
# (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64),
# (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
#
#
#
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()
