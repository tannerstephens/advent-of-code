#!/usr/bin/env python3

from os.path import dirname, realpath
from re import match

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0].translate({94: 'T', 46: 'S'})


class Traps:
  trap_regex = r'T.S|S.T'

  def __init__(self, first_row: str) -> None:
    self.working_row = first_row

    self.safe = first_row.count('S')

    self.lookup = {}

  def get_above_three(self, i: int) -> str:
    if i == 0:
      return 'S' + self.working_row[0:2]

    if i == len(self.working_row) - 1:
      return self.working_row[-2:] + 'S'

    return self.working_row[i-1:i+2]

  def generate_next_row(self):
    if self.working_row in self.lookup:
      new_row = self.lookup[self.working_row]
    else:
      new_row = ''

      for i in range(len(self.working_row)):
        above_three = self.get_above_three(i)

        trap = match(self.trap_regex, above_three)

        new_row += 'T' if trap else 'S'

      self.lookup[self.working_row] = new_row

    self.safe += new_row.count('S')
    self.working_row = new_row


  def generate_x_rows(self, x: int):
    for _ in range(x):
      self.generate_next_row()



def part1():
  pi = parse_input()

  traps = Traps(pi)

  traps.generate_x_rows(39)

  return traps.safe

def part2():
  pi = parse_input()

  traps = Traps(pi)

  traps.generate_x_rows(399999)

  return traps.safe

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
