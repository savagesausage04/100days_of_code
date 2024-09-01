from turtle import Screen
from ball import Ball
from paddle import Paddle
from blocks import Blocks
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

COLORS = ["yellow", "green", "orange", "red"]


paddle = Paddle(x_pos=0, y_pos=-240)
ball = Ball()

X_START = -360
Y_START = 0
y = Y_START
block_list = []
for r in range(0, 4):
    for b in range(0, 2):
        x = X_START
        for a in range(0, 10):
            block = Blocks(x_pos=x, y_pos=y, color=COLORS[r])
            block_list.append(block)
            screen.update()
            x += 80
        y += 20


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

start_time = time.time()

game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_side_wall()

    if ball.ycor() > 280:
        ball.bounce_top_wall()
        ball.change_speed()

    if ball.ycor() < -220 and ball.distance(paddle) < 50:
        ball.bounce_paddle()

    for block in block_list:
        if block.ycor() - ball.ycor() <= 30 and ball.distance(block) < 50:
            block.hideturtle()
            ball.bounce_top_wall()
            block_list.remove(block)

    if len(block_list) == 0:
        ball.win()

    if ball.ycor() < -280:
        ball.reset()
        game_on = False

screen.exitonclick()