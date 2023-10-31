class Coffee:
    all = []
    def __init__(self, name):
        self.name = name

        type(self).all.append(self)

    #name property
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Name must be a string")
        elif len(new_name) < 3:
            raise Exception("Name must have more than 3 characters")
        elif hasattr(self, 'name'):
            raise Exception("Name cannot be reset")
        else:
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        if len(self.orders()):
            return len(self.orders())
        else:
            return 0

    def average_price(self):
        if len(self.orders()):
            return sum([order.price for order in Order.all if order.coffee is self])/len(self.orders())

class Customer:
    all = []
    def __init__(self, name):
        self.name = name

        type(self).all.append(self)

    #bonus class method
    # @classmethod
    # def most_aficionado(cls, coffee):
    #     top_price = max([order.price for order in Order.all if order.coffee is coffee])
    #     if top_price:
    #         customer_name = next(order.name for order in Order.all if order.price is top_price)
    #         return next(customer for customer in cls.all if customer.name is customer_name)
    #     else:
    #         return None

    #name property
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Name must be a string")
        elif len(new_name) < 1 or len(new_name) > 15:
            raise Exception("Improper length of name")
        else:
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        type(self).all.append(self)

    #customer property
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, cust_class):
        if isinstance(cust_class, Customer):
            self._customer = cust_class

    #coffee property
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, cof_class):
        if isinstance(cof_class, Coffee):
            self._coffee = cof_class

    #price property
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise Exception("Price must be float")
        elif new_price < 1.0 or new_price > 10.0:
            raise Exception("Price not in range")
        elif hasattr(self, 'price'):
            raise Exception("Price cannot be reset")
        else:
            self._price = new_price
