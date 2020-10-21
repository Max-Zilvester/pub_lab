class Pub:
    
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        #self.drinks is a dict of stock level
        self.drinks = drinks

    def sell_a_drink(self, drink, customer):
        if customer.age >= 18 and customer.drunkeness_level < 15:
            self.till += drink.price

    def stock_total_value(self, drink):
        total_value = 