class Phone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"
    
class Smartphone(Phone):
    def __init__(self, brand, model, price, os):
        super().__init__(brand, model, price)
        self.os = os