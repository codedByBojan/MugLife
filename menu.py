class MenuItem:
    """Models each Menu item."""
    def __init__(self, name, cost, ingredients):
        """Initialize name, cost and ingredients for coffee"""
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Display of the coffee menu from the machine"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        available = ""
        for item in self.menu:
            available += f"{item.name}/"
        return available
    
    

