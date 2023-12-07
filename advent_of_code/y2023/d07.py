from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    HAND_TYPES = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]
    CARD_ORDER = "23456789TJQKA"

    def cards_to_values(self, hand, card_order=None):
        card_order = card_order or self.CARD_ORDER
        return tuple(card_order.index(c) for c in hand)

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        s = 0

        hands = []

        self.processed_hands = [
            (tuple(sorted(Processing(line[0][0]).counts().values())), int(line[0][1]), line[0][0])
            for line in p.re_findall(r"(.+?) (\d+)", mapping=lambda s: s)
        ]

        for hand, bet, cards in self.processed_hands:
            strength = self.HAND_TYPES.index(hand) + 1

            hands.append((strength, bet, self.cards_to_values(cards)))

        hands.sort(key=lambda hand: (hand[0], *hand[2]))

        for i, hand in enumerate(hands):
            s += hand[1] * (i + 1)

        return s

    def part2(self, puzzle_input: str):
        s = 0

        hands = []

        for hand, bet, cards in self.processed_hands:
            if "J" in cards and hand[0] != 5:
                jokers_count = cards.count("J")

                hand = list(hand)
                hand.remove(jokers_count)
                hand[-1] += jokers_count

                hand = tuple(hand)

            strength = self.HAND_TYPES.index(hand) + 1

            hands.append((strength, bet, self.cards_to_values(cards, "J23456789TQKA")))

        hands.sort(key=lambda hand: (hand[0], *hand[2]))

        for i, hand in enumerate(hands):
            s += hand[1] * (i + 1)

        return s
