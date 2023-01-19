from turtle import *
import random as r
c = ['red','orange','brown','green','white']
w = r.randint(1,2)
l = r.randint(1,3)
ini_move = 5
move_incr = 10

class CarManager():
    def __init__(self):
        self.all_cars =[]
        self.car_speed = ini_move


    def create_car(self):
        rnd_chc = r.randint(1,5)
        if rnd_chc ==1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=w,stretch_len=l)
            new_car.color(r.choice(c))
            x = 320
            y = r.randint(-280,280)
            new_car.goto(x,y)
            new_car.setheading(180)
            # append car
            self.all_cars.append(new_car)
    
        
    def go(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += move_incr