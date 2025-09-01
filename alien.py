from turtle import Turtle
from xmlrpc.client import FastParser
import time
from fire_ball import FireBall
fire_ball = FireBall()


class Alien(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(x, y)
        self.x = 1
        self.y = 2
        self.fireball = None
        self.is_shooting = False
        self.is_alive = True

    def move_alien(self):
        self.goto(self.xcor() + self.x , self.ycor())
        # Only move the fireball if it's active (i.e., alien is shooting)
        if self.is_shooting:
            self.fireball.move_fireball("down")


    def change_direction(self):
        self.x *= -1

    def hit_the_wall(self):
        if self.xcor() > 365 or self.xcor() < -365:
            self.change_direction()

    def move_alien_down(self):
        self.goto(self.xcor(), self.ycor() - self.y)
        # self.fireball.goto(self.xcor(), self.ycor() - self.y)

    def die(self):
        self.goto(self.xcor(), self.ycor() + 1000)
        self.is_alive = False

    def add(self, fire_ball):
        self.fireball = fire_ball

    def shoot(self):
        if not self.is_shooting:  # Only shoot if the alien isn't already shooting
            self.is_shooting = True
            self.fireball.goto(self.xcor(), self.ycor() - 40)
            self.fireball.showturtle()

    def stop_shooting(self):
        self.fireball.goto(self.xcor(), self.ycor() - 40)
        self.is_shooting = False
        self.fireball.hideturtle()
