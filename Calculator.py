# python program to create a simple calculator

# 3 steps to build calculator program
# 1. functions for operations
# 2. user input
# 3. print result

# step-1: create functions:
# Function to addition two numbers
def add(num1,num2):
    return num1 + num2

# Function to subtraction two numbers
def sub(num1,num2):
    return num1 - num2

# Function to multiplication two numbers
def mul(num1,num2):
    return num1 * num2

# Function to division two numbers
def div(num1,num2):
    return num1 / num2

# Function to average two numbers
def avg(num1,num2):
    return (num1 + num2)/2

# step-2: user input
print("please select a operation:\n " \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average")

select = int(input("select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# step-3: print the result:

if select == 1:    
    print(number1, "+", number2, "= ", \
          add(number1, number2))
    
if select == 2:    
    print(number1, "-", number2, "= ", \
          sub(number1, number2))
    
if select == 3:    
    print(number1, "*", number2, "= ", \
          mul(number1, number2))
    
if select == 4:    
    print(number1, "/", number2, "= ", \
          div(number1, number2))
    
if select == 5:    
    print(number1, "+", number2, ")", "/", "2", "= ", \
          avg(number1, number2))
    
else:
    print("Invalid operation! Please select again!")