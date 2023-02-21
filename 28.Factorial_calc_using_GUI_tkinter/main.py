# This is a calculator used for calculating factorial of a number 
# but as GUI (graphical user interface) interactive window.
# I have used tkinter module t=of Python to do this.
# In another file named (about_tkinter) I have explained different small widgets to form GUI using tkinter
from tkinter import *

# using functions
def Factorial(num):
    if num<0:
        return -1
    if num == 0 or num==1:
        return 1
    return num*Factorial(num-1)

def show():
    num = int(inp.get())
    ans = Factorial(num)
    label3.config(text=f'{ans}')

# screen /window
wnd = Tk()
wnd.title("Factorial Calculator")
wnd.minsize(width=300,height=300)
wnd.config(padx=20,pady=20)

# Label
label1 = Label(text='Enter a num-',font=('arial',14,'bold'))
label1.grid(column=0,row=0)

#input
inp = Entry()
inp.grid(column=1,row=0)

# Label
label2 = Label(text=f'The factorial is ->',font=('arial',14,'bold'))
label2.grid(column=0,row=1)

label3 = Label(text='0',font=('arial',14,'bold'))
label3.grid(column=1,row=1)

#Button
bnt = Button(text="OKK",bg='grey',fg='red',command=show)
bnt.grid(column=2,row=0)

wnd.mainloop()