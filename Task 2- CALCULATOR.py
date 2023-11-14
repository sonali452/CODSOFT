number_1 = float(input('Enter a number :'))
number_2 = float(input('Enter another number :'))

while True:
    User_operation = input ('Enter the operation you want to perform with these numbers(add/subtract/multiply/divide) :')
    User_operation_list = ['add', 'subtract', 'multiply', 'divide']
    if User_operation not in User_operation_list:
            print('you entered the wrong operation')
            print('try again')
    else:
        break

if User_operation == 'add':
    print (number_1 + number_2)
elif User_operation == 'subtract':
    print (number_1 - number_2)
elif User_operation == 'multiply':
    print (number_1 * number_2)
elif User_operation == 'divide':
    print (number_1 / number_2)
else:
    print ('invalid operation!')


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter operation choice (1/2/3/4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation choice. Please enter 1, 2, 3, or 4.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()



