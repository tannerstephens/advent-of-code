#!/usr/bin/env python3

from os.path import dirname, realpath
from collections import defaultdict

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]


class ErrorCorrect:
  def __init__(self):
    self.letter_counts: list[defaultdict] = []

  def parse_line(self, line: str):
    for i, c in enumerate(line):
      if i >= len(self.letter_counts):
        self.letter_counts.append(defaultdict(int))

      self.letter_counts[i][c] += 1

  def parse_lines(self, lines: list[str]):
    for line in lines:
      self.parse_line(line)

  def get_error_corrected_line(self):
    return ''.join(map(lambda letter_count: max(letter_count, key=letter_count.get), self.letter_counts))

  def get_min_line(self):
    return ''.join(map(lambda letter_count: min(letter_count, key=letter_count.get), self.letter_counts))

def part1():
  pi = parse_input()

  error_correct = ErrorCorrect()
  error_correct.parse_lines(pi)

  return error_correct.get_error_corrected_line()

def part2():
  pi = parse_input()

  error_correct = ErrorCorrect()
  error_correct.parse_lines(pi)

  return error_correct.get_min_line()

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
