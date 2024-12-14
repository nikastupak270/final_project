class Offer:
    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price


    def __repr__(self):
        return f'{self.id}: Тур {self.name}, вартість {self.price}'
