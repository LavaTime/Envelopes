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
                envelope.used = (True)
                if envelope.money >= max_money:
                    booli = True
                    print("the envelope has:", envelope.money, "$")
                    break
        if not booli:
            print("the envelope has:", self.envelopelist[99].money, "$")  # if there aren't any envelopes left

    def display(self):
        return "Player chooses a percentage of envelopes \n the game opens these envelopes and remembers the amount of money \n Then the game goes over the unopened envelopes and pick a envelope with more money then the maximum "

    def play(self):
        """
        Prints: Envelope
        """
        self.perform_strategy()