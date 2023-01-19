from turtle import *
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0,-300)
        self.shape('turtle')
        self.color('brown')

    def up(self):
        self.forward(10)
    
    def down(self):
        self.backward(10)

    def start_again(self):
        self.goto(0,-300)
        self.penup()
        self.setheading(90)

class Line(Turtle):
    
    def draw_line(self):
        self.hideturtle()
        self.goto(-320,290)
        self.pencolor('red')
        self.pendown()
        self.goto(320,290)
        
        self.penup()

        self.goto(-320,-280)
        self.pencolor('red')
        self.pendown()
        self.goto(320,-280)
