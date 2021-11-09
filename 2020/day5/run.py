#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read()

TRANSLATION_DICT = {
  70: '0',
  66: '1',
  76: '0',
  82: '1'
}

def parse_input():
  return map(lambda s: int(s, 2), puzzle_input.translate(TRANSLATION_DICT).split())

def part1():
  pi = parse_input()

  return max(pi)

def part2():
  pi = parse_input()

  seat_ids = set(pi)

  for seat_id in seat_ids:
    target = seat_id + 1
    if target not in seat_ids:
      return target

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
