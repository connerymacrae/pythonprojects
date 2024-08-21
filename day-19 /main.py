from turtle import Turtle, Screen


jarje = Turtle()


def mov_fd():
    jarje.fd(10)


def mov_bk():
    jarje.bk(10)


def spin_lft():
    jarje.left(10)


def spin_rt():
    jarje.right(10)


def clear():
    jarje.clear()
    jarje.teleport(0, 0)


screen = Screen()
screen.listen()

screen.onkey(key='w', fun=mov_fd)
screen.onkey(key='s', fun=mov_bk)
screen.onkey(key='a', fun=spin_lft)
screen.onkey(key='d', fun=spin_rt)
screen.onkey(key='c', fun=clear)


screen.exitonclick()
