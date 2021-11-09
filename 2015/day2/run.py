#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  listified = []

  for line in puzzle_input:
    listified.append(list(map(int, line.split('x'))))

  return listified

def surface_area(present):
  l,w,h = present
  return (2*l*w) + (2*w*h) + (2*h*l)

def get_small_side(present):
  small_side = present[:]
  small_side.remove(max(present))

  return small_side

def small_side_area(present):
  ss = get_small_side(present)

  return ss[0] * ss[1]

def small_side_perimiter(present):
  ss = get_small_side(present)
  return 2*ss[0] + 2*ss[1]

def volume(present):
  l,w,h = present

  return l*w*h

def part1():
  pi = parse_input()

  sqft = 0

  for present in pi:
    sqft += surface_area(present) + small_side_area(present)

  return sqft

def part2():
  pi = parse_input()

  ft = 0

  for present in pi:
    ft += volume(present) + small_side_perimiter(present)

  return ft

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
