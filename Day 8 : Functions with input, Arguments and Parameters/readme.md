# Functions with input,Arguments and Parameters & Ceaser Cipher Project :



def my_function():
	#do this
	#then do this
	#finally do this 

-------------

Function with input 


def my_function(something):
	#do this with something
	#then do this
	#finally do this 
	
	
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"Madar {name}")
  print(f"Chod {name}")


greet_with_name("Rohan")

here name is the parameter and Rohan is the argument 

-------------

Positional vs Keyword Arguments

def greet_with(name,location):
   print(f"Hello {name}")
   print(f"What is it like in {location}?")

greet_with("Rohan","Kolkata")
greet_with("Angela","London")

OUTPUT :

Hello Rohan
What is it like in Kolkata?
Hello Angela
What is it like in London?


Positional Argument : we have not specified,which perticular parameter we want associate the data with,so its just gone and looked at the position.

def my_function(a,b,c):
	#do this
	#then do this
	#finally do this 
	
def my_function(1,3,2) then a will be assigned 1 , b = 3 and c =2 	
	
Keyword Argument :



def my_function(a,b,c):
	#do this
	#then do this
	#finally do this 
	
	
def my_function(a=1,b=2,c=3):
	
def greet_with(name,location):
   print(f"Hello {name}")
   print(f"What is it like in {location}?")
   
greet_with(name="Rohan",location="Kolkata")
greet_with(location="Kolkata",name="Rohan",)

OUTPUT :

Hello Rohan
What is it like in Kolkata?
Hello Rohan
What is it like in Kolkata?


-------------------------


Area Calc
Instructions

How do you round UP a number? : https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number


You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5

                     = 1.6
                     = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

CODE-----


#Write your code below this line 👇
import math 

def paint_calc(height,width,cover):
  result = int(math.ceil((height*width)/cover))
  print(f"You'll need {result} cans of paint.")


#Write your code above this line 👆
#Define a function called paint_calc() so that the code below works.   

#Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



---------------------

Prime Numbers
Instructions
Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H

Here are the numbers up to 100, prime numbers are highlighted in yellow:

https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw


CODE ---

#Write your code below this line 👇



def prime_checker(number):
  result = True
  for var in range(2,number):
    if number % var == 0:
      result = False

  if result == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



