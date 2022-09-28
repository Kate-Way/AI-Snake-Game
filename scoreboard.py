from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open('data.txt') as keep_score:
            self.high_score = int(keep_score.read())
        # position at the top of the screen
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as keep_score:
                keep_score.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.score += 1
        self.update_scoreboard()





