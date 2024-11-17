class Cart:
    def __init__(self):
        self.list_cart = []

    def add(self, new_product):
        self.list_cart.append(new_product)


    def remove(self, product_name):
        for product in self.list_cart:
            if product_name == product.name:
                self.list_cart.remove(product)



    def view(self):
        return self.list_cart

    def cart_checkout(self):
        suma = 0

        for produs in self.list_cart:
            suma += produs.price
            self.list_cart.remove(produs)
        
        return suma