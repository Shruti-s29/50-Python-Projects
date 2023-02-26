#global / constants
BACKGROUND_COLOR = "#B1DDC6"
global current_word,ans,flip_timer
current_word,ans = '',''


# libraries used
from tkinter import *
import pandas as pd
import random as r

# ---------------reading dataset (prepared by myself only)---------
data_file = pd.read_csv("31.Flashy_card_for_Hindi_language_learning\Language_dataset.csv")
# print(data_file)
data = data_file.to_dict(orient='records')
# print(data)

# ------------------------ Functions --------------------
def choose_hindi_word():
    global current_word,flip_timer
    window.after_cancel(flip_timer)     # cancelling flip timer as we have entered new word
    current_word = r.choice(data)
    cnv.itemconfig(card_title,text='Hindi',fill='black')
    cnv.itemconfig(card_word,text=current_word['Hindi_Words'],fill='black')
    cnv.itemconfig(card_bgimage,image=front_image)

    flip_timer = window.after(5000,func=flip_card)  # re-initializing

def flip_card():
    global ans
    ans= current_word['English_words']
    cnv.itemconfig(card_title,text='English',fill='white')
    cnv.itemconfig(card_word,text=ans,fill='white')
    cnv.itemconfig(card_bgimage,image=back_image)

# ------------- UI setup ---------------------------------

window = Tk()
window.title("Flashy Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(5000,func=flip_card)


## Card UI

cnv = Canvas(width=800,height=530,bg=BACKGROUND_COLOR,highlightthickness=0)
##-- Back side
back_image = PhotoImage(file='31.Flashy_card_for_Hindi_language_learning\images\card_back.png')
##-- Front side
front_image = PhotoImage(file='31.Flashy_card_for_Hindi_language_learning\images\card_front.png')
card_bgimage = cnv.create_image(409,270,image=front_image)
card_title = cnv.create_text(409,230,text="",font=('Italic',18,'bold'))
card_word = cnv.create_text(409,290,text='',font=("Arial",18,'bold'))
cnv.grid(column=0,row=0,columnspan=2)


## Right - wrong button
r_image = PhotoImage(file='31.Flashy_card_for_Hindi_language_learning\images\\right.png')
r_button = Button(image=r_image,bg=BACKGROUND_COLOR,command=choose_hindi_word)
r_button.grid(column=2,row=2)

w_image = PhotoImage(file='31.Flashy_card_for_Hindi_language_learning\images\wrong.png')
w_button = Button(image=w_image,bg=BACKGROUND_COLOR,command=flip_card)
w_button.grid(column=0,row=2)

# text for question
que =Label(text="Do you know the English Translation of this Hindi Word ?\n Click Yes (Right) or No (Left) \n Answer in 5 seconds",font=("Arial",16,'bold'),bg=BACKGROUND_COLOR)
que.grid(column=1,row=2)


# fro first occurence
choose_hindi_word()

window.mainloop()