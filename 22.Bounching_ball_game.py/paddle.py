from turtle import *

class Paddle(Turtle):   #Usage of inheritance
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        y = self.ycor()
        # if self.distance(250,250) < 10:
        #     self.go_down
        y_new = y + 20
        x= self.xcor()
        self.goto(x,y_new)

    def go_down(self):
        y = self.ycor()
        # if self.distance(250,-250)<10:
        #     self.go_up
        y_new = y - 20
        x= self.xcor()
        self.goto(x,y_new)