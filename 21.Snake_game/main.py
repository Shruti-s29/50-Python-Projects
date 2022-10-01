# importing libraries

from turtle import Turtle,Screen 
import time 
from snake import *
from food import *
from score import *
# pop up windown / Screen 
scr = Screen()
scr.setup(width=600,height=600)
scr.title("Snack Game By Shruti")
scr.bgcolor('black')
scr.tracer(0)   # Doesn't show any procedure on screen untill update is called

# main code

    #creating Snake body
snk = snake()
    # Food
f = Food()
    # score show on screen 
score = scoreboard()
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
    snk.move_snake()

    # collision with food
    if snk.head.distance(f) < 17:
        f.refresh()
        snk.expand()
        score.update_score()

    # breaking condition 
     # collision with the wall
    if (snk.head.xcor() > 295) or (snk.head.xcor() < -295) or (snk.head.ycor() > 295) or (snk.head.ycor() < -295) :
        game_is_onn = False
        score.game_over()
        
     # collision with its own tail
    for seg in snk.segments[1:]:
        if snk.head.distance(seg) < 5:
            game_is_onn = False
            score.game_over()


#exit
scr.exitonclick()