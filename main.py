import random


CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10,
    "Ace": 11
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return None

class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0

    def add_card(self, deck):
        self.cards.append(deck.deal_card())

    def calculate_score(self):
        total = 0
        total_aces = 0
        for card in self.cards:
            total += CARD_VALUES[card.rank]
            if card.rank == "Ace":
                total_aces += 1

        while total > 21 and total_aces > 0:
            total_aces -= 1
            total -= 10

        return total

class Player:
    def __init__(self, name):
        self.hand = Hand()
        self.chip_count = 1000
        self.name = name



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deck = Deck()
    deck.shuffle_deck()

    player = Player("Player 1")
    dealer = Player("Dealer")

    while len(dealer.hand.cards) < 2:
        player.hand.add_card(deck)
        dealer.hand.add_card(deck)

    print("Player's hand:")

    for card in player.hand.cards:
        print(card)
    print(f"Score: {player.hand.calculate_score()}\n")

    print("Dealer's hand:")
    print("???")
    print(dealer.hand.cards[1])

    if dealer.hand.calculate_score() == 21:
        for card in dealer.hand.cards:
            print(card)
        print("Dealer has won the game!")


    player_choice = input("(H)it, (S)tand").lower()
    player_bust = False

    while player_choice != "s" and player.hand.calculate_score() < 21:
        if player_choice == "h":
            player.hand.add_card(deck)

        for card in player.hand.cards:
            print(card)
        print(f"Score: {player.hand.calculate_score()}\n")

        if player.hand.calculate_score() > 21:
            print("Player bust")
            player_bust = True
            continue

        player_choice = input("(H)it, (S)tand").lower()

    if not player_bust:
        while dealer.hand.calculate_score() < 17:
            dealer.hand.add_card(deck)
            for card in dealer.hand.cards:
                print(card)

            print(f"Score: {dealer.hand.calculate_score()}\n")

        if dealer.hand.calculate_score() > 21:
            print("Dealer bust")
        else:
            if player.hand.calculate_score() > dealer.hand.calculate_score():
                print("Player wins!")
            elif dealer.hand.calculate_score() > player.hand.calculate_score():
                print("Dealer wins!")
            else:
                print("Push")