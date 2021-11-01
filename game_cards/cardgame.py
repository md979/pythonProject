from game_cards.player import Player
from game_cards.deckofcards import *
class Cardgame:
    def __init__(self,name1,name2):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.deck = DeckofCards()
        self.new_game()

    def new_game (self):
        self.deck.shuffles()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)


    def get_winner(self):
        if len(self.player1.cards) > len(self.player2.cards):
            return self.player1
        if len(self.player1.cards) < len(self.player2.cards):
            return self.player2
        return "none"
















