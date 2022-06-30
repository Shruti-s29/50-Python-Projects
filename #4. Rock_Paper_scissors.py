import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

'''Rules of game -
rock wins against scissors
scissors wins against paper
paper wins against rock
'''
def game(x,y):
    
    # Tie conditions   -- return 0
    if (x==y):
        return 0
    elif ((x==0 and y==2) or (x==1 and y==0) or (x==2 and y==1)):
        return 2            # player wins
    else:
        return 1


print("Welcome to the Game --- Rock Paper Scissors \nYour Turn -- Choose any one")
print(" 0 for Rock \n 1 for Paper \n 2 for scissors")

selection =[rock,paper,scissors]

your_sc = 0
comp_sc = 0

for i in range(1,6):
    playerSel = int(input("Your Turn-- \n"))
    compSel = r.randint(0,2)

    print(f"Round--{i}")
    print("Your Choice --\n",selection[playerSel])
    print("Computer's choice --\n",selection[compSel])

    res = game(playerSel,compSel)
    
    if res == 0:
        print("-------Tie !!!-------")
        your_sc,comp_sc = your_sc,comp_sc
    elif res == 2:
        your_sc +=1
        print("-------You Won !!!-------")
    else:
        comp_sc +=1
        print("-------You Lost !!!-------")
    
print("******************************************")
# print(your_sc,comp_sc)
if your_sc > comp_sc:
    print(f"-------Congratulations!------- \n YOU WON !! \n your score is {your_sc}/5")

elif your_sc < comp_sc:
    print(f"-------Better Luck Next Time------- \n YOU LOST !! \n your score is {your_sc}/5")

else:
    print("-------Its a Tie!------- ")

print("*************** Game Ended ************************")