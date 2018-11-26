from poker_tables import card_table

class PokerPlayer():

    def __init__(self, id):

        self.id = id
        self.cards_by_suit = {}
        self.cards_by_rank = {}
        self.ranks = []
        self.suits = []
        self.run = []

    def set_hand(self, line_cards):

        for card in line_cards:

            card_rank = card[0]
            card_suit = card[1]
            self.ranks.append(card_rank)
            self.suits.append(card_suit)

            if card_suit not in self.cards_by_suit:
                self.cards_by_suit[card_suit] = [card_rank]
            else:
                self.cards_by_suit[card_suit].append(card_rank)

            if card_rank not in self.cards_by_rank:
                self.cards_by_rank[card_rank] = [card_suit]
            else:
                self.cards_by_rank[card_rank].append(card_suit)

        card1 = card_table['rank'][self.ranks[0]]
        card2 = card_table['rank'][self.ranks[1]]
        card3 = card_table['rank'][self.ranks[2]]
        run = sorted([card1, card2, card3])

        self.run = run
        self.first_highest, self.second_highest, self.third_highest = run[2], run[1], run[0]
        self.score = self.score_hand()

        if (self.score == 'Straight' or self.score == 'Straight Flush'):
            if self.run == [2, 3, 14]:
                self.run = [1, 2, 3]
                # change depending on one's definition of ace's value in a low ace straight
                self.third_highest, self.second_highest, self.first_highest = 2, 3, 14

    def is_a_straight_flush(self):
        '''
        Straight Flush:
        A straight flush is a hand that is both a straight and a flush.
        '''

        return self.is_a_straight() and self.is_a_flush()

    def is_three_of_a_kind(self):
        '''
        Three Of A Kind:
        A three of a kind is a hand in which all three of the cards have the same rank.
        '''

        return len(self.cards_by_rank.keys()) == 1

    def is_a_straight(self):
        '''
        Straight:
        A straight is a hand in which the cards have ranks that are in a 'run.'
        This means that they are of the format `n, n+1, n+2`, where n is the index of the following:
        [ `2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A`].

        Some examples of straights:

        - the hand `5h 3c 4d` (because the cards can be ordered `3c 4d 5h` to form a 'run' of `3-4-5`)
        - the hand `Qh Kd As` (because it forms a run of `Q-K-A`)
        - the hand `9h Td Js` (because it forms a run of `9-T-J`)

        SPECIAL CASE:
        Aces can also be used as a 1. That means that `A-2-3` is also a run.
        An ace cannot, however, be both high and low in the same straight, so `K-A-2` does not qualify.

        '''

        card1, card2, card3 = self.run[0], self.run[1], self.run[2]

        low_straight = (card1 == 2 and card2 == 3 and card3 == 14)
        normal_straight = (card3 - card2 == 1 and card2 - card1 == 1)

        return True if low_straight or normal_straight else False

    def is_a_flush(self):
        '''
        Flush: A flush is a hand in which all three cards have the same suit.
        '''

        return len(self.cards_by_suit.keys()) == 1

    def is_a_pair(self):
        '''
        Pair: A pair is a hand in which two of the cards have the same rank, but the third is different.
        '''

        return len(self.cards_by_rank.keys()) == 2

    def find_high(self):
        '''
        High Card: Any hand that doesn't fit into one of the other categories is considered a 'high card' hand.
        '''

        highest_card = str(self.run[-1])

        if highest_card in card_table['rank']:
            return card_table['rank'][highest_card]
        else:
            return card_table['numbers_to_text'][highest_card]

    def score_hand(self):

        if self.is_a_straight_flush():
            return 'Straight Flush'
        elif self.is_three_of_a_kind():
            return 'Three of a Kind'
        elif self.is_a_straight():
            return 'Straight'
        elif self.is_a_flush():
            return 'Flush'
        elif self.is_a_pair():
            return 'Pair'
        else:
            return self.find_high()
