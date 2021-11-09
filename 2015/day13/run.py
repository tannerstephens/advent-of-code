#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

from itertools import permutations

def parse_input():
  happiness_map = {}
  for line in puzzle_input:
    work = line.split(' ')

    p1 = work[0]
    p2 = work[-1][:-1]

    if p1 not in happiness_map:
      happiness_map[p1] = {}

    change = -1 if work[2] == 'lose' else 1

    happiness_map[p1][p2] = change*int(work[3])

  return happiness_map

def calculate_table_score(happiness_map, order):
  score = 0

  l = len(order)

  for i in range(l):
    person = order[i]
    person_l = order[i-1]
    person_r = order[(i+1)%l]

    score += happiness_map[person][person_l] + happiness_map[person][person_r]

  return score

def part1():
  pi = parse_input()

  return max(map(lambda order: calculate_table_score(pi, order), permutations(pi.keys(), len(pi.keys()))))

def part2():
  pi = parse_input()

  old = pi.keys()

  pi['ME'] = {}

  for key in old:
    pi[key]['ME'] = 0
    pi['ME'][key] = 0

  return max(map(lambda order: calculate_table_score(pi, order), permutations(pi.keys(), len(pi.keys()))))

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
