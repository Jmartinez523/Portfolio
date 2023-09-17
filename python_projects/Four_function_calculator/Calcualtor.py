#This function adds two numbers
def add(x, y):
    return x+y

#This function subtract two numbers
def subtract(x,y):
    return x-y

#This function Multiply two numbers
def multiply(x,y):
    return x*y

#This function Divide two number
def divide(x,y):
    return x/y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    #check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter Second number: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue
    else:
        print("Please enter the following numbers: 1/2/3/4")
        continue

    if choice == '1':
        print(num1, "+" , num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-" , num2, "=", subtract(num1, num2))
    
    elif choice == '3':
        print(num1, "*" , num2, "=", multiply(num1, num2))

    elif choice == '4':
        if num2 == 0:
            print("You cannot divide by 0.")
            continue
        print(num1, "/" , num2, "=", divide(num1, num2))

    #check if user wants another calculation
    #break the while loop if answer is no
    next_calculation = input("Let's do next Calculation? (Yes/No): ")
    if next_calculation.lower() == "no":
        break
    elif next_calculation.lower() == "yes":
        continue
    else:
        print("Invalid Input")
        break