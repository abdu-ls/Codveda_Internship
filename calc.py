 
#Addition function.
def add(x, y):

    return x + y

#Subtraction function.
def subtract(x, y):

    return x - y

#Multiplication function.
def multiply(x, y):

    return x * y
    
#Division function, handles division by zero.
def divide(x, y):

    if y == 0:
        return "Error: you cannot divide by zero!"
    return x / y

print("\n\t***** operations: *****\n")


while True:
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide\n")
    choice = input("select operator (1, 2, 3 or 4):> ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter only numbers.")
            continue

        if choice == '1':
            print(f"Answer: {num1} + {num2} = {add(num1, num2)}\n")
        elif choice == '2':
            print(f"Answer: {num1} - {num2} = {subtract(num1, num2)}\n")
        elif choice == '3':
            print(f"Answer: {num1} * {num2} = {multiply(num1, num2)}\n")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Answer: {num1} / {num2} = {result}\n")
    else:
        print("Invalid input, Please select a valid operation choice with (1, 2, 3 or 4).")

    next_calc = input("**** Another calculation? (yes/no): ")
    if next_calc.lower() != "yes" and next_calc.lower() != "y":
        break
