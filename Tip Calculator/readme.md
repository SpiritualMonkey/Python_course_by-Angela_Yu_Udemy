# Day 2 : Tip calculator 

If the bill was $150.00, split between 5 people, with 12% tip. 

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

## Take Aways :


Data Types :

There are four data types : String,Integer,Float,Booleans 

String :

index starts from zero of a string.

Code : print("Hello"[0])

output : H 

Subscripting : it stars from zero and by mentioning any index in [] you cabn get the value.

Code : print("Hello"[4])

output : o



Integer :

len() function doesnot work with integer it will give you TypeError: object of type 'int' has no len()

code : print(123+345) 

output : 468

if there is any large number insted osf comma python put underscore Large Number : 123,456,789

python interpretetion : 123_456_789



Float(Decimal Places) : 

when the demical can float from left to right 

Example : Pi(3.14159), random - 4.55, 445.77



Booleans : it has only two values which is True or False 


--------------------------

Type Error,Type Checking , Type Convention :

function type() tells you the type of the variable 

Type Casting/Convention :

str(),float(),int() converts any variable to the mentioned function variable name.If you use int("456") it will covert the string to integer.  

code : 

a = 123

print(type(a))

output : <class 'int'>

Code : 

a = str(123)

print(type(a))

output :  <class 'str'>

------------------------

Mathematical Operations :

when mathematical devition is used then the output is a float. 

** signs is the exponent or to the power

Order of execution : PEMDAS 
P- Parentheses
E- Exponents
M- Multiplication
D- Division
A- Addition
S- Subtraction

-----------------------

Round Function : round(number, digits) -The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

code : print(round(8/3,2))

output : 2.66


print(round(2.6667777,4))

output : 2.6667

The double forward slash in Python is known as the integer division operator. Essentially, it will divide the left by the right, and only keep the whole number component.

Code : 

print(type(8//3))

print(type(8/3))

output :

<class 'int'>
<class 'float'>

YOu can use one variable for multiple purpose :

code :

result = 4/2
result /= 2  # This lines means result = result/2
print(result)

output : 1.0


-------------

Code :

score = 0
height = 1.8
isWinning = True

print("Your score is " + str(score))

# f-string

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")


output :

Your score is 0
Your score is 0, your height is 1.8, you are winning is True

f string,introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings (because of the leading f character preceding the string literal). The idea behind f-strings is to make string interpolation simpler. 
To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format(). F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting. 
 


