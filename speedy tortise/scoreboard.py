from turtle import Turtle
ALIGNMENT = 'left'
FONT = ('Courier', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.ht()
        self.up()
        self.goto(-230, 220)
        self.pencolor('black')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over_message(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
