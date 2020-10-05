from envelope import Envelope

class N_max_strategy:
    def __init__(self, envelops):
        self.envelops = envelops
        self.N = None

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

envs = []
for i in range(10000000):
    envs.append(Envelope())
stra = N_max_strategy(envs)
stra.N = 100
stra.play()