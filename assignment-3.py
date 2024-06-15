class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category
    
    def get_info(self):
        return (self.vehicle_id, self.make, self.model, self.year, self.category)

class RentalSystem:
    def __init__(self):
        self.rental = []
        self.rset = set()
        self.categories = {}

    def add_vehicle(self, vehicle):
        if vehicle.vehicle_id not in self.rset:
            self.rental.append(vehicle)
            self.rset.add(vehicle.vehicle_id)
            print("Vehicle added.")
        else:
            print("Vehicle with that ID already exists.")
    
    def remove_vehicle(self, vehicle_id):
        for vehicle in self.rental:
            if vehicle.vehicle_id == vehicle_id:
                self.rental.remove(vehicle)
                self.rset.remove(vehicle_id)
                print("Vehicle removed.")
                return
        print("Vehicle not found.")
    
    def search_vehicles(self, term):
        res = [vehicle for vehicle in self.rental if term.lower() in vehicle.make.lower() or term.lower() in vehicle.model.lower()]
        if res:
            for vehicle in res:
                x = vehicle.get_info()
                print(f"ID : {x[0]}, Make : {x[1]}, Model : {x[2]}, Year : {x[3]}, Category : {x[4]}")         
        else:
            print("No vehicles found.")

    def list_vehicles(self):
        if not self.rental:
            print("No vehicles added yet.")
        else:
            for vehicle in self.rental:
                x = vehicle.get_info()
                print(f"ID : {x[0]}, Make : {x[1]}, Model : {x[2]}, Year : {x[3]}, Category : {x[4]}")

    def categorize_vehicles(self):
        for vehicle in self.rental:
            if vehicle.category not in self.categories:
                self.categories[vehicle.category] = []
            self.categories[vehicle.category].append(vehicle)
        return self.categories
    
    def print_by_category(self, category_name):
        if category_name in self.categories:
            print(f"Vehicles in category '{category_name}':")
            for vehicle in self.categories[category_name]:
                x = vehicle.get_info()
                print(f"ID : {x[0]}, Make : {x[1]}, Model : {x[2]}, Year : {x[3]}")
        else:
            print(f"No vehicles found for category '{category_name}'.")


rental_system = RentalSystem()

ch1 = 0

while ch1 != 6:
    print("1. Add vehicle.")
    print("2. Remove vehicle.")
    print("3. Search vehicle.")
    print("4. List all vehicles.")
    print("5. Search categories.")
    print("6. Exit")

    ch1 = int(input("Enter choice : "))

    if ch1 == 1:
        vehicle_id = input("Enter vehicle ID: ")
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        category = input("Enter category: ")
        new_vehicle = Vehicle(vehicle_id, make, model, year, category)
        rental_system.add_vehicle(new_vehicle)
        rental_system.categorize_vehicles()
    
    elif ch1 == 2:
        vehicle_id = input("Enter vehicle ID to remove: ")
        rental_system.remove_vehicle(vehicle_id)

    elif ch1 == 3:
        term = input("Enter make or model to search: ")
        rental_system.search_vehicles(term)
    
    elif ch1 == 4:
        rental_system.list_vehicles()
    
    elif ch1 == 5:
        term = input("Enter category to search : ")
        rental_system.print_by_category(term)
    
    elif ch1 == 6:
        print("Good bye !")
        
    else:
        print("Invalid choice. Please enter a number between 1-6.")
