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
        if isinstance(new_name, str) and len(new_name) >= 3 and not hasattr(self, 'name'):
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

    #name property
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1<= len(new_name) <= 15:
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
        if isinstance(new_price, float) and 1.0 <= new_price <= 10.0 and not hasattr(self, 'price'):
            self._price = new_price
