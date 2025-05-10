import random

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price}$ (Кількість: {self.quantity})"

    def purchase(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return self.price * amount
        return None


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product}")

    def sell_random_product(self):
        if not self.products:
            print("У магазині немає товарів.")
            return
        product = random.choice(self.products)
        if product.quantity > 0:
            amount = random.randint(1, product.quantity)
            total_cost = product.purchase(amount)
            print(f"Ви придбали {amount} одиниць {product.name} за {total_cost}$!")
        else:
            print(f"Товар {product.name} закінчився.")


store = Store()
store.add_product(Product("Яблуко", 1.2, 100))
store.add_product(Product("Апельсин", 2.5, 50))
store.add_product(Product("Банан", 1.0, 75))
store.show_products()
store.sell_random_product()
store.show_products()
