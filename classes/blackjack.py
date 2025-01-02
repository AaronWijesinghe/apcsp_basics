import os
import time
import random
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# ANSI codes for better formatting
bold = "\033[1m"
end = "\033[0m"

class Card:
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit
    
    def display_card(self):
        print(f'  - {self.rank} of {self.suit}')

class Deck:
    def __init__(self):
        self.cards = []
    
    def build_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "A": 11
        }

        for suit in suits:
            for rank, value in ranks.items():
                self.cards.append(Card(rank, value, suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True
    
    def draw_hand(self, deck):
        for dealt_cards in range(2):
            self.hand.append(deck.deal_card())
    
    def display_hand(self):
        print(f"{bold}[This is your hand.]{end}")
        for card in self.hand:
            card.display_card()

    def hit(self, deck):
        self.hand.append(deck.deal_card())
    
    def get_hand_value(self):
        self.hand_value = 0
        ace_count = 0

        for card in self.hand:
            if card.rank == "A":
                ace_count += 1
                self.hand_value += 11
            else:
                self.hand_value += card.value
        
        while self.hand_value > 21 and ace_count > 0:
            self.hand_value -= 10
            ace_count -= 1

        print(f"Hand Value: {self.hand_value}")

    def update_hand(self, deck, game):
        if self.hand_value < 21:
            hit = input("\nDo you want to hit, double down, or stay (y/2x/n)? ").lower().strip()
            if hit.startswith("y"):
                self.hit(deck)
            elif hit.startswith("2x") and game.money >= game.bet * 2:
                game.bet *= 2
                print("")
                self.hit(deck)
                self.playing_hand = False
                self.display_hand()
                self.get_hand_value()
            elif hit.startswith("2x") and game.money < game.bet * 2:
                input("You don't have enough money to double down. ")
            else:
                self.playing_hand = False
        else:
            self.playing_hand = False

class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True
    
    def draw_hand(self, deck):
        for _ in range(2):
            self.hand.append(deck.deal_card())
    
    def display_hand(self):
        print(f"{bold}[This is the dealer's hand.]{end}")
        for card in self.hand:
            card.display_card()
            time.sleep(1)
        self.get_hand_value()

    def hit(self, deck):
        while self.hand_value < 17:
            self.hand.append(deck.deal_card())
            self.get_hand_value(display=False)
        clear()
        print(f"There are {len(self.hand)} cards in the dealer's deck.")
    
    def get_hand_value(self, display=True):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "A":
                ace_in_hand = True
        
        if ace_in_hand:
            self.hand_value -= 10
        if display:
            print(f"Hand Value: {self.hand_value}")

class Game:
    def __init__(self, money):
        self.money = money
        self.bet = 20
        self.winner = ""
    
    def set_bet(self):
        betting = True
        while betting:
            bet = input(f"What is your bet {bold}(MINIMUM of $20){end}? ").replace("$", "")
            try:
                bet = float(bet)
            except:
                print("Invalid bet. Defaulting to a $20 bet.")
                bet = 20

            if bet < 20:
                print("Too low of a bet. Your bet was changed to $20.")
                bet = 20
            
            if bet > self.money:
                clear()
                print("You cannot afford the bet.")
            else:
                self.bet = bet
                betting = False
    
    def scoring(self, player_hand_value, dealer_hand_value):
        if player_hand_value == 21:
            print("You got black jack!")
            self.winner = "p"
        elif dealer_hand_value == 21:
            print("The dealer got black jack!")
            self.winner = "d"
        elif player_hand_value > 21:
            print("You went over 21.")
            self.winner = "d"
        elif dealer_hand_value > 21:
            print("The dealer went over 21.")
            self.winner = "p"
        else:
            if player_hand_value > dealer_hand_value:
                print(f"You had {player_hand_value - dealer_hand_value} more points than the dealer. You won!")
                self.winner = "p"
            elif dealer_hand_value > player_hand_value:
                print(f"The dealer had {dealer_hand_value - player_hand_value} more points than you. You lost.")
                self.winner = "d"
            else:
                print(f"This game ended in a tie.")
                self.winner = "d"
        self.payout()
        print("Press ENTER to bet again, or close this window to take your winnings.")
        input(f"You currently have ${self.money:.2f}. ")
    
    def payout(self):
        if self.winner == "p":
            self.money += self.bet
        elif self.winner == "d":
            self.money -= self.bet
    
    def display_money(self):
        print(f"You currently have ${self.money:.2f}. ")
    
    def display_money_and_bet(self):
        print(f"Money Left: ${self.money:.2f}\nBet: ${self.bet:.2f}")

clear()
print("Welcome to Blackjack!")
print("Gambling Problem? Call 1-800-GAMBLER")
try:
    money = float(input("\nHow much money do you want to put on the table? ").replace("$", ""))
except:
    input("Invalid amount of money. Come back when you're not broke. ")
    raise SystemExit

game = Game(money)
while True:
    clear()
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    player = Player()
    dealer = Dealer()

    game.display_money()
    game.set_bet()

    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    print("")
    game.display_money_and_bet()
    print(f"\n{bold}[This is the dealer's first card.]{end}")
    dealer.hand[0].display_card()

    while player.playing_hand:
        print("")
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck, game)
    input("Your turn is over. ")

    dealer.hit(game_deck)
    print("")
    dealer.display_hand()

    print("")
    game.scoring(player.hand_value, dealer.hand_value)

    if game.money < 20:
        input("You ran out of money. ")
        raise SystemExit