from turtle import *


class Ball(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape('circle')
        self.color("white")
        
        self.speed(3)
        self.penup()
        self.x_move = 4
        self.y_move = 7

    def move(self):
        self.setheading(125)
        # self.speed(0.01)
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new,y_new)

    def bounce_y(self):
        self.y_move *=-1
        

    def bounce_x(self):
        self.x_move *=-1
        


