from turtle import *
import random
import turtle

#screen setup
scr = Screen()
scr.setup(width = 800, height=600)
race_onn = False

#input on pop
user_inp = scr.textinput(title=" Welcome! To the game - Make a Bet", prompt="Enter the colour of turtle who will win ? 'Red','Blue','Orange','Pink','Purple','Green','SlateGrey','SaddleBrown' ")

# turtle formation and location

color_list = ['Red','Blue','Orange','Pink','Purple','Green','SlateGrey','SaddleBrown']
y_pos = [-150,-100,-50,0,50,100,150,200]
turtle_list = []
for i in range(8):
    new = Turtle(shape='turtle')
    new.color(color_list[i])
    new.penup()
    new.goto(x=-350,y=y_pos[i])
    turtle_list.append(new)


#race
if user_inp:
    race_onn = True

while race_onn:
    for turtles in turtle_list:
        if turtles.xcor()>350:
            race_onn = False
            win_color = turtles.pencolor()
            if win_color.lower() == user_inp.lower():
                print(f"You Won !! {win_color} Turtle is the winner")
            else:
                print(f"Ohh ! You Lost !! {win_color} Turtle is the winner")

        rand_distance = random.randint(0,10)
        turtles.forward(rand_distance)


#exit
scr.exitonclick()