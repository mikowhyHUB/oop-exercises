class Phone:

    def __init__(self, price):
        self._price = price

    @property
    def get_price(self):
        print('getting...)')
        return self._price


phone = Phone(2000)
phone.__dict__

print(phone._price)
