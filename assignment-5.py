import datetime

class Product:
    def __init__(self, name, category, price, quantity, expiration_date):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

    def get_info(self):
        return (self.name, self.category, self.price, self.quantity, self.expiration_date)

    def is_expired(self):
        today = datetime.date.today()
        return self.expiration_date < today

class InventorySystem:
    def __init__(self):
        self.inventory = []
        self.categories = {}

    def add_product(self, product):
        self.inventory.append(product)
        print("Product added.")
        self.categorize_products()

    def remove_product(self, product_name):
        for product in self.inventory:
            if product.name == product_name:
                self.inventory.remove(product)
                print("Product removed.")
                self.categorize_products()
                return
        print("Product not found.")

    def search_products(self, term):
        res = [product for product in self.inventory if term.lower() in product.name.lower() or term.lower() in product.category.lower()]
        if res:
            for product in res:
                x = product.get_info()
                print(f"Name: {x[0]}, Category: {x[1]}, Price: {x[2]}, Quantity: {x[3]}, Expiration Date: {x[4]}")
        else:
            print("No products found.")

    def list_all_products(self):
        if not self.inventory:
            print("No products added yet.")
        else:
            for product in self.inventory:
                x = product.get_info()
                print(f"Name: {x[0]}, Category: {x[1]}, Price: {x[2]}, Quantity: {x[3]}, Expiration Date: {x[4]}")

    def categorize_products(self):
        self.categories = {}
        for product in self.inventory:
            if product.category not in self.categories:
                self.categories[product.category] = []
            self.categories[product.category].append(product)

    def print_by_category(self, category_name):
        if category_name in self.categories:
            print(f"Products in category '{category_name}':")
            for product in self.categories[category_name]:
                x = product.get_info()
                print(f"Name: {x[0]}, Price: {x[2]}, Quantity: {x[3]}, Expiration Date: {x[4]}")
        else:
            print(f"No products found for category '{category_name}'.")

    def check_expired_products(self):
        for product in self.inventory:
            if product.is_expired():
                print(f"Expired product found: {product.name}")
                self.inventory.remove(product)
            else:
                print("No expired product found.")
        self.categorize_products()

    def save_inventory(self, filename):
        try:
            with open(filename, 'w') as file:
                for product in self.inventory:
                    file.write(f"{product.name},{product.category},{product.price},{product.quantity},{product.expiration_date}\n")
            print("Inventory saved to file.")
        except Exception as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory(self, filename):
        try:
            with open(filename, 'r') as file:
                self.inventory = []
                for line in file:
                    name, category, price, quantity, expiration_date = line.strip().split(',')
                    expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
                    self.inventory.append(Product(name, category, float(price), int(quantity), expiration_date))
            self.categorize_products()
            print("Inventory loaded from file.")
        except Exception as e:
            print(f"Error loading inventory from file: {e}")            
inventory_system = InventorySystem()

ch1 = 0

while ch1 != 8:
    print("1. Add product.")
    print("2. Remove product.")
    print("3. Search product.")
    print("4. List all products.")
    print("5. Search categories.")
    print("6. Check for expired products.")
    print("7. Load inventory file.")
    print("8. Exit")

    ch1 = int(input("Enter choice: "))

    if ch1 == 1:
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
        new_product = Product(name, category, price, quantity, expiration_date)
        inventory_system.add_product(new_product)
    
    elif ch1 == 2:
        name = input("Enter product name to remove: ")
        inventory_system.remove_product(name)

    elif ch1 == 3:
        term = input("Enter name or category to search: ")
        inventory_system.search_products(term)
    
    elif ch1 == 4:
        inventory_system.list_all_products()
    
    elif ch1 == 5:
        category = input("Enter category to search: ")
        inventory_system.print_by_category(category)
    
    elif ch1 == 6:
        inventory_system.check_expired_products()
    
    elif ch1 == 7:
        inventory_system.load_inventory('inventory.txt')

    elif ch1 == 8:
        inventory_system.save_inventory('inventory.txt')
        print("Goodbye!")

    else:
        print("Invalid choice. Please enter a number between 1-8.")