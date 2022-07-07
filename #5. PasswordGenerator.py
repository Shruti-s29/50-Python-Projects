import random as r

#   ----------------- OUTPUT PROMPT -----------
# Making Prompt more attractive---
print("***** Welcome to Password Generator *****")
print("-- To proceed Answer the Following question as your requirements --\n Answer in numeric digits ")
print("*** After answering Tap Enter ***\n")

# taking user input----

#Number of uppercase letters user want in password
up_alpha = int(input("How many Uppercase Characters You want in your password ? (Ex: A,B,C..)\n"))

#Number of lowercase (small) letters user want in password
low_alpha = int(input("How many Lowercase Characters You want in your password ? (Ex: a,b,c..)\n"))

#Number of special characters user want in password
chars = int(input("How many Special Characters You want in your password ? (Ex: !,$,@..)\n"))

# -------- MAIN CODE FOR SOLUTION --------

def password(u,l,sc):           # u - upercase letter , l - lowercase letter , sc - special characters
    
    ans = ""            # the required password
    alpha_small = "abcdefghijklmnopqrstuvwxyz"  #26
    alpha_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    #26
    char = "!@#$%&_"                            # total 7 characters

    for i in range(u):
        k = r.randint(0,25)
        ans = ans + alpha_big[k]

    for i in range(l):
        k = r.randint(0,25)
        ans = ans + alpha_small[k]

    for i in range(sc):
        k = r.randint(0,6)
        ans = ans + char[k]
    lst_ans = list(ans)
    r.shuffle(lst_ans)
    passwrd = "".join(lst_ans)

    return passwrd

# ----------- Calling the solution ---------------
len_psswrd = up_alpha+low_alpha+chars
print(f"-- You have opted for password of length {len_psswrd} --")
ans = password(up_alpha,low_alpha,chars)
print("Your Password is -- \n",ans)