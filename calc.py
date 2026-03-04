def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 6:
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
    elif choice == 4:
        if b != 0:
            print("Result:", div(a, b))
        else:
            print("Division by zero not allowed")
    elif choice == 5:
        print("Result:", mod(a, b))
    else:
        print("Invalid choice")