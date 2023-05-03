from cards import *
from player import *
from round import *

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

round1 = Round(p1)
round1.start_round()

# Things still to implement:
# IN terms of game logic:
# beg function
# points for kicking
# only allow legal moves instead of even telling them the error perhaps
# hang jack has to be added
# dealer point if game is tied