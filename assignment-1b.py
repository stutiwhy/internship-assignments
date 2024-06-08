# temperature conversion tool

def faToCel(fa):
    return (fa - 32) * (5 / 9)

def celToFa(cel):
    return (cel * (9 / 5)) + 32

choice1 = 0
choice2 = 0
res = None

while choice1 != 4:

    print("1. Input temperature")
    print("2. Choose conversion")
    print("3. Display result")
    print("4. Exit")

    choice1 = int(input("Enter choice : "))

    if choice1 == 1:
        temp = float(input("Enter temperature : "))

    elif choice1 == 2:
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        
        choice2 = int(input("Enter choice : "))

        if choice2 not in (1,2):
            print("Invalid choice. Choose a number between 1-2.")
        elif choice2 == 1:
            res = faToCel(temp)
        elif choice2 == 2:
            res = celToFa(temp)
        
    elif choice1 == 3:
        if res is not None:
            print("The result is : %0.2f" %res)
        else:
            print("No conversion performed yet.3")
    
    elif choice1 == 4:
        print("Good bye!")
    
    else:
        print("Invalid choice. Choose a number between 1-4.")