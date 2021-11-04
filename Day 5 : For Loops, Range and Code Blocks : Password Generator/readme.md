# For Loops, Range and Code Blocks 

Loops for python List 

## LOOP :

for item in list_of_items:
#Do something to each item

## CODE :

fruits = ["Apple","Peach","Orange"]
for fruit in fruits:
  print(fruit)
  
Output :

Apple
Peach
Orange

--------------------------------------------

## Average Height
Instructions
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.


CODE :

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum_of_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_of_height += student_heights[n]
  total_student = n + 1
result = round(sum_of_height/total_student)

print(result)

BY ANGELA :

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)


----------------------------

## Highest Score
Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

CODE :


student_scores = input("Input a list of student scores ").split()


for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)

result = 0
for score in student_scores:
  if score > result:
    result = score
print(f"The highest score in the class is: {result}")


-----------------------------------------------


## Range with for loops 

for number in range(a,b):
	print(number)
	

## Adding Events Execise :


## Adding Evens Coding Challange 
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

CODE ---------

#Write your code below this row 👇

highest_number = int(input("Plaese type the number, untill which you want to add the even numbers?\n"))

list_of_numbers = []
sum_of_even = 0

for n in range(0,highest_number+1):
  if(n%2 == 0):
    list_of_numbers.append(n)
print(list_of_numbers)
for number in list_of_numbers:
  sum_of_even += number
print(sum_of_even)

OR ------------------

#Write your code below this row 👇

highest_number = int(input("Plaese type the number, untill which you want to add the even numbers?\n"))

list_of_numbers = []
sum_of_even = 0

for n in range(0,highest_number+1,2):
  list_of_numbers.append(n)
print(list_of_numbers)
for number in list_of_numbers:
  sum_of_even += number
print(sum_of_even)


---------------------------------

## FizzBuzz

Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`


I have made the code a bit dynamic where you can put your own range.
CODE :

#Write your code below this row 👇

highest_number = int(input("Plaese type the number, untill which you want to do this task?\n"))

list_of_numbers = []

for n in range(1,highest_number+1):
  list_of_numbers.append(n)
print(list_of_numbers)
for number in list_of_numbers:
  if number % 3 == 0 and number % 5 == 0:
    list_of_numbers[list_of_numbers.index(number)] = "FizzBuzz"
  elif number % 3 == 0:
    list_of_numbers[list_of_numbers.index(number)] = "Fizz"
  elif number % 5 == 0:
    list_of_numbers[list_of_numbers.index(number)] = "Buzz"
for number in list_of_numbers:
  print(number)


--------------------
