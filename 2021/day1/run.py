#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [int(line) for line in puzzle_input]

def part1():
  pi = parse_input()

  c = 0
  l = 99999

  for n in pi:
    c += n > l
    l = n

  return c

def part2():
  pi = parse_input()

  c = 0
  l = 9999999

  for i, n1 in enumerate(pi[:-2]):
    n = n1 + pi[i+1] + pi[i+2]
    c += n > l
    l = n

  return c

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
