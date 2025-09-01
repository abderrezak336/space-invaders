from turtle import Turtle


class FireBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(2, -195)
        self.y_move = 20
        self.spaceship_x = self.xcor()

    def move_fireball(self, dire):
        new_y = self.ycor() + self.y_move if dire == "up" else self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)

    def reset_fireball(self):
        self.penup()
        self.goto(self.spaceship_x, -195)
        self.hideturtle()

    def set_x(self, new_x):
        self.spaceship_x = new_x

