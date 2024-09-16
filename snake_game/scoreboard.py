from turtle import Turtle
with open("highscore.txt") as file:
    saved_score = file.read()

ALIGNMENT = 'center'
FONT = ('Helvetica', 24, 'italic')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(saved_score)
        self.ht()
        self.up()
        self.goto(0, 260)
        self.pencolor('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:    {self.score}  High Score:   {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over_message(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
