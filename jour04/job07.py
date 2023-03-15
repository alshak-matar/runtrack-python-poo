import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    
    def __repr__(self):
        return f"{self.value} of {self.color}"

class Game:
    def __init__(self):
        self.deck = []
        self.players = []
        self.dealer = []
        self.create_deck()
    
    def create_deck(self):
        colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for color in colors:
            for value in values:
                card = Card(value, color)
                self.deck.append(card)
        random.shuffle(self.deck)
    
    def add_player(self, player_name):
        self.players.append({'name': player_name, 'hand': []})
    
    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                card = self.deck.pop()
                player['hand'].append(card)
            card = self.deck.pop()
            self.dealer.append(card)
    
    def get_card_value(self, card):
        if card.value in ['Jack', 'Queen', 'King']:
            return 10
        elif card.value == 'Ace':
            return 11
        else:
            return int(card.value)
    
    def calculate_hand_value(self, hand):
        value = 0
        for card in hand:
            value += self.get_card_value(card)
        return value
    
    def display_hand(self, hand):
        for card in hand:
            print(card)
    
    def play_game(self):
        self.add_player('Player')
        self.deal_cards()
        player_hand = self.players[0]['hand']
        dealer_hand = self.dealer
        print("Dealer's hand:")
        print(dealer_hand[0])
        print("Player's hand:")
        self.display_hand(player_hand)
        while True:
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == 'hit':
                card = self.deck.pop()
                player_hand.append(card)
                self.display_hand(player_hand)
                if self.calculate_hand_value(player_hand) > 21:
                    print("Bust! You lose.")
                    return
            else:
                break
        dealer_value = self.calculate_hand_value(dealer_hand)
        while dealer_value < 17:
            card = self.deck.pop()
            dealer_hand.append(card)
            dealer_value = self.calculate_hand_value(dealer_hand)
        print("Dealer's hand:")
        self.display_hand(dealer_hand)
        player_value = self.calculate_hand_value(player_hand)
        if player_value > 21:
            print("Bust! You lose.")
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win!")
        elif dealer_value > player_value:
            print("Dealer wins.")
        else:
            print("It's a tie.")
game = Game()
game.play_game()
