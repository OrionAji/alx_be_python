class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        return self.price * self.quantity
    Product1 = Product("Laptop", 1000, 5)
    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    print(Product1.get_info())