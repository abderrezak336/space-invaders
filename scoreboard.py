from turtle import Turtle


def read_top_score():
    with open("top_score.txt", mode="r") as data:
        top_score = data.read()
    return top_score

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.heart = 3
        self.color("white")
        self.hideturtle()
        self.penup()
        self.updatescreen()

    def updatescreen(self):
        self.clear()
        self.goto(-10, 260)
        self.write(f"Score: {self.score}", align="center", font=("arial", 20, "normal"))
        self.goto(-290, 260)
        self.write(f"Top Score: {read_top_score()}", align="center", font=("arial", 20, "normal"))
        self.goto(+290, 260)
        self.write(f"Hearts: {self.heart}", align="center", font=("arial", 20, "normal"))


    def increas_score(self):
        self.score += 10
        self.updatescreen()

    def decrease_heart(self):
        self.heart -= 1
        self.updatescreen()

    def update_top_score(self):
        if self.score > int(read_top_score()):
            with open("top_score.txt", mode="w") as file:
                file.write(f"{self.score}")

    def reset_score(self):
        self.score = 0
        self.heart = 3
        self.updatescreen()






