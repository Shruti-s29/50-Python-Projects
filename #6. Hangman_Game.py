from Hangman_requirements import stages,logo,word_list
import random as r

print(logo)             # making prompt look attractive
print("******************* Welcome ****************************\n")

# choose a word
word = r.choice(word_list)
word_length = len(word)
#print(word)                debugging purpose

blanks = ["_" for i in range(word_length)]
str = " ".join(blanks)
print(f"|| Guess the word ||-- | {str} |")

life = 7
while life!=0 and "_" in blanks:
    user_guess = input("Enter an alphabet\n").lower()

    if user_guess in blanks:
        print(f"--You have already guessed this letter--")
        continue

    if user_guess in word:
        for i in range(word_length):
            if word[i]==user_guess:
                blanks[i]=user_guess
                str1 = " ".join(blanks)
        print("~~~ You Guessed it right ~~~")
        print("----------------")
        print(f"| {str1} |")
        print("-----------------")
    else:                                       # The guessed letter is not in choosen word
        print("~~~ This letter is not present in the word~~~\n-- Oops!!You loose a life --")
        print(stages[life-1])
        life-=1
    
if life==0 and "_" in blanks:
    print("************You Lost ****************\n*********Game Over*********")

else:
    print("******** You Won ************")

#-----------------------------------------------------------------------