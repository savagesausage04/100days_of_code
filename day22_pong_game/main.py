from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if (ball.distance(r_paddle) < 40 and ball.xcor() > 315) or (ball.distance(l_paddle) < 40 and ball.xcor() < -315):
        ball.bounce_paddle()



    if ball.xcor() > 390:
        ball.reset()
        scoreboard.left_point()


    if ball.xcor() < -390:
        ball.reset()
        scoreboard.right_point()

screen.exitonclick()
