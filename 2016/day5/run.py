#!/usr/bin/env python3

from os.path import dirname, realpath
from hashlib import md5
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]

def part1():
  pi = parse_input()

  i = 0

  p = ''

  while len(p) != 8:
    check = f'{pi}{i}'

    m = md5(check.encode()).hexdigest()

    if m[:5] == '00000':
      p += m[5]

    i += 1

  return p

def part2():
  pi = parse_input()

  i = 0

  p = ['~'] * 8

  while '~' in p:
    check = f'{pi}{i}'

    m = md5(check.encode()).hexdigest()

    if m[:5] == '00000':
      pos = m[5]

      if pos in {'0', '1', '2', '3', '4', '5', '6' ,'7'}:
        if p[int(pos)] == '~':
          p[int(pos)] = m[6]

    i += 1

  return ''.join(p)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
