from turtle import Turtle
from xmlrpc.client import FastParser



class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(0, -240)
        self.is_shoot = False
        self.fireball = None

    def go_left(self):
        self.goto(self.xcor() - 40, -240)
        self.fireball.goto(self.xcor() + 2, -195)

    def go_right(self):
        self.goto(self.xcor() + 40, -240)
        self.fireball.goto(self.xcor() + 2, -195)

    def shoot(self):
        self.fireball.showturtle()
        self.is_shoot = True
        self.fireball.move_fireball("up")

    def add(self, fireball_class):
        self.fireball = fireball_class

