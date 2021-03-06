from envelope import Envelope
from random import randint


class BaseStrategy:

    def __init__(self, envelope_list):
        self._envelopeList = envelope_list

    def play(self):
        """
        performs the strategy using the object
        param:
            self: the object
        return:
            None
        """
        self.perform_strategy()

    def perform_strategy(self):
        """
        (you is the user)
        This preforms the first strategy,
        that shows you a envelope's stats and you chose if to take it or turn it down,
        and shows you a different one until you chose one or you reached the last envelope.
        param:
            None
        return:
            None
        """

        for x in range(len(self._envelopeList)):
            current_envelope = self._envelopeList[x]
            print("envelope number {0} contains: {1} $".format(x, current_envelope.money))
            current_envelope.used = True
            print("do you want to keep it (Y) or do you want to move on (N)??? \n\n")
            answer = input("Y or N ?")
            if answer == "Y" or answer == "y":
                print("Great")
                print("this is envelope number {0} and it contains: {1} $".format(x, current_envelope.money))
            elif answer == "N" or answer == "n":
                print("Ok, lets move on...")

    def display(self):
        return (
            "This strategy shows you the inside of an envelope, and if you want to keep it you enter the letter 'Y', and if you don't enter 'N'.\n this will go on until you keep a envelope or ran out of new ones.")


# SECOND STRATEGY


class Automatic_BaseStrategy:

    def __init__(self, envelope_list):
        self._envelopeList = envelope_list

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
        number = -1
        while self._envelopeList[number].used or number == -1:
            number = randint(0, 101)

        my_envelope = self._envelopeList[number]
        self._envelopeList[number].used = True

        print(my_envelope.money)

    def display(self):
        return "This strategy chooses a random envelope for you."


# Third strategy


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopelist, percent):
        """
        Args:
            envelopelist:
            percent:
        """
        self.envelopelist = envelopelist
        self.percent = percent

    def perform_strategy(self):
        """
        performs the game
        prints: winning envelope
        Param: The object
        """
        max_money = 0.0
        booli = False
        numofenvelope = int(100 * float(self.percent))
        for i in range(0, abs(
                numofenvelope) - 1):  # goes over the selected number of envelopes and selects the higest prize
            self.envelopelist[i].used = True
            if float(self.envelopelist[i].money) > float(max_money):
                max_money = self.envelopelist[i].money
        for envelope in self.envelopelist:
            if not envelope.used:
                envelope.used = True
                if envelope.money >= max_money:
                    booli = True
                    print("the envelope has:", envelope.money, "$")
                    break
        if not booli:
            print("the envelope has:", self.envelopelist[99].money, "$")  # if there aren't any envelopes left
        for i in range(0, 99):
            self.envelopelist[i].used = False

    def display(self):
        return "Player chooses a percentage of envelopes \n the game opens these envelopes and remembers the amount of money \n Then the game goes over the unopened envelopes and pick a envelope with more money then the maximum "

    def play(self):
        """
        Prints: Envelope
        """
        self.perform_strategy()


# Forth Strategy


class N_max_strategy:
    """
    can run the forth strategy on a set of envelops
    Attributes:
        envelops (list): list of envelops to run the strategy one
        N (int): holds the N for the strategy
    """

    def __init__(self, envelops):
        self.envelops = envelops
        self._N = None

    @property
    def N(self):
        return self._N

    # noinspection PyPep8Naming
    @N.setter
    def N(self, new_n):
        if type(new_n) is int:
            self._N = new_n
        else:
            print('N can only be an integer')

    def display(self):
        return "This is a strategy that opens N - 1 evelopes are are bigger than the first one"

    def play(self):
        """
        performs the strategy using the N and the object
        Args:
            self: the object
        Returns:
            None
        Raises: 
            None
        Warnings:
            self.N must have been set before calling
        """
        self.perform_strategy(self.N)

    def perform_strategy(self, counter):
        """
        perform the forth strategy, that opens envelopes that are bigger with some count
        Args:
            counter (int): how many bigger envelops to open before stopping
        Returns:
            None
        """
        n_biggest = [self.envelops[0]]
        i = 0
        while len(n_biggest) < counter:
            if i == len(self.envelops):
                print('Not enough numbers')
                break
            if self.envelops[i].money > n_biggest[-1].money and not self.envelops[i].used:
                n_biggest.append(self.envelops[i])
            i += 1
        for i in range(len(self.envelops)):
            if self.envelops[i] == n_biggest[-1]:
                self.envelops[i].used = True
                break
        print(str(n_biggest[-1].money))

# envs = []
# for i in range(10000000):
#    envs.append(Envelope())
# stra = N_max_strategy(envs)
# stra.N = 100
# stra.play()
# envs = []
# for i in range(10000000):
#    envs.append(Envelope())
# stra = N_max_strategy(envs)
# stra.N = 100
# stra.play()
