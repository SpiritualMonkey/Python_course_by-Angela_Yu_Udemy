#Number Guessing Game Objectives:

from random import randint
from replit import clear 

HARD_TURNS = 5
EASY_TURNS = 10

turns = 0

def compare(guess,random_num,turns):
  """Checks random_num againts guess. Returns the number of turns remaining"""
  # to access the global turns variable, we have to use "global turns" inside the local function and then change it. It is a bad practice, instaed we can return the constant variable from if-else statement. The code will look like :

  # global turns  
  # if guess > random_num:
  #   print("Too high.")
  #   turns -= 1 
  # elif guess < random_num:
  #   print("Too low.")
  #   turns -= 1 
  # elif guess == random_num:
  #   print(f"You got it! The answer was {random_num}.")

  if guess > random_num:
    print("Too high.")
    return turns-1 
  elif guess < random_num:
    print("Too low.")
    return turns-1
  elif guess == random_num:
    print(f"You got it! The answer was {random_num}.")
  

def difficulty_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  # to access the global turns variable, we have to use "global turns" inside the local function and then change it. It is a bad practice, instaed we can return the constant variable from if-else statement. The code will look like :

  # global turns
  # if level == "easy":
  #   turns = EASY_TURNS
  # elif level == "hard":
  #   turns = HARD_TURNS
  if level == "easy":
    return EASY_TURNS
  elif level == "hard":
    return HARD_TURNS


def game():
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  random_num = randint(1,100)

  #this line is to check/debug the code
  #print(f"Pssst, the correct answer is {random_num}")


  turns = difficulty_level()
  print(f"You have {turns} attempts remaining to guess the number.")
  guess = 0
  while guess != random_num:
    guess = int(input("Make a guess: "))
    turns = compare(guess,random_num,turns)
    print(f"You have {turns} attempts remaining to guess the number.")
    if turns == 0:
      print("You have run out of guess. you lose!")
      return
game()
   





