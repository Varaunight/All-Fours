from cards import *

class Player():
    def __init__(self, name):
        self.name = name
        # When team_id is negative, the player is not on a team yet
        self.team_id = -1
        self.cards = []

    def print_player(self):
        print(self.name + ", Team " + str(self.team_id) + ":")
        i = 1
        for card in self.cards:
            print(str(i) + ".", end = " ")
            card.print_card()
            i += 1

    def deal_cards(self, deck, num_of_cards):
        i = 1
        while (i <= num_of_cards):
            card = deck.cards.pop()
            self.cards.append(card)
            i += 1

    def check_cards(self, suit):
        check = False
        for card in self.cards:
            if (card.suit == suit):
                check = True
                break
        return check
    
    def check_flush(self, suit):
        check = True
        for card in self.cards:
            if (card.suit != suit):
                check = False
                break
        return check


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