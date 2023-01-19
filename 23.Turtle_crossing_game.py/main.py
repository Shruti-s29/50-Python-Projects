from turtle import *
from add_func import *
from cars import *
from score import *
import time

scr = Screen()
scr.screensize(200,200,'Black')
scr.title('Turtle Crossing')
scr.tracer(0)

tim = Player()
cm = CarManager()
scrb = Scoreboard()

scr.listen()
scr.onkeypress(tim.up,'w')
scr.onkeypress(tim.down,'s')
scr.update()

l = Line()
l.draw_line()
scr.tracer(8,25)


game_is_onn = True
while game_is_onn:
    time.sleep(0.1)
    cm.create_car()
    cm.go()

    # collision with car
    for car in cm.all_cars:
        if car.distance(tim) < 25:
            game_is_onn = False
            scrb.game_over()

    # successful crossing
    if tim.ycor()>290:
        tim.start_again()
        cm.level_up()
        scrb.increase_level()
    
# exit
scr.exitonclick()