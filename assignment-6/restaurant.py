from menu import Menu # importing all necessary classes from the other files
from order import Order
from exceptions import InvalidMenuItemError

menu = Menu() # instance of Menu class being created
order = Order(menu) # instance of Order class passing instance of menu class as parameter to access methods of menu class during orderning process
menu.read_menu_from_file('menu.txt') # reading menu file
order.read_orders_from_file('orders.txt') # reading order file

ch1 = 0
while ch1 != 3:
    print("1. Menu")
    print("2. Orders")
    print("3. Exit")
    ch1 = int(input("Enter choice : "))

    if ch1 == 1: # entering menu management
        ch2 = 0
        while ch2 != 5:
            print("1. Add item to menu.")
            print("2. Update item in menu.")
            print("3. Remove item from menu.")
            print("4. View menu.")
            print("5. Exit")
            ch2 = int(input("Enter choice : "))

            if ch2 == 1:
                name = input("Enter item name : ").title() # title() automatically converts item name format to Item Name Format
                price = float(input("Enter price : "))
                quantity = int(input("Enter available quantity : "))
                menu.add_item(name, price, quantity)

            elif ch2 == 2:
                name = input("Enter updated name : ").title()
                price = float(input("Enter updated price : "))
                quantity = int(input("Enter updated quantity : "))
                try:
                    menu.update_item(name, price, quantity)    
                except InvalidMenuItemError as e: # exception handling
                    print(e)

            elif ch2 == 3:
                try:
                    menu.delete_item()
                except InvalidMenuItemError as e: # exception handling
                    print(e)

            elif ch2 == 4:
                menu.display_menu()

            elif ch2 == 5:
                menu.write_menu_to_file('menu.txt')
                print("Exiting menu management.")

            else:
                print("Invalid choice. Please choose a number between 1-5.")

    elif ch1 == 2: # entering order management
        ch3 = 0
        while ch3 != 5:
            print("1. Place new order.")
            print("2. View current order.")
            print("3. Generate receipt and place order.")
            print("4. View past orders.")
            print("5. Exit")
            ch3 = int(input("Enter choice: "))

            if ch3 == 1:
                order.take_order()

            elif ch3 == 2:
                order.view_current_order()

            elif ch3 == 3:
                order.generate_receipt()

            elif ch3 == 4:
                order.view_past_orders("orders.txt") # passing the file name to read as argument

            elif ch3 == 5:
                print("Exiting order management.")

            else:
                print("Invalid choice. Enter a number between 1-5.")

    elif ch1 == 3:
        print("Good bye !") # adios
        break

    else:
        print("Invalid choice. Enter a number between 1-4.")
