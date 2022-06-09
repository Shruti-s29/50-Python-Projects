''' Logic Behind an year to be a leap year is -
        year should be evenly divisible by 4
            except the year should be evenly divisible by 100
                unless the year is evenly divisible by 400
'''
# Have a look at the flowchart for this problem - By below 3 line of code

# from PIL import Image
# im = Image.open(r"Flowchart_leap_year.png")    # open method used to open different extension image file
# im.show()                                      #uncomment this statement to see the flowchart for this problem

year = int(input("Enter year-\n"))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"The year {year} is a Leap year!")
        else:
            print(f"The year {year} is not a Leap year!")
    else:
        print(f"The year {year} is a Leap year!")
        
else:
    print(f"The year {year} is not a Leap year!")