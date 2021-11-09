#!/usr/bin/env python3

from hashlib import md5
from os.path import dirname, realpath

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def find_prefix(key, prefix):
  num = 1
  while md5(f'{key}{num}'.encode()).hexdigest()[:len(prefix)] != prefix:
    num += 1

  return num

def part1():
  pi = parse_input()

  return find_prefix(pi[0], '00000')

def part2():
  pi = parse_input()

  return find_prefix(pi[0], '000000')

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
