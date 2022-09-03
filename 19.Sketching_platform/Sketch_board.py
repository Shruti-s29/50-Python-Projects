# importing libraries
from turtle import *

# making of a timmy and screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red","black")
scr = Screen()


# defining func
def move_forward():
    timmy.forward(10)       # forward by 10 paces

def move_backward():
    timmy.backward(10)

def clear_canvas():
    timmy.clear()
    timmy.penup()
    timmy.setposition(0.00,0.00)
    timmy.pendown()

def tilt_CW():
    new_head = timmy.heading() + 10
    timmy.setheading(new_head)

def tilt_CCW():
    new_head = timmy.heading() - 10
    timmy.setheading(new_head)

# main
scr.listen()
scr.onkey(fun=move_forward,key='Right')
scr.onkey(fun=move_backward,key='Left')
scr.onkey(fun=clear_canvas,key='c')
scr.onkey(fun=tilt_CW,key="Up")
scr.onkey(fun=tilt_CCW,key="Down")



#exit
scr.exitonclick()