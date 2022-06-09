# This is an application which produces a band name for your pet based on the city you grew up and your pet's name.

print("Welcome! This is Band Name Generator\n")                               #greeting message
city = input("Enter the name of city where you grew up?\n")                   #asking user for the city where they grew up
pet_name = input("What's your pet name?\n")                                   #asking user for their pet's name

band_name = city+"'s"+" "+pet_name                                            #String Concatination
print("Your Pet's Band name can be- ",band_name)