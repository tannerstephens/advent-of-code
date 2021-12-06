#!/usr/bin/env python3

from os.path import dirname, realpath
from re import compile

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  regex = compile(r'(\d+),(\d+) -> (\d+),(\d+)')

  return [[int(n) for n in regex.search(line).groups()] for line in puzzle_input]



def part1():
  pi = parse_input()



def part2():
  pi = parse_input()

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
