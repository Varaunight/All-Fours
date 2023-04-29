from cards import *

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

p1.print_player()
p2.print_player()
p3.print_player()
p4.print_player()

first = Round(p3)
for player in game_players:
    first.player_play(player)
first.find_winner()


