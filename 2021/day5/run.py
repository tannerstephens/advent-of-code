#!/usr/bin/env python3

from collections import defaultdict
from os.path import dirname, realpath
from re import compile

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  regex = compile(r'(\d+),(\d+) -> (\d+),(\d+)')

  return [[int(n) for n in regex.search(line).groups()] for line in puzzle_input]


def get_delta(_1, _2):
  if _1 < _2:
    return 1
  elif _1 > _2:
    return -1
  else:
    return 0


def update_points(line: list[int], points: defaultdict):
  x1, y1, x2, y2 = line

  dx = get_delta(x1, x2)
  dy = get_delta(y1, y2)

  x = x1 - dx
  y = y1 - dy

  while x != x2 or y != y2:
    x += dx
    y += dy

    points[(x,y)] += 1



def part1():
  pi = parse_input()

  hor_and_ver = filter(lambda line: line[0] == line[2] or line[1] == line[3], pi)

  points = defaultdict(int)

  for line in hor_and_ver:
    update_points(line, points)

  return sum(1 for i in points if points[i] > 1)


def part2():
  pi = parse_input()

  points = defaultdict(int)

  for line in pi:
    update_points(line, points)

  return sum(1 for i in points if points[i] > 1)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
