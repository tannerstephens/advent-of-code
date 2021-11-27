#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]


def dragon(a: str):
  b = a[::-1]
  b = b.translate({0x31: '0', 0x30: '1'})

  return f'{a}0{b}'


def checksum(data: str) -> str:
  r = ''.join('1' if data[i] == data[i+1] else '0' for i in range(0,len(data), 2))

  if len(r) % 2 == 0:
    return checksum(r)

  return r


def solve(pi, l):
  data = pi

  while len(data) < l:
    data = dragon(data)

  data = data[:l]

  return data, checksum(data)

def part1():
  pi = parse_input()

  return solve(pi, 272)[1]

def part2():
  pi = parse_input()

  return solve(pi, 35651584)[1]

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
