logo = r'''
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

bidders = {}

more_bidders = True

while more_bidders:
    name = input("What is your name?")
    amount = int(input("Enter the amount you want to bid:$"))
    bidders[name] = amount
    yes_or_no = input("Are there any other bidders? Type 'yes or 'no'.")
    if yes_or_no == "no":
        more_bidders = False
    elif yes_or_no == "yes":
        print("\n" *100)
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The highest bidder is {winner} with the bid amount ${bid_amount}.")

find_highest_bidder(bidders)