Day 13 : Debugging 

# Step one : Describe the problem 

## Describe Problem

incorrect :

def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

correct :

## Describe Problem
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

-------------------------------------------------------------
#Step two : Fix the Errors

## Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

correct :

## Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

----------------------------------------------------------------

# Step three :  Play Computer

## Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
  
correct :

## Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

------------------------------------------------------------------------

# Step four : Fix the Errors

## Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

TypeError: '>' not supported between instances of 'str' and 'int'

correct :

## Fix the Errors
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")
  
------------------------------------------------------------------------

# Step five : Print is Your Friend

## Print is Your Friend

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

Output : 0


## Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
print(f"pages = {pages}")
print(f"words_per_pages = {word_per_page}")
total_words = pages * word_per_page
print(total_words)

Output :
Number of pages: 45
Number of words per page: 458
pages = 45
words_per_pages = 0

correct :

## Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(f"pages = {pages}")
print(f"words_per_pages = {word_per_page}")
total_words = pages * word_per_page
print(total_words)

Number of pages: 45
Number of words per page: 345
pages = 45
words_per_pages = 345
15525


---------------------------------------------------------------------------

# step six : Use a Debugger 

## Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

use a debugger and use breakpoints 

--------------------------------------------------------------------------

## Final Tips :

Take a break.

Ask a friend.

Run your code often.

Stackoverflow.



