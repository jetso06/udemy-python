from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(5, 1)
        self.penup()
        self.teleport(x_cord, y_cord)

    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)