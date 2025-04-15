class Food():
    def __init__(self, name, preparation_method, preparation_time):
        self.name = name
        self.preparation_method = preparation_method
        self.preparation_time = preparation_time
        return name, preparation_method, preparation_time


class Rice(Food):
    def __init__(self):
        super().__init__(name="Rice", preparation_method="Boil", preparation_time=20)

    def __str__(self):
        return f"Name: {self.name}, Preparation Method: {self.preparation_method}, Preparation Time: {self.preparation_time} minutes"


class FrenchFries(Food):
    def __init__(self):
        super().__init__(name="French Fries", preparation_method="Fry", preparation_time=15)
    
    def __str__(self):
        return f"Name: {self.name}, Preparation Method: {self.preparation_method}, Preparation Time: {self.preparation_time} minutes"


class Pizza(Food):
    def __init__(self):
        super().__init__(name="Pizza", preparation_method="Bake", preparation_time=30)

    def __str__(self):
        return f"Name: {self.name}, Preparation Method: {self.preparation_method}, Preparation Time: {self.preparation_time} minutes"
    

class Barbecue(Food):
    def __init__(self):
        super().__init__(name="Barbecue", preparation_method="Grill", preparation_time=60)

    def __str__(self):
        return f"Name: {self.name}, Preparation Method: {self.preparation_method}, Preparation Time: {self.preparation_time} minutes"


print(Rice().preparation_method)
print(FrenchFries().preparation_method)
print(Pizza().preparation_method)
print(Barbecue().preparation_method)