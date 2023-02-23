''' For efficient working or studying there is an strategy given as - Pomodoro Strategy 
-> First, start a timer for 25 min
-> work continuosly till the timer stops
-> take 5 mins break
IF these 3 steps have been completed 4 times then take 25-30 minutes break'''
# I will be implementing this algorithm with my python code
# I will be using tkinter module for GUI in this project.

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    cnv.itemconfig(timer_text ,text='0 0  0 0')
    label1.config(text='TIMER')
    checkmark.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    if reps %8 ==0:
        label1.config(text='Long Break')
        countdown(LONG_BREAK_MIN*60)
        
    elif reps %2==0:
        label1.config(text='Short Break')
        countdown(SHORT_BREAK_MIN*60)
            
    else:
        countdown(WORK_MIN*60)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    time_mins = count//60
    time_secs = count%60
    if time_mins<60:
        time_mins ='0 0'
    if time_secs <10:
        time_secs = f'0{time_secs}'
    cnv.itemconfig(timer_text,text=f'{time_mins}   {time_secs}')
    
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=''
        work_session = reps//2
        for _ in range(work_session):
            mark+='✅'
        checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk(screenName="Shruti's")
window.title("Timer For Work Efficiency")
window.config(padx = 100,pady=100,bg='#BFEAF5')
window.minsize(width=150,height=150)

cnv = Canvas(width=348,height=262,bg='#BFEAF5',highlightthickness=0)
timer_img = PhotoImage(file='29.Study_Work_timer_for efficient_working\Timer.png')
cnv.create_image(180,132,image=timer_img)
timer_text = cnv.create_text(155,132,text='0 0 0 0',fill='white',font=(FONT_NAME,20,'bold'))
cnv.grid(column=1,row=1)

label1 = Label(text='TIMER',bg='#BFEAF5',fg='black',font=(FONT_NAME,20,'bold'))
label1.grid(column=1,row=0)

start_button = Button(text='Start',bg='#BFEAF5',fg='black',command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text='Reset',bg='#BFEAF5',fg='black',command=reset_timer)
reset_button.grid(column=2,row=2)

checkmark = Label(fg='green',bg='#BFEAF5')
checkmark.grid(column=1,row=2)


#intact
window.mainloop()