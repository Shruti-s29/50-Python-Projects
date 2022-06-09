# This is An application where you can find the splitting bill amount 
# also including the tip amount you opt for, among your friends and family.

print("Welcome! This will give you the bill amount each person has to pay\n") 

# Taking Input from the user
total_bill = float(input("Enter the total Bill amount!"))
tip_percent = int(input("What Tip percent would you like to give?\n10,12 or 15?\n"))
people = int(input("How many person you want to split?\n"))

tip = float(total_bill*(tip_percent/100))               #Calculating tip amount from tip percent

new_bill =float(total_bill+tip)                         #estimating new bill according to tip

bill_per_person = float(new_bill/people)                #dividing the new bill equally to every person

print("Each Person should pay- ",bill_per_person)       #Desired output