#THIS clear() FUNCTION ONLY WORKS WITH replit(https://replit.com/~) MODULE, SO IF YOU WANT RUN HEAD OVER TO THE REPLIT WEBSITE

from replit import clear

#HINT: You can call clear() to clear the output in the console.
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

bids = {}

print("Welcome to the secret auction program.")

program_run = True

def find_highest_bidder(bid_dictionary):
  highest_bid = 0
  highest_bidder = ""
  for bidder in bid_dictionary:
    bid_amount = int(bid_dictionary[bidder])
    if bid_amount > highest_bid:
      highest_bid = bid_amount 
      highest_bidder = bidder
  print(f"The highest bidder is {highest_bidder} and the highest bid is ${highest_bid}")

while program_run :
  name = input("What is your name?: ")
  price = input("What's your bid?: $")
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if should_continue == "no":
    clear() 
    find_highest_bidder(bid_dictionary=bids)
    program_run = False
  elif should_continue == "yes":
    clear() 
    





