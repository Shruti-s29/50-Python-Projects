from turtle import Turtle
import random as rnd 

class Food(Turtle):
    # food's shape is a circle of diameter 10
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        new_x = rnd.randint(-270,270)
        new_y = rnd.randint(-270,270)
        self.goto(new_x,new_y)

