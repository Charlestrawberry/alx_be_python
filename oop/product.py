class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    
    
    def stock_value(self):
        
        stock_prod = self.price * self.quantity
        return stock_prod

# create product
book_1 = Product("Python Book", 5, 10)
book_2 = Product("Bible", 13, 10)
book_3 = Product("Clinical book", 15, 10)
book_4 = Product("Guitar book", 11, 10)
book_5 = Product("Law book", 18, 10)

# put the product in a list
products = [book_1, book_2, book_3, book_4, book_5]
total = 0
for product in products:
    total += product.stock_value()

print("Total stock value:", total)

