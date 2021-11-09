#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

def parse_input():
  return map(int, puzzle_input)

def part1():
  pi = sorted(parse_input())

  ones = 0
  threes = 0

  last = 0

  for n in pi:
    delta = n-last

    if delta == 1:
      ones += delta

    elif delta == 3:
      threes += 1

    last = n

  return ones*(threes+1)

def num_ways_to_n(n, adapters, memo={0: 1}):
  for v in adapters:
    ways = 0
    for pos in range(v-3, v):
      ways += memo.get(pos, 0)
    if v == n:
      return ways
    memo[v] = ways

def part2():
  pi = sorted(parse_input())

  return num_ways_to_n(pi[-1], pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
