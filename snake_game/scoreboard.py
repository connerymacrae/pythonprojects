from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Helvetica', 24, 'italic')



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.up()
        self.goto(0, 260)
        self.pencolor('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:    {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over_message(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


