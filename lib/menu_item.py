class MenuItem:
    def __init__(self, item, price):
        if not isinstance(item, str):
            raise TypeError('Item must be a string.')
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be an integer or float.')
        self.item = item
        self.price = price
