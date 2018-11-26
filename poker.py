import sys
from poker_player import PokerPlayer
from poker_game import PokerGame

poker_round = {
    'lines': []
}

for i, line in enumerate(sys.stdin):
    if i != 0:
        poker_round['lines'].append(line.rstrip())

game = PokerGame()
game.add_players(poker_round)
game.print_winners()


