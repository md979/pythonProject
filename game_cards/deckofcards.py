import random
from game_cards.game_card import Card
from random import shuffle

#creat list  or 52 cards 13 of evry value * 4 suit and shuffle the list

class DeckofCards:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,j))
    def shuffles (self):
        random.shuffle(self.cards)


#take acard and delate
    def del_one(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
