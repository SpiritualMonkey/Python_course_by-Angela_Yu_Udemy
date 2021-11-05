Python functions, code blocks , while loop & Karel 

Functions :

Syntax : function_name()

We know it is a fuction by seeing the parenthesis at the end of it.

num_char = len("Hello")
print(num_char)

OUTPUT :

5

Createing new function :

def my_function():
	# Do this
	# Then do this
	# Finally do this 
	
Calling the function 

my_function()


Example :

def my_function():
  print("Hello")
  print("Bye")

my_function() 

OUTPUT :

Hello
Bye

Built-in Functions : https://docs.python.org/3/library/functions.html


indentation determines the function blocks.

tabs vs spaces ---

Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code that is already indented with tabs.

Python disallows mixing tabs and spaces for indentation.

Style Guide for Python Code : https://www.python.org/dev/peps/pep-0008/


While Loop --

Syntax --

while something_is_true
    #Do something repeatedly
	
Example --

Reeborg's World :

number_of_hurdles = 6
while number_of_hurdles > 0:
    hurdle_jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
	
	
Reeborg's World :

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

While the wall hight inconsistent in Reeborg's World. 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def  hurdle_jump():
    turn_left()
    while wall_on_right():
        move()   
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
    
while not at_goal():
    if wall_in_front():
        hurdle_jump()
    else:
        move()
		
		
---------------------------
       
