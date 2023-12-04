from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        points = 0

        self.wins = []

        for card in p.re_findall(r"\d+", int):
            card = card[1:]
            wins = set(card[:10]) & set(card[10:])

            self.wins.append(len(wins))

            if wins:
                points += pow(2, self.wins[-1] - 1)

        return points

    def part2(self, puzzle_input: str):
        num_cards = [1] * len(self.wins)

        for i, wins in enumerate(self.wins):
            for j in range(wins):
                num_cards[i + j + 1] += num_cards[i]

        return sum(num_cards)
