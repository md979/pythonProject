from unittest import TestCase
from game_cards.game_card import Card

class TestCard(TestCase):
    def setUp(self):
        self.card = Card("4", "hearts")

    def test__init__1(self):
        self.assertEqual(self.card.value, 4)
        self.assertEqual(self.card.suit, "hearts")

    def test__init__2(self):
        self.assertNotEqual(self.card.value,("4","daimonds"))
    def test__int__3(self):
        with self.assertRaises(ValueError):
            self.card.value = Card("-5","spades")

