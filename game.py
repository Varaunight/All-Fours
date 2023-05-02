from cards import *
from player import *
from round import *

deck = Deck.make_deck()
Deck.shuffle_deck(deck)

team1 = Team(1)
team2 = Team(2)

p1 = Player("Sooks")
p2 = Player("Phil")
p3 = Player("Avi")
p4 = Player("Loo")

Team.add_player(team1, p1)
Team.add_player(team2, p2)
Team.add_player(team1, p3)
Team.add_player(team2, p4)

for team in game_teams:
    for player in team.players:
        player.deal_cards(deck, 6)
        

# First we initialize a Round where a deck is created and all players are dealt 6 cards
# At this point, game scores for both teams are initailed to 0 in the Round itself.
# this will then be set to their team points after.

# We then kick a card from the deck to initialize the trump suit

# here is where the lift class comes in
# Starting with p1, we initialize play_card() function for all the players.
# We need to setup play card so that it has the undertrump logic
# We then 
#
#
#
#
#
#


round1 = Round(p1)
round1.start_round()
