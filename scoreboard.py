from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)



