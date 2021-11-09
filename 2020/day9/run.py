#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

def parse_input():
  return map(int, puzzle_input)

def part1():
  pi = list(parse_input())

  i = 25

  while i < len(pi):
    s = pi[i-25:i]
    c = pi[i]
    good = False
    for val in s:
      if (c-val) in s:
        good = True
        break

    if not good:
      return c

    i += 1


def part2():
  pi = list(parse_input())

  t = part1()

  start = 0
  end = 0

  s = pi[0]

  while s != t:
    end += 1

    s += pi[end]

    while s > t:
      s -= pi[start]
      start += 1

  nums = pi[start:end]

  return min(nums) + max(nums)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
