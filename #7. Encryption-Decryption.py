''' This encryption Technique is inspired by Julius Caesar -- He used to encrypt military messages 
    he choose a number and shift all the alphabets to right by the number..
    example - message is - hello -- decided number is 2 
    h--> j | e-->g | l-->n | o-->q   encrypted msg will be "jgnnq"
'''
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# -------------------------Developer -------------------------------------
def encrypt(message,shift_n):
    msg = list(message.split())
    enc_msg = []
    for i in range(len(msg)):
        enc =''
        word = msg[i]
        for j in range(len(word)):
            letter = word[j]
            enc += chr(ord(letter)+shift_n)
        enc_msg.append(enc)

    return " ".join(enc_msg)

def decrypt(message,shift_n):
    msg = list(message.split())
    dec_msg = []
    for i in range(len(msg)):
        dec =''
        word = msg[i]
        for j in range(len(word)):
            letter = word[j]
            dec += chr(ord(letter)-shift_n)
        dec_msg.append(dec)

    return " ".join(dec_msg)

# ------------------ User Prompt --------------------------------

print(logo)
print("-------Welcome to encryption and decryption of message using Caesar Cipher------")
choice = input("What do you want -- to Encrypt or Decrypt message?\n Enter E for encryption and D for decryption\n").upper()

if choice == "E":
    message = input("|| Enter the message you want to encrypt ||\n")
    shift = int(input("|| Enter a number by which you want to shift letters ||\n"))
    ans = encrypt(message,shift)
    print("|| Your Encrypted message is --\n",ans)
    
if choice == "D":
    message = input("|| Enter the message you want to decrypt ||\n")
    shift = int(input("|| Enter a number by which you want to shift letters ||\n"))
    ans1 = decrypt(message,shift)
    print("|| Your Decrypted message is --\n",ans1)