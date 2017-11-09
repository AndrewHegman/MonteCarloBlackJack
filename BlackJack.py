from CardDeck import Deck

card_deck = Deck()
'''
for i in range(card_deck.minimum_rank + (13), card_deck.maximum_rank+1 + 13):
    print(card_deck.number_to_string(i))
'''

hands = card_deck.deal_cards(1)
#print(",".join(card_deck.number_to_string(hands[i][j]) for i in range(2) for j in range(2)))
#print((card_deck.number_to_string(hands[i][j]) for i in range(2) for j in range(2)))
print("Cards in play: " + str(card_deck.cards_in_play))
card_deck.display_current_hands(hands, True)
