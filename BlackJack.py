from CardDeck import Deck

card_deck = Deck()
for i in range(card_deck.minimum_rank + (13), card_deck.maximum_rank+1 + 13):
    print(card_deck.number_to_string(i))

