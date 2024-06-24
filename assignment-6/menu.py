from exceptions import InvalidMenuItemError # importing user defined exception

class MenuItem: # defining class for menu item with each item property initiazed
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu: # class that has all the menu process methods in it
    def __init__(self):
        self.menu_items = [] # creating an empty list to store instances of the MenuItems class

    def read_menu_from_file(self, filename): # method to load menu from file 
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, price, quantity = line.strip().split(',') # extracting the values from the format it is stored in
                    self.menu_items.append(MenuItem(name, float(price), int(quantity))) # adding the menu items from file to menu_items list
            print("Menu loaded from file.")
        except FileNotFoundError: # exception handling
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading menu from file: {e}")

    def add_item(self, name, price, quantity): # method to add item to the menu
        for item in self.menu_items:
            if item.name == name: # if item already exists in the menu, it asks if we want to increase its quantity and by how much
                q_ch = input("Item already in menu, would you like to increase quantity? (y/n) : ").lower()
                if q_ch == 'y':
                    try:
                        n = int(input("By how much? : "))
                        item.quantity += n
                        print("Quantity updated.")
                        return
                    except ValueError: # exception handling
                        print("Invalid input. Quantity not updated.")
                        return
                elif q_ch == 'n':
                    return
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    return
        
        new_item = MenuItem(name, price, quantity)
        self.menu_items.append(new_item) # if item does not exist, new instance is created and appended in the menu_items list
        print(f"Item '{name}' added to the menu.")

    def update_item(self, name, price, quantity): # method to update already existing item
        item_found = False
        for item in self.menu_items:
            if item.name == name:
                item.price = price
                item.quantity = quantity
                print(f"Item '{name}' updated.")
                item_found = True
                break
        if not item_found:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.") # exception handling
        
    def delete_item(self): # method to delete an existing item
        name = input("Enter name of item to be removed : ")
        item_found = False
        for item in self.menu_items:
            if item.name == name:
                self.menu_items.remove(item)
                print(f"Item '{name}' deleted from the menu.")
                item_found = True
                break
        if not item_found:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.") # exception handling
        
    def display_menu(self): # method to display the menu
        if not self.menu_items:
            print("Menu is empty.")
        else:
            for item in self.menu_items:
                print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")

    def write_menu_to_file(self, filename): # method to write all the menu items in a file "menu.txt"
        try:
            with open(filename, "w") as file:
                for item in self.menu_items:
                    file.write(f"{item.name},{item.price},{item.quantity}\n")
            print("Menu saved to file.")
        except Exception as e:
            print(f"Error saving menu to file: {e}")

# menu = Menu()
# menu.read_menu_from_file("menu.txt")  