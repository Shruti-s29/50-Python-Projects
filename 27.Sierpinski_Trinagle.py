## A Fascinating Mathematical Structure

#The Sierpinski Triangle Pattern is formed when the midpoint of the sides of an equilateral triangle are connected,
# forming smaller congruent equilateral triangles inside the original triangle. The middle triangle is removed,
#and this process repeated indefinitely. The Sierpinski Triangle has the properties that the area
# tends to zero and the perimeter to infinity as the iterations continue.

# proving and visualizing the phenomenon through my code.

from turtle import *
import random as r

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed('fastest')

scr = Screen()

# function 
def get_new_point(pnt):
    chc = r.choice(l)
    # print("choice",chc)
    new_x = (pnt[0]+chc[0])//2
    new_y = (pnt[1]+chc[1])//2
    new_pnt = (new_x,new_y)
    return new_pnt

# three random points to form a equilateral triangle
A = (-260,0)
B = (0,260)
C = (260,0)

l = [A,B,C]
for i in l:
    tim.goto(i)
    tim.dot(8,'black')

x = r.randint(-260,260)
y = r.randint(0,260)
start_point = (x,y)
tim.goto(start_point)
tim.dot(8,'red')

j = get_new_point(start_point)
tim.goto(j)
tim.dot(8,'red')

for i in range(1000):
    k = get_new_point(j)
    tim.goto(k)
    tim.dot(8,'red')
    j = k

print("Finished")

scr.exitonclick()