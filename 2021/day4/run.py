#!/usr/bin/env python3

from os.path import dirname, realpath

from re import compile

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  numbers = [int(n) for n in puzzle_input[0].split(',')]

  r = compile(r' ?(\d+) +(\d+) +(\d+) +(\d+) +(\d+)')

  boards = [[[int(n) for n in r.findall(line)[0]] for line in puzzle_input[i:i+5]] for i in range(2, len(puzzle_input), 6)]

  return numbers, boards


class BingoBoard:
  def __init__(self, board: list[list[int]]) -> None:
    self.board = board

    self.lookup = {}

    for y, line in enumerate(board):
      for x, n in enumerate(line):
        self.lookup[n] = (x, y)

    self.card = [[False for _ in self.board[0]] for _ in self.board]

  def __repr__(self) -> str:
    out = ''

    for line in self.board:
      out += f'{line[0]:2} {line[1]:2} {line[2]:2} {line[3]:2} {line[4]:2}\n'

    return out

  def check_win(self):
    cols = [[] for _ in self.card]
    diag = [[], []]

    for d, line in enumerate(self.card):
      if sum(line) == 5:
        return True

      for i in range(5):
        cols[i].append(line[i])

      diag[0].append(line[d])
      diag[1].append(line[-d-1])

    for col in cols:
      if sum(col) == 5:
        return True

    for di in diag:
      if sum(di) == 5:
        return True

    return False


  def call_number(self, n: int) -> bool:
    if n in self.lookup:
      x, y = self.lookup[n]

      self.card[y][x] = True

      return self.check_win()

    return False

  def get_unmarked_numbers(self):
    out = []

    for y, line in enumerate(self.board):
      for x, n in enumerate(line):
        if not self.card[y][x]:
          out.append(n)

    return out


def get_first_winner(numbers: list[int], boards: list[BingoBoard]) -> tuple[BingoBoard, int]:
  for n in numbers:
    for board in boards:
      if board.call_number(n):
        return board, n

def get_last_board(numbers: list[int], boards: list[BingoBoard]) -> tuple[BingoBoard, int]:
  not_won = boards

  for n in numbers:
    next_not_won = []

    for board in not_won:
      if not board.call_number(n):
        next_not_won.append(board)

      elif len(not_won) == 1:
        return board, n

    not_won = next_not_won


def part1():
  numbers, boards = parse_input()

  boards = [BingoBoard(board) for board in boards]

  winner, n = get_first_winner(numbers, boards)

  return sum(winner.get_unmarked_numbers()) * n


def part2():
  numbers, boards = parse_input()

  boards = [BingoBoard(board) for board in boards]

  loser, n = get_last_board(numbers, boards)

  return sum(loser.get_unmarked_numbers()) * n

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
