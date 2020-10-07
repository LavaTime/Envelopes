from envelope import Envelope


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

    @N.setter
    def N(self, newN):
        if newN is int:
            self._N = newN
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
        n_biggest = [self.envelops[0].money]
        i = 0
        while len(n_biggest) < counter:
            if i == len(self.envelops):
                print('Not enough numbers')
                break
            if self.envelops[i].money > n_biggest[-1]:
                n_biggest.append(self.envelops[i].money)
            i += 1
        print(str(n_biggest))


#envs = []
#for i in range(10000000):
#    envs.append(Envelope())
#stra = N_max_strategy(envs)
#stra.N = 100
#stra.play()
