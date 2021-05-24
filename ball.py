from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.x_move = 10  # increase by 10 pixel
        self.y_move = 10  # increase by 10 pixel

    def move(self):
        new_x = self.xcor() + self.x_move  # increase by 10 pixel
        new_y = self.ycor() + self.y_move  # increase by 10 pixel
        self.goto(new_x, new_y)

    def bounce_y(self):  # reverse the moving of ball--> bounce
        self.y_move *= -1  # Reverse the ball moving direction : +10--> -10

    def bounce_x(self):
        self.x_move *= -1
