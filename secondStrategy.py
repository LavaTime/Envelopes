from envelope import Envelope
from random import randint

class Automatic_BaseStrategy:

    def __init__(self, envelopeList):
        self._envelopeList = envelopeList

    def play(self):
        """
        performs the strategy using the object
        param:
            self: the object
        return:
            Envelope
        """
        self.perform_strategy()

    def perform_strategy(self):
        """
        This preforms the second strategy,
        chooses a random envelope for you.
        param:
            None
        return:
            Envelope
        """
        number = randint(0, 10000)

        myEnvelope = self._envelopeList[number]

        print(myEnvelope)

    def display(self):
        return ("This strategy chooses a random envelope for you.")
