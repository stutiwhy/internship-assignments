# from menu import Menu
from exceptions import InvalidMenuItemError, InsufficientQuantityError

class Order:
    def __init__(self, menu): # initializing class Order with an object of class Menu
        self.menu = menu
        self.order_items = [] # creating empty list for items in the order

    def write_orders_to_file(self, filename): # method to write to (append) the orders made to a file "orders.txt"
        try:
            with open(filename, "a") as file:
                for item in self.order_items:
                    file.write(f"{item["name"]},{item["price"]},{item["quantity"]}\n")
            print("Orders saved to file.")
        except FileNotFoundError: # exception handling
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error saving orders to file: {e}")

    def read_orders_from_file(self, filename): # method to read previous orders from file
        try:
            self.past_orders = [] 
            with open(filename, 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    self.past_orders.append({
                        'name': name,
                        'price': float(price),
                        'quantity': int(quantity)
                    })
            print("Orders loaded from file.")
        except FileNotFoundError: # exception handling
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading orders from file: {e}")

    def add_item(self, name, quantity): # method to add item to order
        item_found = False
        
        for item in self.menu.menu_items:
            if item.name == name:
                if item.quantity >= quantity:
                    self.order_items.append({
                        'name': name,
                        'price': item.price,
                        'quantity': quantity
                    })
                    print(f"{quantity} {name}(s) added to the order.")
                    item.quantity -= quantity
                    item_found = True
                    break
                else:
                    raise InsufficientQuantityError(name, item.quantity) # exception handling
        
        if not item_found:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.")
        if not item_found:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.")

    def take_order(self): # method to take inputs of order items
        ordering = True
        while ordering:
            try:
                name = input("Enter item name: ").title() # title() automatically converts item name format to Item Name Format
                quantity = int(input("Enter quantity: "))
                
                self.add_item(name, quantity)

                while True:
                    add_another = input("Add another item? (y/n): ").lower() # after adding 1 item, it asks if we want to add another, and if we don't then it takes us back to menu
                    if add_another == 'y':
                        break # takes us back to entering item names and all
                    elif add_another == 'n':
                        ordering = False
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
            
            except ValueError: # exception handling
                print("Invalid input. Please enter valid inputs.")
            
            except InsufficientQuantityError as e:
                print(e)

            except InvalidMenuItemError as e:
                print(e)
                break

    def view_current_order(self): # method to view the current order before generating receipt
        if not self.order_items:
            print("No items in order.")
        else:
            for item in self.order_items:
                print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

    def view_past_orders(self, filename): # method to view previous order which reads from the "orders.txt" file
        try:
            with open(filename, 'r') as file:
                print("Past Orders:")
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    print(f"Name: {name}, Price: {price}, Quantity: {quantity}")
                    print("---------------------------")
            print("End of Past Orders.")
        except FileNotFoundError: # exception hand;ing
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading orders from file: {e}")

    def calculate_total(self): # method to calculate the total amount after making an order. this also adds/subtracts taxes and discounts based on if you're an engineer, a woman, or have a pet with you
        try:
            bill = 0.0
            engineer = False
            woman = False
            pet = False

            ch1 = input("Are you an engineer? (y/n) : ").lower()
            if ch1 == 'y':
                engineer = True
                print("We are so sorry to hear that. We regret to inform you that you will have to pay engineer's tax (10%).")
            elif ch1 != 'n':
                print("Invalid input.")

            ch2 = input("Are you a woman? (y/n) : ").lower()
            if ch2 == 'y':
                woman = True
                print("We are thrilled to hear that. You are eligible for our very special Women's discount! (10%)")
            elif ch2 != 'n':
                print("Invalid input.")

            ch3 = input("Do you have a pet with you? (y/n) : ").lower()
            if ch3 == 'y':
                pet = True
                print("We are sorry to say that you'll have to pay pet tax in addition to your bill....\n\n\nJust kidding. You're getting pet discount! (5%)")
            elif ch3 != 'n':
                print("Invalid input.")

            for item in self.order_items:
                price = item['price'] * item['quantity']
                bill += price

            if engineer:
                bill *= 1.1  # 10% engineer tax

            if woman:
                bill *= 0.9  # 10% women's discount

            if pet:
                bill *= 0.95  # 5% pet discount

            return bill # returning the total amount after all discounts and taxes

        except ZeroDivisionError:
            print('No')

    def generate_receipt(self): # generating the receipt of the current order, it calls calculate_total method to calculate amount and then displays it with the order items
        try:
            total_bill = self.calculate_total()
            print("---------------------------")
            for item in self.order_items:
                print(f"{item['name']} : {item['price']} * {item['quantity']}")
            print("---------------------------")
            print(f"Amount payable after discounts : {total_bill:.2f}")
            print("---------------------------")

            self.write_orders_to_file("orders.txt") # automatically appends the order to "orders.txt" file ("places" the order)

            for order_item in self.order_items: # subtracts the quantities mentioned in this order in the menu items
                for menu_item in self.menu.menu_items:
                    if menu_item.name == order_item["name"]:
                        menu_item.quantity -= order_item["quantity"]
                        break

            self.order_items = [] # clears the current order list so new order can be given fresh start?
        
        except ZeroDivisionError: # exception handliung
            print("No")