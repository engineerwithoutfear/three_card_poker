from poker_tables import card_table, score_table
from poker_player import PokerPlayer


class PokerGame():

    def __init__(self):

        self.players = []
        self.winners = ''

    def add_players(self, round):

        for line in round['lines']:
            player = PokerPlayer(line[0])
            player.set_hand(line.split(' ')[1:])
            self.players.append(player)

    def score_round(self, players):

        results = []
        winningest = {}

        for player in players:

            score_lookup = score_table.index(str(player.score))

            if score_lookup in winningest:
                winningest[score_lookup].append(player)
            else:
                winningest[score_lookup] = [player]

        top_score = sorted(list(winningest.keys()))[0]

        if len(winningest[top_score]) is not 1:
            results = self.resolve_ties(
                winningest[top_score], top_score, score_table.index('Pair'))
        else:
            results = [winningest[top_score][0].id]

        winners = [str(id) for id in sorted(results)]

        return ' '.join(winners)

    def resolve_ties(self, players, score, pair_index):

        winners = []

        # if highest scoring hands are a pair
        if score == pair_index:
            winners = self.break_pair_tie(players,
                                          score, pair_index)

        # for all other cases:
        else:
            # if the highest cards are equal, then the second highest cards should be compared.
            # if those are equal, then the third highest cards should be compared.
            # if all three are equal, then the hands are tied.
            level = 'first_highest'

            while True:

                cards = []
                for player in players:
                    if level == 'first_highest':
                        cards.append([player.first_highest, player.id])
                    elif level == 'second_highest':
                        cards.append([player.second_highest, player.id])
                    else:
                        cards.append([player.third_highest, player.id])

                cards.sort()
                cards.reverse()

                players_with_max_value, max_value = [cards[0][1]], cards[0][0]

                for i in range(1, len(cards)):
                    if cards[i][0] == max_value:
                        players_with_max_value.append(cards[i][1])

                # if a single winner has been found or all three cards were determined to be equal
                if len(players_with_max_value) == 1 or level == 'third_highest':
                    winners = players_with_max_value
                    break

                # else compare second or third highest cards
                level = 'second_highest' if level == 'first_highest' else 'third_highest'
                # while retaining only the tied candidates from the current round
                players = [
                    player for player in players if player.id in players_with_max_value]

        return winners

    def break_pair_tie(self, tied_players, score, pair_index):
        '''
        The winning hand is the hand that has a higher pair.
        For example `8c 8h 4d` beats `5s 5h 2h` because the pair of `8`s beats the pair of `5`s.
        If the pair is tied, then the remaining card is used to decide the winner.
        '''

        winner_ids = []
        third_cards = {}
        pairs_by_rank = {}
        players_by_id = {}

        for player in tied_players:

            players_by_id[player.id] = player

            for key in player.cards_by_rank:

                key_val = card_table['rank'][key]

                # if length == 2, it's a pair
                if len(player.cards_by_rank[key]) == 2:
                    if key_val in pairs_by_rank:
                        pairs_by_rank[key_val].append(player.id)
                    else:
                        pairs_by_rank[key_val] = [player.id]

        # filter out all but the highest pair
        highest_pair = sorted(pairs_by_rank.keys())[-1]

        # if more than one player left, tiebreak using third card
        for player_id in pairs_by_rank[highest_pair]:

            player = players_by_id[player_id]

            for key in player.cards_by_rank:

                key_val = card_table['rank'][key]

                # if len == 1, it's the third/nonpair card
                if len(player.cards_by_rank[key]) == 1:
                    if key_val in third_cards:
                        third_cards[key_val].append(player_id)
                    else:
                        third_cards[key_val] = [player_id]

        highest_third = sorted(third_cards.keys())[-1]

        for player_id in third_cards[highest_third]:
            winner_ids.append(player_id)

        return winner_ids

    def find_winners(self, players):

        self.winners = self.score_round(players)

    def print_winners(self):

        self.find_winners(self.players)
        print(self.winners)
