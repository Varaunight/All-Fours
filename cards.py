# Cards classes and functions
from colorama import init, Fore, Back, Style
import random

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
        return deck
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

#---------------------------------------------------------------------

class Player():
    def __init__(self, name):
        self.name = name
        # When team_id is negative, the player is not on a team yet
        self.team_id = -1
        self.cards = []

    def print_player(self):
        print(Fore.WHITE + self.name + ", Team " + str(self.team_id) + ":")
        i = 1
        for card in self.cards:
            print(Fore.WHITE + str(i) + ".", end = " ")
            card.print_card()
            i += 1

    def deal_cards(self, deck, num_of_cards):
        i = 1
        while (i <= num_of_cards):
            card = deck.cards.pop()
            self.cards.append(card)
            i += 1


null_player = Player("Null")

#---------------------------------------------------------------------

game_teams = []
game_players = []

class Team():
    def __init__(self, team_id):
        self.team_id = team_id
        self.players = [null_player, null_player]
        self.name = (self.players[0].name + " and " + self.players[1].name)
        self.score = 0
        game_teams.append(self)
    
    @staticmethod
    def add_player(team, player):
        if team.players[0] == null_player:
            team.players[0] = player
            player.team_id = team.team_id
            game_players.append(player)
        else:
            team.players[1] = player
            player.team_id = team.team_id
            game_players.append(player)

#---------------------------------------------------------------------

class Round():
    def __init__(self, first_to_act):
        self.players = game_teams
        self.cards_in_round = []
        self.first_to_act = first_to_act
        self.first_to_act_index = game_players.index(first_to_act)

    def player_play(self, player):
        card_index = (int(input(player.name + ": Please select a card from 1 to " + str(len(player.cards)) + " ")) - 1)
        self.cards_in_round.append(player.cards.pop(card_index))

    def find_winner(self):
        card_values = []
        for card in self.cards_in_round:
            card_values.append(card.value)
        highest_card_index = card_values.index(max(card_values))
        print(game_players[(self.first_to_act_index + highest_card_index) % len(game_players)].name + " is the winner!")

