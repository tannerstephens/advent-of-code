#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()
  return pi[0].count('(') - pi[0].count(')')

def part2():
  pi = parse_input()
  floor = 0

  for i, c in enumerate(pi[0]):
    floor += 1 if c == '(' else -1

    if floor < 0:
      return i+1

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
