from cards import *
from player import *
from round import *

hearts_3 = Card("Hearts ♥", "3", 3, 0)
hearts_4 = Card("Hearts ♥", "4", 4, 0)
hearts_5 = Card("Hearts ♥", "5", 5, 0)
hearts_6 = Card("Hearts ♥", "6", 6, 0)
hearts_7 = Card("Hearts ♥", "7", 7, 0)
hearts_8 = Card("Hearts ♥", "8", 8, 0)
hearts_9 = Card("Hearts ♥", "9", 9, 0)
hearts_10 = Card("Hearts ♥", "10", 10, 10)
hearts_jack = Card("Hearts ♥", "Jack", 11, 1)
hearts_queen = Card("Hearts ♥", "Queen", 12, 2)
hearts_king = Card("Hearts ♥", "King", 13, 3)
hearts_ace = Card("Hearts ♥", "Ace", 14, 4)

clubs_2 = Card("Clubs ♣", "2", 2, 0)
clubs_3 = Card("Clubs ♣", "3", 3, 0)
clubs_4 = Card("Clubs ♣", "4", 4, 0)
clubs_5 = Card("Clubs ♣", "5", 5, 0)
clubs_6 = Card("Clubs ♣", "6", 6, 0)
clubs_7 = Card("Clubs ♣", "7", 7, 0)
clubs_8 = Card("Clubs ♣", "8", 8, 0)
clubs_9 = Card("Clubs ♣", "9", 9, 0)
clubs_10 = Card("Clubs ♣", "10", 10, 10)
clubs_jack = Card("Clubs ♣", "Jack", 11, 1)
clubs_queen = Card("Clubs ♣", "Queen", 12, 2)
clubs_king = Card("Clubs ♣", "King", 13, 3)
clubs_ace = Card("Clubs ♣", "Ace", 14, 4)

diamonds_2 = Card("Diamonds ♦", "2", 2, 0)
diamonds_3 = Card("Diamonds ♦", "3", 3, 0)
diamonds_4 = Card("Diamonds ♦", "4", 4, 0)
diamonds_5 = Card("Diamonds ♦", "5", 5, 0)
diamonds_6 = Card("Diamonds ♦", "6", 6, 0)
diamonds_7 = Card("Diamonds ♦", "7", 7, 0)
diamonds_8 = Card("Diamonds ♦", "8", 8, 0)
diamonds_9 = Card("Diamonds ♦", "9", 9, 0)
diamonds_10 = Card("Diamonds ♦", "10", 10, 10)
diamonds_jack = Card("Diamonds ♦", "Jack", 11, 1)
diamonds_queen = Card("Diamonds ♦", "Queen", 12, 2)

sA = Card("Spades ♠", "Ace", 14, 4)
sK = Card("Spades ♠", "King", 13, 3)
sQ = Card("Spades ♠", "Queen", 12, 2)
sJ = Card("Spades ♠", "Jack", 11, 1)
s10 = Card("Spades ♠", "10", 10, 10)
s9 = Card("Spades ♠", "9", 9, 0)
s8 = Card("Spades ♠", "8", 8, 0)
s7 = Card("Spades ♠", "7", 7, 0)


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
round1.trump_suit = diamonds_10.suit
lift = Lift(p1, round1)

fivec = Card("Clubs ♣", "5", 5, 0)
tend = Card("Diamonds ♦", "10", 10, 10)
eightd = Card("Diamonds ♦", "8", 8, 0)

lift.add_card(p1, clubs_5)
lift.add_card(p2, s10)
lift.add_card(p3, diamonds_10)


# test all possible scenarios with three cards
print(lift.check_undertrump(diamonds_jack))  # should return False





print(lift.trump_suit)
for card in lift.cards_in_lift:
    card[1].print_card()