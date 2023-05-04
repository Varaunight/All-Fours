# Cards classes and functions
from player import *
import colorama
from colorama import init, Fore, Back, Style
import random
colorama.init(autoreset=True)

#---------------------------------------------------------------------

class Card():
    def __init__(self, suit, name, value, game_value):
        self.suit = suit
        self.name = name
        self.value = value
        self.game_value = game_value

    def print_card(self):
        if self.suit in ["Hearts ♥"]:
            print(Fore.RED + self.name + " of " + self.suit)
        if self.suit in ["Diamonds ♦"]:
            print(Fore.RED + self.name + " of " + self.suit)
        if self.suit in ["Clubs ♣"]:
            print(Fore.LIGHTCYAN_EX + self.name + " of " + self.suit)
        if self.suit in ["Spades ♠"]:
            print(Fore.LIGHTCYAN_EX + self.name + " of " + self.suit)

#---------------------------------------------------------------------

class Deck():
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        random.shuffle(self.cards)

    @staticmethod
    def make_deck():
        deck = Deck()
        for suit in ["Hearts ♥","Clubs ♣","Diamonds ♦","Spades ♠"]:
            for value in range(2,15):
                if (value < 10):
                    deck.cards.append(Card(suit,str(value),value,0))
                if value == 10:
                    deck.cards.append(Card(suit, str(10), value, 10))
                if value == 11:
                    deck.cards.append(Card(suit, "Jack", value, 1))
                if value == 12:
                    deck.cards.append(Card(suit, "Queen", value, 2))
                if value == 13:
                    deck.cards.append(Card(suit, "King", value, 3))
                if value == 14:
                    deck.cards.append(Card(suit, "Ace", value, 4))
        deck.shuffle_deck()
        return deck
    


