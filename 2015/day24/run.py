#!/usr/bin/env python3

from os.path import dirname, realpath
from functools import reduce
from itertools import combinations
from operator import mul


dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [int(line) for line in puzzle_input]

def solve(num_groups, weights):
  target_number = sum(weights) // num_groups

  for i in range(len(weights)):
    pos = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == target_number]

    if pos:
      return min(pos)

def part1():
  pi = parse_input()

  return solve(3, pi)

def part2():
  pi = parse_input()

  return solve(4, pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
