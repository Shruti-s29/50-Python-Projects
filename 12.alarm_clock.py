from datetime import datetime as dt
from playsound import playsound as pls

I_hour = int(input("Enter hour- "))
I_min = int(input("Enter minute- "))
I_clock = input("am/pm ").lower()

if I_clock == 'pm':       #24 hour time 
    I_hour +=12

while True:
    
    if dt.now().hour == I_hour and dt.now().minute == I_min :
        print("BEEP .. BEEP .. BEEP")
        pls('11.Audio_sample.mp3')
        break
