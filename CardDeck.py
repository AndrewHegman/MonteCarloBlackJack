class Deck:
    def __init__(self):
        self.cards_in_play = []
        self.number_of_cards = 52
        self.number_of_suits = 4
        self.number_of_ranks = 13
        self.minimum_rank = 1
        self.maximum_rank = 13

    def number_to_string(self, number):
        suit = ""
        if number < 14:
            suit = "S"
        elif number < 27:
            suit = "H"
            number -= 13
        elif number < 40:
            suit = "D"
            number -= 26
        elif number < 53:
            suit = "C"
            number -= 39

        if number > 1 and number < 11:
            return str(number) + suit
        elif number == 1:
            return "A" + suit
        elif number == 11:
            return "J" + suit
        elif number == 12:
            return "Q" + suit
        elif number == 13:
            return "K" + suit

    def get_card_val(self, card_num):
        if card_num > 14 and card_num < 27:
            card_num -= 13
        elif card_num < 40:
            card_num -= 26
        elif card_num < 53:
            card_num -= 39

    def deal_cards(self, num_players):
        pass