bidding = {}
bidding_is_finished = False


def clear():  # Prints 50 blank lines
    print("\n" * 50)

def get_highest_bidder(bidding):
    highest_bid = 0
    winner = ''
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_is_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bidding[name] = price
    will_continue = input("Are there any other bidders, yes or no?: ")
    if will_continue == "yes":
        clear()
    if will_continue == "no":
        bidding_is_finished = True
        get_highest_bidder(bidding)
