# Read this breakdown of program requirements: http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF



import random
from replit import clear


def blackjack():
  # print(logo) 
  should_run = True

  should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  if should_continue == "n":
    should_run = True

  player_deck= []
  comp_deck = []

  def random_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10, 10]
    card = random.choice(cards)
    return card

  def card_loader(deck,card):
    return deck.append(card)

  def calculate_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
      return 0  
    if 11 in deck and sum(deck) > 21:
      index = deck.index(11)
      deck[index] = 1
    return sum(deck)

  def compare(player_score,comp_score):
    if comp_score == 0:
      return "Lose,oppomemt has a Blackjack"
    elif player_score == 0:
      return "win with a Blackjack"
    elif player_score > 21:
      return "You went over.You lose"
    elif comp_score > 21:
      return "Opponent went over.You win"
    elif player_score == comp_score:
      return "Draw"
    elif player_score > comp_score:
      return "you win"
    else:
      return "you lose"

  for _ in range(2):
    card_loader(player_deck,random_cards())
    card_loader(comp_deck,random_cards())

  while should_run: 

    player_score = calculate_score(player_deck)
    comp_score = calculate_score(comp_deck)
   
    print(f"Your cards: {player_deck}, current score: {player_score}")

    print(f"Computer's first card: {comp_deck[1]}")

    # to test code
    # print(f"Computer's cards: {comp_deck}, current score: {comp_score}")

    if player_score == 0 or comp_score == 0 or player_score > 21:
      should_run = False
    else:
      another_player_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_player_card == "y":
        card_loader(player_deck,random_cards())
      else :
        should_run = False
    
    
   #if you say y then it will add another card in your deck and if you say n then it will carry on with the existing card.

  while comp_score < 16 :
    card_loader(comp_deck,random_cards())
    comp_score = calculate_score(comp_deck)

  
  print(f"Your final hand: {player_deck}, final score: {player_score}")
  print(f"Computer's final hand: {comp_deck}, final score: {comp_score}")
  print(compare(player_score,comp_score))
  
  while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    blackjack()
    

blackjack()
