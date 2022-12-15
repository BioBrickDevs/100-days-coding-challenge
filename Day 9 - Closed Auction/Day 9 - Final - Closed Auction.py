from replit import clear
import art 
bids = {}
to_continue = True
while to_continue == True:
    clear()
    print(art.logo)


    bidder = input("Your Name: ")
    bid = int(input("How much you will bid?: $"))

    bids[bidder] = bid

   
    more = input("More bidders? yes / no: ")
    if more == "no":
        to_continue = False

max = 0
for name in bids:
    if bids[name] > max:
        max = bids[name]
        winner = name

clear()
print(art.logo)
print(f"The winner is {winner} with bid of ${max}.")
