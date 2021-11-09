#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from functools import reduce

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()

  mem = reduce(lambda t, line: t + len(eval(line)), pi, 0)
  return reduce(lambda t, line: t + len(line), pi, 0) - mem

def part2():
  pi = parse_input()

  og_length = reduce(lambda t, line: t + len(line), pi, 0)
  encode_length = reduce(lambda t, line: t + len(line) + line.count('"') + line.count('\\') + 2, pi, 0)

  return encode_length - og_length

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
