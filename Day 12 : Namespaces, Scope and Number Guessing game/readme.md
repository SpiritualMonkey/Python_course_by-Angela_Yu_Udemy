# Namespaces, Scope and Number Guessing game

Scope 

#Local Scope 

def drink_potion():
  potion_strength = 2 
  # potion_strength is local 
  print(potion_strength)

drink_potion()
### print(potion_strength), this line will give an error

#Global Scope 

### player_health is in global scope
player_health = 10

def drink_potion():
  potion_strength = 2 
  #potion_strength is in local scope
  print(player_health)

drink_potion() 
print(player_health)



def game():
  def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion() # this will give "NameError: name 'drink_potion' is not defined",the function is in local scope we cant call outside of its scope


#There is no block scope 

game_level = 3
enemies = ["skeleton","Zombie","Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy) #This is valid code even though this new_enemy variable created inside if statement. 

However the following is not valid code gives error : NameError: name 'new_enemy' is not defined.

game_level = 3
def create_enemy():
  enemies = ["skeleton","Zombie","Alien"]
  if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

### The local scope concent is only aplicable for functions in python and not to loops and if,while etc.


## Modifying Global Scope 

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

-------------------------------------------------

enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


## Avoid modifing global variable 

-----------------------------------

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies+1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

OUTPUT :

enemies inside function: 1
enemies outside function: 2


## Python Global Constant 


### It is better to name the variable in all UPPERCASE which will be constant so then when you use it, it will remind you to not to modify it

PI = 3.14159
URL = "https://www.google.com/"
TWITTER = "dev_ta_ron"

-----------------------------------

What will be printed in the console when the following code is run?

DO NOT run the code, just pretend to be a computer.

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()


ANS : 16 explanation : Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.

----------------------------------
