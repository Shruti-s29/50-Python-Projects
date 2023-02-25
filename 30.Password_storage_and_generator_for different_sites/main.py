''' This is a password generator and will store you passwords with their individual sites to your local disk
for a safer environment. UI will be build through tkinter module in python.
'''
from tkinter import *
import random as r
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    inp3.delete(0,END)
    special_char = list('!@#$%&')
    alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabets_small = list('abcdefghijklmnopqrstuvwxyz')
    numbers= list('0123456789')
    pswd = ''
    while len(pswd)<10:
        pswd+= str(r.choice(alphabets))
        pswd+= r.choice([r.choice(x) for x in (alphabets, alphabets_small, special_char, numbers)])  # to choose between different lists
    
    # sending password to screen clipboard
    inp3.insert(0,pswd)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #

## _____ standard dialogs in tkinter - POPUPS _________
# working with messagebox - popup
# importing done above, because it is not a class so * can't import it, we have to do this explicitly

def save():
    website = inp1.get()
    username = inp2.get()
    pss = inp3.get()
    new_data = {
        website:{
        'username' : username,
        'password' : pss
        }
    }
    if website =="" or username=="" or pss=="" :
        messagebox.showwarning(title='Warning',message=" Don't leave any field Empty")
    else:
        is_okk = messagebox.askokcancel(title="Details Entered -",message=f'Website : {website} \n Username : {username} \n Password : {pss}')
        if is_okk:
                ## previous technique
            # with open('data.txt','a') as data_file:
            #     data_file.write(f'{website} | {username} | {pss}\n')
              ## implementing exception handling

            # Exception if intially File doesn't exist
            try:
                with open('data.json','r') as data_file:
                    # reading previous data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open('data.json','w') as data_file:
                    # saving data
                    json.dump(new_data,data_file,indent=4)

            else:
                # updating data
                data.update(new_data)
                with open('data.json','w') as data_file:
                    # saving data
                    json.dump(data,data_file,indent=4)
            
            inp1.delete(0,END)
            inp2.delete(0,END)
            inp3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=400,height=400)
window.config(padx=20,pady=20,bg='white')

cnv = Canvas(width=200,height=200,bg='white',highlightthickness=0)
img_file = PhotoImage(file='logo.png')
cnv.create_image(100,95,image=img_file)
cnv.grid(column=1,row=1)

label1= Label(text='Website :',bg='white',fg='black',font=('Arial',10,'bold'))
label1.grid(column=0,row=2)

inp1 = Entry(width=35,borderwidth=2)
inp1.focus()            # start with the cursor ready to type mode
inp1.grid(column=1,row=2)

label2 = Label(text='Email/Username :',bg='white',fg='black',font=('Arial',10,'bold'))
label2.grid(column=0,row=3)

inp2 = Entry(width=35,borderwidth=2)
inp2.grid(column=1,row=3)

label2 = Label(text='Password :',bg='white',fg='black',font=('Arial',10,'bold'))
label2.grid(column=0,row=4)

inp3 = Entry(width=25,borderwidth=2)
inp3.grid(column=1,row=4)

generate_pass = Button(text='Generate',command=pass_generator)
generate_pass.grid(column=2,row=4)

add_pass = Button(text='Add',width=25,command=save)
add_pass.grid(column=1,row=5)


window.mainloop()