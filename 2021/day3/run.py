#!/usr/bin/env python3

from os.path import dirname, realpath
from math import ceil

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input(line_fn=str):
  return [line_fn(line) for line in puzzle_input]

def part1():
  pi = parse_input()

  count = [0 for _ in pi[0]]

  for line in pi:
    for i,c in enumerate(line):
      count[i] += c == '1'

  half = len(pi) // 2

  gamma = ''
  epsilon = ''

  for c in count:
    gamma = gamma + ('1' if c > half else '0')
    epsilon = epsilon + ('0' if c > half else '1')


  g = int(gamma, 2)
  e = int(epsilon, 2)

  return g*e

def part2():
  most = parse_input()
  least = list(most)

  i = 0

  while len(most) > 1:
    one_count = 0

    for line in most:
      one_count += line[i] == '1'

    half = ceil(len(most) / 2)

    f = '1' if one_count >= half else '0'

    most = list(filter(lambda line: line[i] == f, most))

    i += 1

  i = 0

  while len(least) > 1:
    one_count = 0

    for line in least:
      one_count += line[i] == '1'

    half = ceil(len(least) / 2)

    f = '0' if one_count >= half else '1'

    least = list(filter(lambda line: line[i] == f, least))

    i += 1

  return int(most[0], 2) * int(least[0], 2)


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
