# importing libraries

from turtle import Turtle ,Screen 
import time 
from snake import *
from food import *
from score import *
# pop up windown / Screen 
scr = Screen()
scr.setup(width=600,height=600)
scr.title("Snake Game By Shruti")
scr.bgcolor('black')
scr.tracer(0)   # Doesn't show any procedure on screen untill update is called
scr.screensize(350,350)
# main code

    #creating Snake body
snk = Snake()
    # Food
f = Food()
    # score show on screen S
score = scoreboard()
disp = Display()
    #reading the input from keyboard
scr.listen()
    # onkey take argument as (what to do, when which key is pressed)
scr.onkey(snk.up,"Up")
scr.onkey(snk.down,"Down")
scr.onkey(snk.left,"Left")
scr.onkey(snk.right,"Right")

game_is_onn = True
while game_is_onn:
    
    scr.update()
    time.sleep(0.1)   # decrease the sleep time to increase the speed of snake
    snk.move()

    # collision with food
    if snk.head.distance(f) < 17:
        f.refresh()
        snk.extend()
        score.update_score()

    # breaking condition 
     # collision with the wall
    if (snk.head.xcor() > 290) or (snk.head.xcor() < -290) or (snk.head.ycor() > 290) or (snk.head.ycor() < -290) :
        game_is_onn = False
        score.game_over()
        
     # collision with its own tail
    for seg in snk.segments[1:]:
        if seg == snk.head:
            pass
        if snk.head.distance(seg) < 5:
            game_is_onn = False
            score.game_over()


#exit
scr.exitonclick()