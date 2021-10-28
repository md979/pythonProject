from game_cards.deckofcards import DeckofCards
from random import *

class Player:

   def __init__(self, name,numofcards):

       self.cards = []
       self.name = name
       self.numofcards = numofcards

       if self.numofcards< 10 or self.numofcards > 26:
           self.numofcards = 26
       else:
           self.numofcards
   def __str__(self):
        return f"{self.name} numofcards:{self.numofcards}"

   def set_hand(self, deck_of_cards: DeckofCards):
       for i in range(self.numofcards):
           self.cards.append(deck_of_cards.del_one())

   def get_card(self):
       return random.choice(self.cards)

   def add_card(self, card):
       self.cards.append(card)




















