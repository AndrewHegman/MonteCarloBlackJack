import random

class Deck:
    def __init__(self):
        self.cards_in_play = []
        self.number_of_cards = 52
        self.number_of_suits = 4
        self.number_of_ranks = 13
        self.minimum_rank = 1
        self.maximum_rank = 13
        random.seed()

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

        if card_num < 2:
            return -1
        elif card_num < 11:
            return card_num
        elif card_num < 14:
            return 10
        else:
            print("Something went wrong!")

    def deal_cards(self, num_players):
        #hands = [[]]
        hands = [([] * 2) for i in range(num_players + 1)]

        for i in range(num_players + 1):
            hands[i].append(self.draw_card())
            hands[i].append(self.draw_card())
        return hands

    def draw_card(self):
        card = random.randint(self.minimum_rank, self.number_of_cards)
        while card in self.cards_in_play:
            card = random.randint(self.minimum_rank, self.number_of_cards)
        self.cards_in_play.append(card)
        return card

    def display_current_hands(self, hands, show_dealer_all=False):
        for i in range(len(hands)):
            if i == 0:
                print("Dealer:")
                if show_dealer_all:
                    print(",".join(self.number_to_string(hands[0][j]) for j in range(2)), end='')
                    card_sum = self.calculate_sum(hands[i])
                    print(" (" + str(card_sum[0]) + ", " + str(card_sum[1]) + ")") if card_sum[1] != 0 else \
                        print(" (" + str(card_sum[0]) + ")")
                else:
                    print(self.number_to_string(hands[0][0]))
            else:
                print("Player " + str(i) + ":")
                print(",".join(self.number_to_string(hands[i][j]) for j in range(2)), end='')
                card_sum = self.calculate_sum(hands[i])
                print(" (" + str(card_sum[0]) + ", " + str(card_sum[1]) + ")") if card_sum[1] != 0 else \
                    print(" (" + str(card_sum[0]) + ")")
            print("")

    def calculate_sum(self, hand):
        card_sum = 0
        alt_sum = 0     # this is used when an ace is present and can be played as either a 1 or 11
        for i in hand:
            card_val = self.get_card_val(i)
            if card_val > 0:
                card_sum += card_val
            else:
                card_sum += 1
                alt_sum = card_sum + 11
        return [card_sum, alt_sum]

    def reset(self):
        pass