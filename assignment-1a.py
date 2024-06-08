# basic calculator

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

res = None
choice1 = 0
choice2 = 0

while choice1 != 4:
    print("1. Choose operation")
    print("2. Input numbers")
    print("3. Display result")
    print("4. Exit")
    
    choice1 = int(input("Enter choice : "))

    if choice1 == 1:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice2 = int(input("Enter choice : "))

        if choice2 not in (1, 2, 3, 4):
            print("Invalid choice. Choose a number between 1-4.")

    elif choice1 == 2:
        if choice2 in (1, 2, 3, 4):
            x = float(input("Enter first number : "))
            y = float(input("Enter second number : "))

            if choice2 == 1:
                res = add(x, y)
            elif choice2 == 2:
                res = sub(x, y)
            elif choice2 == 3:
                res = mul(x, y)
            elif choice2 == 4:
                if y == 0:
                    print("Number cannot be divided by 0.")
                else:
                    res = div(x, y)
        else:
            print("Choose an operation first.")

    elif choice1 == 3:
        if res is not None:
            print(f"The result is: {res}")
        else:
            print("No calculation performed yet.")

    elif choice1 == 4:
        print("Good bye!")
    else:
        print("Invalid choice. Choose a number between 1-4.")