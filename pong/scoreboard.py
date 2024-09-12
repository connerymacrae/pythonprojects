from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 80, 'bold')


class Scoreboard(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0
        self.ht()
        self.up()
        self.goto(x_pos, y_pos)
        self.pencolor('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over_message(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)