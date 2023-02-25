# we will be implementing list and dictionary comprehension in this project.

# we can perform list compehrension for an string type too.
from turtle import *
import pandas as pd

# NATO phonectic alphabets -these are the predefined sequence where it describes every word with example of other ex- A for Alfa



# reading dataframe
df = pd.read_csv('nato_phonetic_alphabet.csv')
# print(df)

#dictionary comprehension
dictLetters = {row.letter:row.code for (ind,row) in df.iterrows()}
# print(dictLetters)

## -- Exception Handling
# output
def solution():
    input_user = input('Enter your Name-')
    letter = input_user.upper()

    # list comprehension
    charofInput = [word for word in letter]
    try:
        ans = [dictLetters[word] for word in charofInput]
    except KeyError:
        print("Sorry,only alphabets allowed!")
        solution()
    else:
        print(*ans)
        # all nato phonectics are being printed

    # calling function in main
solution()
# exit