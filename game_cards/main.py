from game_cards.game_card import *
from game_cards.player import *
from game_cards.deckofcards import *
from game_cards.cardgame import *


player1_name = input("player1 enter your name: ")
player2_name = (input("player2 enter your name: "))
game = Cardgame(player1_name,player2_name)
for i in range(10):
    player1cards = game.player1.get_card()
    player2cards = game.player2.get_card()
    print(f"{player1_name}: {game.player1.cards}.\n{player2_name}: {game.player2.cards}.")
    if player1cards>player2cards:
        print(f"p1 card: {player1cards}, p2 card: {player2cards}\n{player1_name} wins this round!")
        game.player1.add_card(player1cards)
        game.player1.add_card(player2cards)




    else:
        print(f"{player2_name},{player2cards} wins this round!")
        game.player2.add_card(player1cards)
        game.player2.add_card(player2cards)
if game.get_winner() == game.player1:
    print(f"the winner is {player1_name}")
elif game.get_winner() == game.player2:
    print(f"the winner is {player2_name}")
elif game.get_winner() == "none":
    print("it's a tie")
#10 rands











