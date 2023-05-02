from player import *
from cards import *

# Every round, we make a new deck and shuffle it. That way, the cards can be calculated from the Round class itself,
# instead of the Player class

class Round():
    def __init__(self, first_to_act):
        self.players = game_teams
        self.cards_in_round = []
        self.first_to_act = first_to_act
        self.first_to_act_index = game_players.index(first_to_act)
        self.game_score_team_1 = 0
        self.game_score_team_2 = 0
        self.trump_suit = None
        self.deck = Deck.make_deck()

    def deal_players(self, num_of_cards):
        for player in game_players:
            player.cards = []
            i = 1
            while (i <= num_of_cards):
                card = self.deck.cards.pop()
                player.cards.append(card)
                i += 1

    def kick_card(self):
        trump_card = self.deck.cards.pop()
        self.trump_suit = trump_card.suit
        trump_card.print_card()

    def start_round(self):
        self.kick_card()
        lift = Lift(game_players[0], self)
        while (len(game_players[0].cards) != 0):
            lift.start_lift()
            lift = Lift(lift.find_winner(), self)
            
            


#---------------------------------------------------------------------

class Lift():
    def __init__(self, first_to_act, round):
        self.players = game_teams
        self.cards_in_lift = []
        self.first_to_act = first_to_act
        self.first_to_act_index = game_players.index(first_to_act)
        self.trump_suit = round.trump_suit

    def player_play(self, player):
        print()
        player.print_player()
        card_index = (int(input(player.name + ": Please select a card from 1 to " + str(len(player.cards)) + " ")) - 1)
        while (self.legal_move(player, player.cards[card_index]) != 0):
            if (self.legal_move(player, player.cards[card_index]) == 1):
                print()
                print("[Please play the suit that is called]")
                print()
                player.print_player()
                card_index = (int(input(player.name + ": Please select a card from 1 to " + str(len(player.cards)) + " ")) - 1)
            if (self.legal_move(player, player.cards[card_index]) == 2):
                print()
                print("[You cannot undertrump!]")
                print()
                player.print_player()
                card_index = (int(input(player.name + ": Please select a card from 1 to " + str(len(player.cards)) + " ")) - 1)
        print("[" + player.name + "] played ", end="")
        player.cards[card_index].print_card()
        self.cards_in_lift.append((player,player.cards.pop(card_index)))

    def find_winner(self):
        trumpquestion = False
        for pair in self.cards_in_lift:
            if pair[1].suit == self.trump_suit:
                trumpquestion = True
                break
        if (trumpquestion):
            trump_played = []
            for pair in self.cards_in_lift:
                if pair[1].suit == self.trump_suit:
                    trump_played.append((pair[0], pair[1].value))
                else:
                    trump_played.append((pair[0], 0))
        else:
            trump_played = []
            suit_played = self.cards_in_lift[0][1].suit
            for pair in self.cards_in_lift:
                if pair[1].suit == suit_played:
                    trump_played.append((pair[0], pair[1].value))
                else:
                    trump_played.append((pair[0], 0))
        highest_card_index = trump_played.index(max(trump_played, key=lambda tuple: tuple[1]))
        print()
        print("[" + trump_played[highest_card_index][0].name + "]" + " is the winner!") 
        return trump_played[highest_card_index][0]   
        

    # this function is false if there is no undertrump and true if there is
    def check_undertrump(self, card):
        check = False
        length = len(self.cards_in_lift)
        if (length == 2):
            if (self.cards_in_lift[1][1].suit == self.trump_suit):
                if (card.value < self.cards_in_lift[1][1].value):
                    check = True
        if (length == 3):
            if (self.cards_in_lift[1][1].suit == self.trump_suit and self.cards_in_lift[2][1].suit == self.trump_suit):
                max_value = max(self.cards_in_lift[1][1].value, self.cards_in_lift[2][1].value)
                if (card.value < max_value):
                    check = True
        if (self.cards_in_lift[1][1].suit == self.trump_suit and self.cards_in_lift[2][1].suit != self.trump_suit):
            if (card.value < self.cards_in_lift[1][1].value):
                check = True
        if (self.cards_in_lift[2][1].suit == self.trump_suit and self.cards_in_lift[1][1].suit != self.trump_suit):
            if (card.value < self.cards_in_lift[2][1].value):
                check = True
        return check              

    # this function will return error codes based on the play of the card
    # 0 will be a success: if the card is the first card to be played of the lift
    # 1 will be a failure: if the card played is of the wrong suit that was called
    # 2 will be a failure: if the player tries to undertrump
    def legal_move(self, player, card):
        if (len(self.cards_in_lift) == 0):
            return 0
        else:
            if (card.suit == self.cards_in_lift[0][1].suit):
                return 0
            else:
                if (card.suit == self.trump_suit):
                    if (player.check_flush(self.trump_suit) ==  True):
                        return 0
                    else:
                        if (self.check_undertrump(card) == True):
                            return 2
                        else:
                            return 0
                else:
                    if (player.check_cards(self.cards_in_lift[0][1].suit) == True):
                        return 1
                    else:
                        return 0
                    

    # this is the only command that we need to run for the lift to begin
    def start_lift(self):
        i = 0
        while (i < len(game_players)):
            self.player_play(game_players[(self.first_to_act_index + i) % len(game_players)])
            i += 1

    def add_card(self, player, card):
        self.cards_in_lift.append((player, card))
