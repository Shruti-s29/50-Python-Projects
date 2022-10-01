from shutil import move
from turtle import *
import turtle

# all capital letter means constant
X_POS = [0,-20,-40]


class snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]

    def create_snake(self):
        for i in range(3):
            t = Turtle(shape='square')
            t.color('white')
            t.penup()
            t.goto(X_POS[i],0)
            self.segments.append(t)

    def move_snake(self):
        ''' move whole snake forward in the direction of head.'''
        for seg_num in range(len(self.segments)-1,0,-1):        #range(start,stop,step)
            x_new = self.segments[seg_num-1].xcor()         # x cordinate
            y_new = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_new,y_new)
        self.head.forward(10)
        
    def up(self):
        ''' Move your snake up '''
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.move_snake()
    
    def down(self):
        ''' Move your snake down '''
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.move_snake()
    
    def left(self):
        ''' Move your snake left '''
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.move_snake()
    
    def right(self):
        ''' Move your snake right '''
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.move_snake()

    def expand(self):
        ''' Expands snake body'''
        new_part = Turtle(shape='square')
        new_part.color('white')
        new_part.penup()
        new_x = self.segments[len(self.segments)-1].xcor()
        new_y = self.segments[len(self.segments)-1].ycor()
        new_part.goto(new_x,new_y)
        self.segments.append(new_part)


