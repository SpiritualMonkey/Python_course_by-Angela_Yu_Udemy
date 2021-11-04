# Randomization and Python List 

## Randomization :

unpridectibility of the code.


## Module :

Python random Module – Generate Random Numbers/Sequences : https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

Python uses Mersenne Twister to generate random numbers-sequences : https://en.wikipedia.org/wiki/Mersenne_Twister

Pseudorandom number generators: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

We have to use "import random" in our code to use the random module which is already created.

CODE :

import random

random_interger = random.randint(1,10)
print(random_interger)

random_float = random.random()
print(random_float)

random_float_below5 = random.random()*5
print(random_float_below5)

OUTPUT : This will generate three outputs : 
1. random interger between 1 and 10
2. random floating number between 0 and 1 , 1 excluded
3. random floating number between 0 and 5 , 5 excluded

We can create our Own module by creating a file with .py extention like my_module.py and the use "import my_module" to use it in the code

CODE :

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲


import my_module

print(my_module.pi)

OUTPUT : this will generate the pi variable value which we have put into our my_module.py

----------------------------------------------------------------------------------------------

### Python List is like arrys 

square bracket is used to carete a list. e.g :

fruits = [item1,item2]

index starts at zero.if you see it like offset then it makes sence.

if you put index as -1 it will start from last.

## Change Iteam :

CODE :

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#to alter 
states_of_america[1] = "Pencilvania"

#to add
states_of_america.append("Angelaland")

#to add a list of entry
states_of_america.extend(["Rohan","Gandu"])

print(states_of_america)

Data Structures Documentation : https://docs.python.org/3/tutorial/datastructures.html



## Random Name Generator :

Convert String to List in Python : https://www.askpython.com/python/string/convert-string-to-list-in-python

Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

CODE :

names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")


import random

random_interger = random.randint(0,4)


print(f"{names[random_interger]} is going to buy the meal today!")


----------------------------------

Treasure Map Code Instructions :


You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']

This is to try and simulate the coordinates on a real map.



Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5

First your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

CODE :

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position1 = int(position[0])-1
position2 = int(position[1])-1

map[position1][position2] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


---------------------------------------

## Rock Paper Scissors

Instructions
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

What are the rules of RPS?
Although the game has a lot of complexity to it, the rules to play it are pretty simple.
The game is played where players deliver hand signals that will represent the elements of the game; rock, paper and scissors. The outcome of the game is determined by 3 simple rules:

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.




