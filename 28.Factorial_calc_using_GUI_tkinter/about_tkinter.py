import tkinter as tki

window = tki.Tk()
window.title('My Screen')
window.minsize(width=550,height=550)

## LABEL --
myLabel1 = tki.Label(text='Hello Shruti',font=('Times New Roman',18,'bold'))
myLabel1.pack()      # by default at center , you can change its position by 'side=' argument
# changing label text
myLabel1.config(text='Hii')

myLabel2 = tki.Label(text='Multiline text',font=('Times New Roman',18,'bold'),foreground='red')
myLabel2.pack()

## BUTTON --
# function for button
def do_when_click():
    print("---Clicked---")
    inp = input1.get()          # to get the text received by Entry
    inp2 = input2.get('1.0')
    myLabel1.config(text=inp)
    myLabel2.config(text=inp2)

# formation of button 
button1 = tki.Button(text="Tap Here",command=do_when_click)
button1.pack()

## INPUT --
# ENTRY - single line text input in the window
input1 = tki.Entry(width=20,bg='red')
input1.pack()

# inp = input1.get()
# print(inp)     thier will be no input because it isn's storing till any button linking.

## ---------- More Widgets ---------

# bigger text input (Multiline text input)
input2 = tki.Text(height=5,width=20,bg='blue')
input2.pack()
# getting
# input2.get('1.0')

## SPINBOX --
spinBox = tki.Spinbox(from_= 0, to= 10,bg='yellow',width=5) # command can be used (make a new func to do something)
spinBox.pack()

## SCALE --
tkscale = tki.Scale(from_=0,to=100,bg='pink')
tkscale.pack()

## CHECKBUTTON --
varcheck = tki.IntVar()  # variable storing num, this should be passed in checkbutton class
ckb = tki.Checkbutton(text='I accept all T&C',fg='violet',variable=varcheck)     # button tick box creation 
ckb.pack()

## RADIO BUTTON --
# to be used when we have different options and can chose one option like msq ques.
var1 = tki.IntVar() # only one correct option

rdb1 = tki.Radiobutton(text="option-1",fg='red',variable=var1,value=1)
rdb2 = tki.Radiobutton(text='option-2',fg='red',variable=var1,value=2)
# packing to screen 
rdb1.pack()
rdb2.pack()

## for keeping intact the screen
window.mainloop()


'''Notes -
-> Positioinng the widgets in the screen in 3 ways
-Pack() -> uses 'side' keyword for positioning and is not flexible
-Place() -> uses coordinate system, takes arguments as x and y
-Grid() -> uses matrix system , take argument as column= ,row= , ex-c=0,r=0
'''