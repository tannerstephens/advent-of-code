#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  out = []

  for line in puzzle_input:
    work = line.split(' ')

    mm = work[0].split('-')

    out.append([(int(mm[0]), int(mm[1])), work[1][0], work[2]])

  return out

def part1():
  pi = parse_input()

  total = 0

  for rule in pi:
    l, r = rule[0]
    n = rule[2].count(rule[1])

    total += l <= n <= r

  return total

def part2():
  pi = parse_input()

  total = 0

  for rule in pi:
    look = rule[1]

    l, r = rule[0]

    if (look == rule[2][l-1]) != (look == rule[2][r-1]):
      total += 1

  return total

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
