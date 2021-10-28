# disaide the valus of the card from the little to the big
class Card:
# the values of the cards and the suits
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s


#chek whats its the bigger card in the round
    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + \
            " of " + \
            self.suits[self.suit]
        return v








