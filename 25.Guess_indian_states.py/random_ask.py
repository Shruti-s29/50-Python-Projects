import random as r
from turtle import *

# created dataset from creating dataset -- got this-
dict_state = {'state': ['ladakh', 'jammu & kashmir', 'himachal pradesh',
 'punjab', 'uttarakhand', 'haryana', 'uttar pradesh', 'bihar', 'west bengal', 
 'sikkim', 'assam', 'arunachal pradesh', 'nagaland', 'manipur', 'mizoram', 
 'tripura', 'meghalaya', 'jharkhand', 'odisha', 'chhattisgarh', 'telangana',
  'andhra pradesh', 'tamil nadu', 'kerala', 'karnataka', 'goa', 'maharashtra',
   'madhya pradesh', 'gujarat', 'rajasthan', 'delhi'],
   
 'x-cord': [-127.0, -167.0, -118.0, -163.0, -76.0, -141.0, -64.0, 78.0,
  139.0, 140.0, 241.0, 252.0, 284.0, 274.0, 254.0, 225.0, 221.0, 63.0,
   54.0, -10.0, -72.0, -79.0, -82.0, -155.0, -168.0, -210.0, -189.0, -128.0, -259.0, -208.0, -123.0], 

 'y-cord': [319.0, 294.0, 243.0, 217.0, 201.0, 174.0, 126.0, 85.0, 
 19.0, 136.0, 113.0, 149.0, 111.0, 81.0, 44.0, 47.0, 89.0, 31.0, -35.0, 
 -21.0, -109.0, -198.0, -273.0, -313.0, -220.0, -181.0, -81.0, 5.0, 27.0, 115.0, 158.0]}

abbreviation_states = [0, ['jammu and kashmir','j&k','j and k','jammu & kashmir'], ['himachal pradesh','hp'],
 0, ['uttarakhand','uk'], 0, ['uttar pradesh','up'], 0, ['west bengal','bengal','wb'], 
 0, 0, ['arunachal pradesh','ap'], 0, 0, 0, 
 0, 0, 0, 0, 0, 0,['andhra pradesh','ap'], 0, 0, 0, 0, 0,
['madhya pradesh','mp'], 0, 0, ['delhi','new delhi','delhi ncr']]

global visited 
visited = []

class Pointer(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # generating random state for asking
        rand_state = r.choice(dict_state['state'])
        while (rand_state in visited):
          rand_state = r.choice(dict_state['state'])
        # print(rand_state)
        
        visited.append(rand_state)
        ind = dict_state['state'].index(rand_state)
        # print(ind)

        x = dict_state['x-cord'][ind]
        y = dict_state['y-cord'][ind]

        # print(x,y) 
        self.goto(x,y)
        self.dot(10,'red')
        self.pendown()
        
class checkmark(Turtle):
  def __init__(self,state_name):
    super().__init__()
    self.hideturtle()
    
    if state_name == visited[-1]:     # current answer
      ind = dict_state['state'].index(state_name)
      x1 = dict_state['x-cord'][ind]
      y1 = dict_state['y-cord'][ind]
      self.penup()
      self.goto(x1,y1)
      self.dot(20,'blue')
      self.pendown()
    else:                           # wrong answer
      ind = dict_state['state'].index(visited[-1])
      x1 = dict_state['x-cord'][ind]
      y1 = dict_state['y-cord'][ind]
      self.penup()
      self.goto(x1,y1)
      self.dot(20,'black')
      self.pendown()

      


# I WAS TRYING TO CREATE STATE SHAPE TO FILL IN
# def state_shape(state_name):
#   cords = dictStatecords[state_name]
#   myShape = Shape('compound')
#   poly1 = cords
#   myShape.addcomponent(poly= poly1,fill='green',outline='black')
#   register_shape(state_name, myShape)
#   shape(state_name)

# state_shape('ladakh')
# scr = Screen()
# print(scr.getshapes())
# tick = checkmark('ladakh',scr)

# scr.exitonclick()