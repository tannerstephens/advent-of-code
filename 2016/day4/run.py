#!/usr/bin/env python3

from os.path import dirname, realpath
from functools import reduce
from collections import defaultdict
from string import ascii_lowercase

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[line[:-7], line[-6:-1]] for line in puzzle_input]


def compute_checksum(s):
  counts = defaultdict(int)

  for c in s:
    if c != '-' and not c.isdigit():
      counts[c] += 1

  to_sort = [(value, key) for key, value in counts.items()]

  by_letter = sorted(to_sort, key=lambda v: v[1])

  by_value = sorted(by_letter, key=lambda v: v[0], reverse=True)

  return ''.join([count[1] for count in by_value[:5]])


def generate_caesar(shift) -> dict:
  t = {}

  for i, c in enumerate(ascii_lowercase):
    t[ord(c)] = ascii_lowercase[(i + shift) % len(ascii_lowercase)]

  return t


def caesar(s: str, shift):
  trans = generate_caesar(shift)

  return s.translate(trans)


def get_valid_rooms(pi):
  return filter(lambda inp: compute_checksum(inp[0]) == inp[1], pi)


def part1():
  pi = parse_input()

  valid = get_valid_rooms(pi)

  return reduce(lambda a,b: a + int(b[0].split('-')[-1]), valid, 0)

def part2():
  pi = parse_input()

  valid = get_valid_rooms(pi)

  trans = map(lambda inp: caesar(inp[0], int(inp[0].split('-')[-1])), valid)

  filt = filter(lambda t: 'north' in t, trans)

  return filt.__next__().split('-')[-1]


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
