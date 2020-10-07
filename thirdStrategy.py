from firstStrategy import BaseStrategy
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
        returns: winning envelope
        Param: The object

        """
        max_money = 0

        for i in range (0, abs(100*self.percent)-1): #goes over the selected number of envelopes and selects the higest prize
            self.envelopelist[i].used(True)
            if self.envelopelist[i].money() > max_money:
                max_money = self.envelopelist
        for envelope in self.envelopelist:
            if not envelope.used():
                envelope.used(True)
                if envelope.money >= max_money:
                    return envelope
        return self.envelopelist[99] #if there aren't any envelopes left
    def display(self):
        print("Player chooses a percentage of envelopes \n the game opens these envelopes and remembers the amount of money")
        print("Then the game goes over the unopened envelopes and pick a envelope with more money then the maximum ")
    def play(self):
        """
        Returns: Envelope
        """
        self.perform_strategy()








