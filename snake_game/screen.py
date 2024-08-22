from turtle import Screen


class SnakeScreen:
    def __init__(self):
        self.create_screen()

    def create_screen(self):
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor('black')
        screen.title('Snakey McSnakeface')
        screen.tracer(0)

    def listen(self):
        self.listen()