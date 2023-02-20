# we will be implementing list and dictionary comprehension in this project.

# we can perform list compehrension for an string type too.
from turtle import *
import pandas as pd

# NATO phonectic alphabets -these are the predefined sequence where it describes every word with example of other ex- A for Alfa

input_user = input('Enter your Name-')
letter = input_user.upper()

# list comprehension
charofInput = [word for word in letter]

# reading dataframe
df = pd.read_csv('26.NATO_alphabet\\nato_phonetic_alphabet.csv')
# print(df)

#dictionary comprehension
dictLetters = {row.letter:row.code for (ind,row) in df.iterrows()}
# print(dictLetters)

# output
ans = [dictLetters[word] for word in charofInput]
print(*ans)
# all nato phonectics are being printed

# exit