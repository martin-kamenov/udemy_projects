from art import logo

print(logo)

def find_highest_bidder(bidder_dictionary):
    max_bid = -float("inf")
    winner = ''

    for curr_name, bid in bidder_dictionary.items():
        if bid > max_bid:
            max_bid = bid
            winner = curr_name

    print(f"The winner is {winner} with a bid of ${max_bid}")

has_bidders = True
bidders = {}

while has_bidders:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bidders[name] = price

    action = input("Are there any other bidders? Type 'yes' or 'no'.\n  ")

    if action == 'no':
        has_bidders = False
        find_highest_bidder(bidders)
    else:
        print('\n' * 30)
