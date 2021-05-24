from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
#top_paddle = Paddle((100, 100))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")


# to make the game keeping updated and refreshed every single time, use While Loop:
game_is_on = True
while game_is_on:

    time.sleep(0.1)  # the ball goes up slowly at 0.1 pixel
    screen.update()
    ball.move()      # call a ball call

    # Detect collision with wall :

    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce :
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()


screen.exitonclick()
