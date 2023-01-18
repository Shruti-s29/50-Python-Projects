from turtle import *
from display import *
from moves import *
from paddle import *
import time

#all output screen modifications
scr = Screen()
scr.screensize(400,400,'black')
# print(scr.screensize())
scr.title("Bounching Ball")
scr.tracer(0)
disp = Display()        

r_pd = Paddle((250,0))
l_pd = Paddle((-250,0))

ball = Ball()

scrb = Scoreboard()


scr.listen()
scr.onkeypress(r_pd.go_up,'Up')
scr.onkeypress(r_pd.go_down,'Down')
scr.onkeypress(l_pd.go_up,'w')
scr.onkeypress(l_pd.go_down,'s')
# I have noted that 
# object method calling should not be followed by brackets.

game_onn = True
while game_onn:
    time.sleep(0.1)        # to slow down our ball
    scr.update()
    ball.move()
        
    #Detect collision with wall
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    #detect collision with paddle:
    r_condition = ball.distance(r_pd) < 40 and ball.xcor()<230
    l_condition = ball.distance(l_pd) < 40 and ball.xcor()<-230
    
    if r_condition or l_condition:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scrb.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scrb.r_point()
    
#exit 
scr.exitonclick()