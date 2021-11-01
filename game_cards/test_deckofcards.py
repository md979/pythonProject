from unittest import TestCase
from game_cards.deckofcards import *

class TestDeckofCards(TestCase):
    def setUp(self):
        self.deck = DeckofCards()




    def test_shuffles(self):
        shuffled = []
        for i in range(0,100):
            shuffled.append([i for i in self.deck.cards])
            self.deck.shuffles()
            self.assertNotIn([i for i in self.deck.cards],shuffled)


    def test_del_one(self):
        self.fail()
