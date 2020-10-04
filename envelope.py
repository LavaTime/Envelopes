from random import randint


class Envelope:

    def __init__(self):
        self._money = randint(0, 10000)
        self._used = False

    @property
    def money(self):
        return (self._money)

    @property
    def used(self):
        return (self._used)

    @money.setter
    def money(self, money):
        self._money = money

    @used.setter
    def used(self, used):
        self._used = used
