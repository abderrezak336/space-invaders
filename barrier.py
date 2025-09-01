from turtle import Turtle






class Barrier(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("#F8AD18")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x, y)
        self.endurance = 30


    def break_wall(self):
        self.goto(self.xcor(), self.ycor() + 1000)