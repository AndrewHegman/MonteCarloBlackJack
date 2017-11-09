class Agent:
    def __init__(self, is_dealer, chips):
        self.is_dealer = is_dealer
        self.count = 0
        self.current_chips = chips
        self.total_won = 0
        self.total_lost = 0
        self.current_bet = 0
