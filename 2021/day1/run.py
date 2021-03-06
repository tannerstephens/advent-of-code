#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input(line_fn=str):
  return [line_fn(line) for line in puzzle_input]

def count_window(pi: list[int], comparison_size: int = 1) -> int:
  c = 0

  n = sum(pi[:comparison_size])

  for i in range(len(pi) - comparison_size):
    s = sum(pi[i+1:i+comparison_size+1])
    c += s > n
    n = s

  return c

def part1():
  pi = parse_input(int)

  return count_window(pi)

def part2():
  pi = parse_input(int)

  return count_window(pi, 3)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
