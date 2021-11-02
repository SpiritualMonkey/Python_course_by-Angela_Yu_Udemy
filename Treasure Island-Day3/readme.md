# Conditional Statements, Logical Opderators, Code Blocks & Scopes


#Control Flow with if / else and Conditional Operators :

conditional if/else

if condition:
	do this
else:
	do this
	
indantation is really importent for python.

Code :

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")
  
  
- Output :

Welcome to the rollercoaster!
What is your height in cm? 120
You can ride the rollercoaster!

== is for comparison.
!= is for not equal to.



- Even/Odd Number :

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

- Nested if statements and elif statements :

if condition:
	if anotherCondition:
		do this
	else:
		do this 
else:
	do this
	
	

 - if/elif 


if condition1:
	do this
elif condition2:
	do this
else:
	do this
	
	
	
# Leap Year Code

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.


- Code :


year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 != 0:
      print("Not leap Year.")
    else:
      print("Leap Year.")
  else:
    print("Leap Year.")
else: 
  print("Not leap Year.")


if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 != 0:
      print("Not leap Year.")
    else:
      print("Leap Year.")
  else:
    print("Leap Year.")
else: 
  print("Not leap Year.")
