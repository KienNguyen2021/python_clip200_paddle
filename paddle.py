
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")    # the self shape is square
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)   # self is in the center, height=5, width=1
        self.penup()
        self.goto(position)    # x = 350 forward, y =0



    def go_up(self):  # Go_up is function

            new_y = self.ycor() + 20  # go up by 20 pixel
            self.goto(self.xcor(), new_y)

    def go_down(self):  # Go_up is function

            new_y = self.ycor() - 20  # go down by 20 pixel
            self.goto(self.xcor(), new_y)


