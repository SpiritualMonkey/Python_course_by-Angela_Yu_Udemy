Distionaries , Nesting and Project : Secret Auction Program 

Distionaries :

{Key: Value}

{"Bug": "An error in a program that prevents the program from running as expected"}

Here Bug is the Key and "An error in a program that prevents the program from running as expected" is the Valuue 

How a dictionary looks like - 

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again."
  }

print(programming_dictionary["Bug"])

OUTPUT :

An error in a program that prevents the program from running as expected.


-----------------
Adding new items to dictionary  :

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  #"Loop": "The action of doing something over and over again."
  }


programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

OUTPUT :

{'Bug': 'An error in a program that prevents the program from running as expected.', 
'Function': 'A piece of code that you can easily call over and over again.', 
'Loop': 'The action of doing something over and over again.'}

#Craete a new empty empty dictionary
empty_dictionary = {}

#Wipe clean an existing dictionary 
programming_dictionary = {}

#Edit/add an item in dictionary 
programming_dictionary["Bug"] = "A moth in your computer"

#Loop through an dictionary

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again."
  }
  
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
  
### if you use for loop to loop through from dictionary then the variable in for loop get the key from the dictionary entities.
  
OUTPUT :

Bug
An error in a program that prevents the program from running as expected.
Function
A piece of code that you can easily call over and over again.
Loop
The action of doing something over and over again. 

------------------------------------------------------------------------------
Grading Program
Instructions
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

CODE -------------


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
  if student_scores[key] >= 91:
    student_grades[key] = "Outstanding"
  elif student_scores[key] <= 90 and student_scores[key] >= 81:
    student_grades[key] = "Exceeds Expectations"
  elif student_scores[key] <= 80 and student_scores[key] >= 71:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

#Don't change the code below 👇
print(student_grades)


-----------------------------

Nesting :

{
"Key1"=[List],
"Key2"={Dictionmary}},
}

Capitals = {
  "France":"Paris",
  "Germany":"Berlin"
}

#Nesting list in a dictionary

travel_log = {
  "France":["Paris","Lille","Dijon"],
  "Germany":["Berlin","Hamburg","Stuttgart"]
}

#Nesting dictionary in a dictionary

travel_log = {
  "France": {
    "cities_visited":["Paris","Lille","Dijon"],"total_visits":12
  },
  "Germany":{
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits":12
  },
}


#Nesting dictionary in a list

travel_log = [
  { "Country_visited":"France",
    "cities_visited":["Paris","Lille","Dijon"],"total_visits":12
  },
  {
    "Country_visited":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits":12
  },
]


# Challenge2 : Dictionary in List

Instructions
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.


CODE ---------


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#�Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_arg,visits_arg,cities_arg):
  country_disc = {}
  country_disc["country"] = country_arg
  country_disc["visits"] = visits_arg
  country_disc["cities"] = cities_arg
  travel_log.append(country_disc)


#�Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


-----------------------------------------------------
