''' Blind or Silent auction in which bidders don't know the bid prices
 it is only revealed when the max price is obtained
 Here is a simple program for silent auction which mainly uses ~~~~~~Dictionaries~~~~~~~'''

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("---Welcome to the Blind auction---")
player_present = True
dict ={}
while player_present:
    player_name = input("Enter your Name-\n")
    bid = int(input("Enter your biding amount-\n"))
    more_players = input("Are there any more bidders \nType 'Yes' or 'No'\n")
    dict[player_name]=bid
    if more_players == "No":
        player_present = False
        break

max_bid = max(list(dict.values()))

for i in dict.keys():
    if dict[i]==max_bid:
        player_won = i

print("---------------------------------------------------\n~~ Auction Over ! ~~")
print(f"The Winner is || {player_won} || with the bid amount of {max_bid} ||")
print(f"Congratulations {player_won} !! \n-------------------------------------------------------")