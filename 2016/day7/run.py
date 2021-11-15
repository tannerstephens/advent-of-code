#!/usr/bin/env python3

from os.path import dirname, realpath
import re
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  in_brackets = r'\[(.*?)\]'

  return [(line, re.findall(in_brackets, line)) for line in puzzle_input]

def part1():
  pi = parse_input()

  abba = r'([a-z])(?!\1)([a-z])\2\1'

  count = 0

  for line in pi:
    if re.search(abba, line[0]) and not any([re.search(abba, l) for l in line[1]]):
      count += 1

  return count

def part2():
  pi = puzzle_input[:]

  r1 = r'(([a-z])(?!\2)([a-z])\2)(?![a-z]*\]).*\[[a-z]*\3\2\3[a-z]*\]'
  r2 = r'\[[a-z]*(([a-z])(?!\2)([a-z])\2).*\][a-z]*\3\2\3'

  count = 0

  for line in pi:
    if re.search(r1, line) or re.search(r2, line):
      count += 1

  return count


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
