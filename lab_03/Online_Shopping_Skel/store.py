import cart

class Store:
    def __init__(self, stock):
        self.stock = stock
        self.customer_carts = dict() #! de explicat in enunt: dict(customer_id, cart)

    def login(self, customer_id):
        self.customer_carts[customer_id] = cart.Cart()

    def add_to_cart(self, customer_id, product_name):
        """
        TODO 1:
            * adauga un produs in cart-ul unui cumparator cu id-ul dat
                - daca cumparatorul nu este logat (id-ul lui nu se gaseste
                  in lista), operatia nu se va realiza (cart-ul ramane neschimbat)
            * odata ce un produs a fost adaugat in cart, este sters din stoc
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

            * product_name (str):    numele produslui ce va fi
                                     adaugat in cart    
                                        
        """ 
        if (customer_id not in self.customer_carts):
            print('You must be logged in')
            return 0
        
        for product in self.stock.list_stock:
            if (product.name == product_name):
                self.customer_carts[customer_id].add(product)
                self.stock.list_stock.remove(product)
    
    def remove_from_cart(self, customer_id, product_name):
        if (customer_id not in self.customer_carts):
            print('You must be logged in')
            return 0
        
        for product in self.stock.list_stock:
            if(product.name == product_name):
                self.customer_carts[customer_id].remove(product)
                self.stock.list_stock.remove(product)

    def view_cart(self, customer_id):
        return [(product.name, product.price) for product in self.customer_carts[customer_id].list_cart]
    
    def checkout(self, customer_id):
        return self.customer_carts[customer_id].cart_checkout()

