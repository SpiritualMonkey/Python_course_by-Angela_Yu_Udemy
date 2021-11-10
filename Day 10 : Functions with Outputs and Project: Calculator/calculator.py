#Calculator
from art import logo

#add
def add(n1,n2):
  return n1+n2

#subtract
def subtract(n1,n2):
   return n1-n2

#multiply
def multiply(n1,n2):
   return n1*n2

#divide
def divide(n1,n2):
   return n1/n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  num2 = float(input("What is the second number?: "))

  for key in operations:
    print(key)

  should_continue = True

  while should_continue :
    operation_symbol = input("Pick an operation : ")

    calculation_function = operations[operation_symbol]
    fisrt_result= calculation_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {fisrt_result}")

    should_continue = input(f"Type 'y' to continue calculating with {fisrt_result}, or type 'n' to start a new calculation.")

    if should_continue == "y":
      num1 = fisrt_result
      num2 = int(input("What is your next number?: "))

      # operation_symbol = input("Pick another operation: ")
      # num3 = int(input("What is your next number?: "))
      # calculation_function = operations[operation_symbol]

      # #two ways to write it , first one is optimized and the second one is to show how output of one function can be a input of another function
      # ##second_result= calculation_function(fisrt_result,num3)
      # second_result= calculation_function(calculation_function(num1,num2)
      # ,num3)

      # print(f"{fisrt_result} {operation_symbol} {num3} = {second_result}")
    else:
      should_continue = False
      calculator()

calculator()
