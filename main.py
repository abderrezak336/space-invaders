from turtle import Screen, Turtle
from barrier import Barrier
from scoreboard import Scoreboard
from spaceship import Spaceship
from fire_ball import FireBall
from alien import Alien
import time
import random

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.listen()
gif_list = ["spaceship.gif", "alien1.gif", "alien2.gif", "alien3.gif", "master.gif", "my_bullet.gif", "exploision.gif", "bullet.gif"]

for l in gif_list:
    screen.register_shape(f"Assets/{l}")

fire_ball = FireBall()
alien_fireball = FireBall()
alien_fireball.hideturtle()
spaceship = Spaceship()
spaceship.add(fire_ball)
spaceship.shape("Assets/spaceship.gif")
aliens_list = []

left_barrier = Barrier(-150, -160)
right_barrier = Barrier(+150, -160)

scoreboard = Scoreboard()

def show_aliens():
    global aliens_list
    x = -290
    y = 200
    for r in range(5):
        for c in range(8):
            alien = Alien(x, y)
            alien_fireball = FireBall()  # Each alien gets its own fireball
            alien_fireball.shape("Assets/my_bullet.gif")
            alien.add(alien_fireball)
            alien.fireball.goto(x, y - 40)
            aliens_list.append(alien)
            x += 80
            if c % 7 == 0 and c != 0:
                x = -290
                y -= 60
            if r == 0:
                alien.shape("Assets/alien3.gif")
            elif 3 > r > 0:
                alien.shape("Assets/alien2.gif")
            else:
                alien.shape("Assets/alien1.gif")

show_aliens()
def move_aliens():
    for alien in aliens_list:
        alien.move_alien()

def go_down():
    for alien in aliens_list:
        alien.move_alien_down()

def check_aliens_move():
    for alien in aliens_list:
        if alien.xcor() > 365 or alien.xcor() < -365:
            go_down()
            change_aliens_direction()

def change_aliens_direction():
    for alien in aliens_list:
        alien.change_direction()

def reset_game():
    spaceship.shape("Assets/spaceship.gif")

fire_ball.shape("Assets/bullet.gif")
alien_fireball.shape("Assets/my_bullet.gif")
fire_ball.hideturtle()

screen.onkey(spaceship.go_left, "Left")
screen.onkey(spaceship.go_right, "Right")
screen.onkey(spaceship.shoot, "space")

def main():
    global aliens_list
    a = random.choice(aliens_list)
    time_speed = 0.05
    game_is_on = True
    while game_is_on:
        alive_aliens = [alien for alien in aliens_list if alien.is_alive == True]
        time.sleep(time_speed)
        screen.update()

        #move the aliens right and left and down
        move_aliens()

        check_aliens_move()

        #random alien shoot
        a.shoot()
        if a.fireball.ycor() < -300:
            a = random.choice(alive_aliens)

        #check the collision with the barriers
        if a.fireball.distance(right_barrier) < 50:
            a.stop_shooting()
            a = random.choice(alive_aliens)
            right_barrier.endurance -= 1
            if right_barrier.endurance <= 0:
                right_barrier.break_wall()
        if a.fireball.distance(left_barrier) < 50:
            a.stop_shooting()
            a = random.choice(alive_aliens)
            left_barrier.endurance -= 1
            if left_barrier.endurance <= 0:
                left_barrier.break_wall()


        if spaceship.is_shoot:
            spaceship.shoot()
        if fire_ball.ycor() > 300:
            spaceship.is_shoot = False
            fire_ball.set_x(spaceship.xcor())
            fire_ball.reset_fireball()


        #check if the fireball touch aliens
        for alien in aliens_list:
            if alien.ycor() <= -150:
                print("game over")
            if fire_ball.distance(alien) < 30:
                alien.shape("Assets/exploision.gif")
                screen.update()
                alien.die()
                spaceship.is_shoot = False
                fire_ball.set_x(spaceship.xcor())
                fire_ball.reset_fireball()
                scoreboard.increas_score()
            if alien.fireball.distance(spaceship) < 40:
                alien.stop_shooting()
                scoreboard.decrease_heart()
                screen.update()
                if scoreboard.heart <= 0:
                    print("game over")
                    spaceship.shape("Assets/exploision.gif")
                    alive_aliens = [a.die() for a in alive_aliens]
                    show_aliens()
                    scoreboard.update_top_score()
                    scoreboard.reset_score()
                    spaceship.shape("Assets/spaceship.gif")
                    main()


            if alien.fireball.ycor() < -300:
                alien.stop_shooting()


main()
screen.exitonclick()
