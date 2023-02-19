import turtle as t
import pandas as pd
from random_ask import *

scr = t.Screen()
scr.title("Guessing Indian States")
scr.setup(width=800,height=800)
scr.bgcolor('black')
image = '25.Guess_indian_states.py\india_map.gif'
scr.addshape(image)
t.shape(image)
scr.tracer(10)
score = 0
count = 0

while (True):
  ## pointer
  pnt = Pointer()
  # print(visited)

  ## dialog box
  answer_input = scr.textinput(title = f'Score {score} out of {count} | Type exit to end | Blue- Correct | Black- Wrong',prompt='Enter the name of State pointed on map (with red)- Ensure correct spelling')
  ans = answer_input.lower()
  scr.update()
  # print('ans -',ans)

  ## exit condition
  if ans == 'exit':
    scr.bye()
    break

  ## execution
  ## SOLVED BUG- it is not checking whether the state is the same state selected by our random
  print('|actual ans-|',visited[-1])
  ind_s = dict_state['state'].index(visited[-1])
  # print(abbreviation_states[ind_s])

  if abbreviation_states[ind_s]:
  # if ((ans in dict_state['state'] and ans == visited[-1]) or (ans in abbreviation_states[ind_s])):
    if ans in abbreviation_states[ind_s]:
      tick = checkmark(visited[-1])
      score +=1
      count +=1
    else:
      tick = checkmark(ans)
      count +=1

  elif ans in dict_state['state'] and ans == visited[-1]:
      tick = checkmark(visited[-1])
      score +=1
      count +=1
  else:
    tick = checkmark(ans)
    count +=1
  
# final exit
scr.bye()