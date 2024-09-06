from turtle import Screen
import time


class SnakeScreen:
    def __init__(self):
        self.create_screen()


    def create_screen(self):
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor('black')
        screen.title('Snakey McSnakeface')
        screen.tracer(0)
        screen.exitonclick()


    def game_mode(self):
        self.update()
        time.sleep(0.2)


    # def listen(self):
    #     self.listen()