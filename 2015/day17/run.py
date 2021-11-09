#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

from itertools import combinations

def parse_input():
  return list(map(int, puzzle_input))

def part1():
  TARGET = 150
  pi = parse_input()

  can_fit = 0

  for r in range(1, len(pi)):
    for comb in combinations(pi, r):
      can_fit += (sum(comb) == TARGET)

  return can_fit

def part2():
  TARGET = 150
  pi = parse_input()

  fit = False
  can_fit = 0

  for r in range(1, len(pi)):
    for comb in combinations(pi, r):
      if sum(comb) == TARGET:
        fit = True
        can_fit += 1

    if fit:
      return can_fit

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
