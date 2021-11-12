#Number Guessing Game Objectives:

import random 

def game():
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  random_num = random.randint(1,100)
  print(f"Pssst, the correct answer is {random_num}")

  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")


  if difficulty_level == "easy":
      attempts_remaining = 10
  elif difficulty_level == "hard":
      attempts_remaining = 5

  while attempts_remaining > 0 :
    guess = int(input("Make a guess: "))
    if guess == random_num:
      print(f"You got it! The answer was {random_num}.")
      attempts_remaining = 0
    elif guess > random_num:
      attempts_remaining -= 1
      print(f"Too high\nGuess again.\nYou have {attempts_remaining} attempts remaining to guess the number.")
      if attempts_remaining == 0:
        print("You lose!")
    elif guess < random_num:
      attempts_remaining -= 1
      print(f"Too low\nGuess again.\nYou have {attempts_remaining} attempts remaining to guess the number.")
      if attempts_remaining == 0:
        print("You lose!")

game()
