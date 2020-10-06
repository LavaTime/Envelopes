from envelope import Envelope


class BaseStrategy:

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
        (you is the user)
        This preforms the first strategy, 
        that shows you a envelope's stats and you chose if to take it or turn it down,
        and shows you a diffrante one until you chose one or you reached the last envelope.

        param:
            None

        return:
            Envelope

        """

        for x in range(len(self._envelopeList)):
            currentEnvelope = self._envelopeList[x]
            print("envelope number" + x + "contains:" + currentEnvelope.money() + "$")
            currentEnvelope.used(True)
            print("\n do you want to keep it (Y) or do you want to move on (N)??? \n\n")
            answer = input("Y or N ?")
            if (answer == "Y" or answer == "y"):
                print("Great")
                return currentEnvelope
            elif (answer == "N" or answer == "n"):
                print("Ok, lets move on...")


    def display(self):
        print("This strategy shows you the inside of an envelope, and if you want to keep it you enter the letter 'Y', and if you don't enter 'N'.")
        print("\n this will go on until you keep a envelope or ran out of new ones.\n\n")
