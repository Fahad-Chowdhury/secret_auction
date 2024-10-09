from art import logo

def main():
    print(logo)
    bids = {}
    choice = 'yes'
    while choice.lower() != 'no':
        name = input("What is your name?: ")
        bid = input("What is your Bid?: $")
        choice = input("Are there any other bidders (yes/no)?: ")
        if bid.isnumeric():
            bids[name] = int(bid)
        print('\n' * 100)
    winner = max(bids, key=bids.get)
    winning_bid = bids[winner]

    print(f'\n\nThe winner is {winner} with a bid of ${winning_bid}')

if __name__ == "__main__":
    main()
