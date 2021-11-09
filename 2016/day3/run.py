#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input() -> list[list[int]]:
  return [[int(n) for n in line.split()] for line in puzzle_input]


def validate_triangle(a, b, c):
  hyp = max(a,b,c)

  legs = a+b+c-hyp

  return legs > hyp


def rotate_input(pi):
  out = []

  for i in range(0, len(pi), 3):
    out += [
      [pi[i][0], pi[i+1][0], pi[i+2][0]],
      [pi[i][1], pi[i+1][1], pi[i+2][1]],
      [pi[i][2], pi[i+1][2], pi[i+2][2]],
    ]

  return out


def part1():
  pi = parse_input()

  return len(list(filter(lambda pos: validate_triangle(*pos), pi)))

def part2():
  pi = parse_input()

  rotated_input = rotate_input(pi)

  return len(list(filter(lambda pos: validate_triangle(*pos), rotated_input)))

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
