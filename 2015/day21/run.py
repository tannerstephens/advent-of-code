#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from itertools import combinations

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  out = []
  for line in puzzle_input:
    out.append(int(line.split(' ')[-1]))

  return out

WEAPONS = (
  (8, 4),
  (10, 5),
  (25, 6),
  (40, 7),
  (74, 8)
)

ARMOR = (
  (0, 0),
  (13, 1),
  (31, 2),
  (53, 3),
  (75, 4),
  (102, 5)
)

RINGS = (
  (0, 0, 0),
  (0, 0, 0),
  (25, 1, 0),
  (50, 2, 0),
  (100, 3, 0),
  (20, 0, 1),
  (40, 0, 2),
  (80, 0, 3)
)

def part1():
  pi = parse_input()

  m = []

  for weapon in WEAPONS:
    for armor in ARMOR:
      for rings in combinations(RINGS, 2):
        damage = weapon[1] + sum([ring[1] for ring in rings])
        defense = armor[1] + sum([ring[2] for ring in rings])

        boss_dps = max(pi[1] - defense, 1)
        player_dps = max(damage - pi[2], 1)

        delta = player_dps - boss_dps

        if delta >= 1:
          m.append(armor[0] + weapon[0] + sum([ring[0] for ring in rings]))

  return min(m)



def part2():
  pi = parse_input()

  m = []

  for weapon in WEAPONS:
    for armor in ARMOR:
      for rings in combinations(RINGS, 2):
        damage = weapon[1] + sum([ring[1] for ring in rings])
        defense = armor[1] + sum([ring[2] for ring in rings])

        boss_dps = max(pi[1] - defense, 1)
        player_dps = max(damage - pi[2], 1)

        delta = player_dps - boss_dps

        if delta < 1:
          m.append(armor[0] + weapon[0] + sum([ring[0] for ring in rings]))

  return max(m)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
