# write code to import product and customer


# define a Order class with the following fields:
# (1) order_id: a unique order id
# (2) customer: an instance of Customer
# (3) products: a list of Product instances

class Customer:
    def __init__(self, name, id):
        self.name = name
        self.customer_id = id

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"


class Order:

    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []]

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        product_list = ""
        for product in self.products:
            product_
        return f"Order ID: {self.order_id}\nCustomer: {self.customer} (ID: {customer.customer_id})\n



# this class has the following methods:
# (1) add_product(product): add a Producet instance to the order. Products are added only through this method
# (2) __str__: return the order id, customer, and list of produces
#     Example output
#     Order ID: O456
#     Customer: Jane Doe (ID: C123)
#     Products:
#     - Laptop - £999.99
#     - Mouse - £25.99





# When done, 
# (1) create an instance of Customer with your details
# (2) create two instances of Product, any product that you like
# (3) create an instance of Order, with a order_id and the customer you just created
# (4) add the products you have just created to the order
# (5) print(order)
