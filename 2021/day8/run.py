#!/usr/bin/env python3

from os.path import dirname, realpath
from typing import DefaultDict
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[a.split(' ') for a in line.split(' | ')] for line in puzzle_input]


def part1():
  pi = parse_input()

  count = 0

  look = {2, 4, 3, 7}

  for left, right in pi:
    for c in right:
      count += len(c) in look

  return count

def part2():
  pi = parse_input()

  count = 0

  for left, right in pi:
    by_length = DefaultDict(list)

    for seg in left:
      l = len(seg)

      by_length[l].append(set(seg))

    num_map = {
      tuple(sorted(by_length[2][0])): 1,
      tuple(sorted(by_length[3][0])): 7,
      tuple(sorted(by_length[4][0])): 4,
      tuple(sorted(by_length[7][0])): 8
    }

    one = by_length[2][0]
    four = by_length[4][0]

    for seg in by_length[5]:
      if len(seg.intersection(one)) == 2:
        num_map[tuple(sorted(seg))] = 3
      elif len(seg.intersection(four)) == 3:
        num_map[tuple(sorted(seg))] = 5
      else:
        num_map[tuple(sorted(seg))] = 2

    for seg in by_length[6]:
      if len(seg.intersection(one)) == 1:
        num_map[tuple(sorted(seg))] = 6
      elif len(seg.intersection(four)) == 4:
        num_map[tuple(sorted(seg))] = 9
      else:
        num_map[tuple(sorted(seg))] = 0

    for i, seg in enumerate(right):
      key = tuple(sorted(seg))

      count += pow(10, 3-i) * num_map[key]

  return count

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
