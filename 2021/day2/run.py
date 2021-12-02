#!/usr/bin/env python3

from os.path import dirname, realpath
from re import compile

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input(line_fn=str):
  for line in puzzle_input:
    yield line_fn(line)

def part1():
  pattern = compile(r'forward (\d)|down (\d)|up (\d)')

  pi = parse_input(lambda line: [int(n) if n else 0 for n in pattern.search(line).groups()])

  x = 0
  y = 0

  for dx, dd, du in pi:
    x += dx
    y += dd - du

  return x*y


def part2():
  pattern = compile(r'forward (\d)|down (\d)|up (\d)')

  pi = parse_input(lambda line: [int(n) if n else 0 for n in pattern.search(line).groups()])

  aim = 0
  x = 0
  y = 0

  for dx, dd, du in pi:
    x += dx
    aim += dd - du
    y += dx * aim

  return x*y

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
