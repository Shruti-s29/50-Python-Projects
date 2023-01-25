# this can be used by youngesters to play any dice game by using computer programs
# this will randomly generate dice turn

from turtle import *
import random as r
import time
scr = Screen()
scr.bgcolor("black")
tim = Turtle()
# tim.hideturtle()

flag = True
while flag:
    ans = scr.textinput(title="dice roll generator",prompt="Are you ready ? Type 'Y' or 'N'")
    # time.sleep(1)
    if ans.lower() == 'y':
        r_num = r.randint(1,6)
        print(r_num)
        tim.pencolor('Red')
        tim.pensize(30)
        tim.write(f"Dice roll is - {r_num}", align="center",font= ("Courier", 20, "normal"))
        time.sleep(4)
        
    else:
        print("Bye")
        flag = False
        scr.bye()
        break
    
    scr.clear()
    scr.bgcolor("black")

#exit
