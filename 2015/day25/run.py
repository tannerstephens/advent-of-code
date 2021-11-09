#!/usr/bin/env python3

from os.path import dirname, realpath
import re

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  regex = r'.+row (\d+).+column (\d+)'
  r = re.match(regex, puzzle_input[0])

  return int(r.group(1)), int(r.group(2))


def part1():
  pi = parse_input()

  code = 20151125

  x = 1
  y = 2

  while x != pi[1] or y != pi[0]:
    code *= 252533
    code %= 33554393

    x += 1
    y -= 1

    if y == 0:
      y = x
      x = 1

  code *= 252533
  code %= 33554393

  return code

def part2():
  return 'Freebie'

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
