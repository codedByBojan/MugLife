class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    
    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def resources_available(self, drink):
        """Checking the ingredients for making coffee"""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
            return True
        
    def make_coffee(self, order):
        """Updates the resource levels after preparing a drink."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Coffee magic! ✨ Here is your {order.name} ☕️")
        
    
