class CustomExceptions(Exception): # because it was mentioned in requirement?
    pass

class InvalidMenuItemError(Exception): # exception which will be raised when the item entered is not found in the menu
    def __init__(self, message="Item not found in the menu."): 
        self.message = message
        super().__init__(self.message)

class InsufficientQuantityError(Exception): # item's quantity is less than the quantity demanded
    def __init__(self, item_name, available_quantity):
        self.item_name = item_name
        self.available_quantity = available_quantity
        super().__init__(f"Insufficient quantity of {item_name}. Available: {available_quantity}")