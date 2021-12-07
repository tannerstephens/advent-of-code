#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [int(n) for n in puzzle_input[0].split(',')]


class Crab:
  def __init__(self, pos: int) -> None:
    self.pos = pos

  def distance(self, pos: int) -> int:
    return abs(self.pos - pos)


def fuel_cost(crabs: list[Crab], pos: int) -> int:
  return sum(crab.distance(pos) for crab in crabs)

def binom2(x: int) -> int:
  return x * (x+1) // 2

def fuel_cost2(crabs: list[Crab], pos: int) -> int:
  return sum(binom2(crab.distance(pos)) for crab in crabs)

def part1():
  pi = parse_input()

  # Critical points will only occur when at least one crab will not move, so we only need to check starting positions

  unique = set(pi)

  crabs = [Crab(n) for n in pi]

  return min(fuel_cost(crabs, n) for n in unique)

def part2():
  pi = parse_input()

  # Fuel cost is binom(abs(3 - x) +1, 2)
  # Again, the critical points are as above

  unique = set(pi)

  crabs = [Crab(n) for n in pi]

  return min(fuel_cost2(crabs, n) for n in unique)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
