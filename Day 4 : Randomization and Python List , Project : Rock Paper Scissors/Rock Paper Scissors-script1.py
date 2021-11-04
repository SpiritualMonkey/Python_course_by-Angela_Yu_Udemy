
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

random_interger = random.randint(0,2)

comp_choice = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
  print("You types an invalid number,you lose!")
else:
  print(comp_choice[choice])

  print(f"Computer chose:\n{comp_choice[random_interger]}")

  if comp_choice[random_interger] == rock and choice == 0:
    print("Match is draw")
  elif comp_choice[random_interger] == rock and choice == 1:
    print("Match is draw")
  elif comp_choice[random_interger] == rock and choice == 2:
    print("You have lost the match")
  elif comp_choice[random_interger] == paper and choice == 0:
    print("You have lost the match")
  elif comp_choice[random_interger] == paper and choice == 1:
    print("Match is draw")
  elif comp_choice[random_interger] == paper and choice == 2:
    print("You have won the match")
  elif comp_choice[random_interger] == scissors and choice == 0:
    print("You have won the match")
  elif comp_choice[random_interger] == scissors and choice == 1:
    print("You have lost the match")
  elif comp_choice[random_interger] == scissors and choice == 2:
    print("Match is draw")

