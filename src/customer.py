class Customer:
    
    def __init__(self, name, age, wallet, drunkeness_level):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkeness_level = drunkeness_level
       
    def buy_a_drink(self, drink):
        self.wallet -= drink.price

    def increase_alcohol_level(self, drink):
        self.drunkeness_level += drink.alcohol_level
        