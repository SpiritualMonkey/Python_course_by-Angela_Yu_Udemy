# Functions with Outputs and Project: Calculator : 


def my_function():
	#do this with something
	#then do this
	#finally do this 
	

my_function()

-------

def my_function(something):
	#do this with something
	#then do this
	#finally do this 
	

my_function(123)

-------


def my_function():
	result = 3*2
	return result
	
	
output = my_function()

-------

def format_name(f_name,l_name):

  #print(f_name.title()+" "+l_name.title()) #This also works

  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  #print(f"{formated_f_name} {formated_l_name}") #This also works 

  #when you put return then it becomes the output of the function in which you are working on.
  return f"{formated_f_name} {formated_l_name}"

#format_name("rohan","basu")

formated_string = format_name("rohan","basu")
print(formated_string)

OUTPUT :

Rohan Basu

#AFTER THE RETURN KEYWORD NO CODE GETS EXECUTED.




---------

# Challenge : Days in Month 
Instructions

In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)

And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.


CODE :

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  if month > 12 or month < 1:
    return "Invalid input"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  year_check = is_leap(year)
  if year_check == True and month == 2:
    return 29
  print(month_days)
  return month_days[month-1]

  
  
#Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# Docstrings:

documentation in python while we are coding 

You have to put the comments in between three pairs of quotation 
You have to use the very first line of your function to do so

Example :

def format_name(f_name,l_name):
  """take a first and last name and format it to return the titelcase version of the string"""
#early return w
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs"

  #print(f_name.title()+" "+l_name.title())

  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  #print(f"{formated_f_name} {formated_l_name}")

  ### when you put return then it becomes the output of the function in which you are working on.
  return f"{formated_f_name} {formated_l_name}"

#format_name("rohan","basu")

formated_string = format_name(input("What is your first name? "),input("What is your last name? "))
print(formated_string)

format_name()


------------

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

OUTPUT :

15

------------


