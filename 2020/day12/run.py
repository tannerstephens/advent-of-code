#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

from re import findall

def parse_input():
  out = []

  for line in puzzle_input:
    work = findall(r'(.)(.+)', line)[0]

    out.append([work[0], int(work[1])])

  return out

DIRS = {
  0: (0, 1),
  90: (1, 0),
  180: (0, -1),
  270: (-1, 0)
}

def part1():
  pi = parse_input()

  sx = 0
  sy = 0

  d = 90

  for w, a in pi:
    if   w == 'N': sy += a
    elif w == 'E': sx += a
    elif w == 'S': sy -= a
    elif w == 'W': sx -= a
    elif w == 'F':
      dx, dy = DIRS[d%360]
      sx += dx*a
      sy += dy*a
    elif w == 'L': d -= a
    elif w == 'R': d += a
    else:
      raise Exception('aaa')

  return abs(sx) + abs(sy)

def part2():
  pi = parse_input()

  sx = 0
  sy = 0

  wx = 10
  wy = 1

  for w, a in pi:
    if   w == 'N': wy += a
    elif w == 'E': wx += a
    elif w == 'S': wy -= a
    elif w == 'W': wx -= a
    elif w == 'F':
      sx += wx*a
      sy += wy*a
    elif w == 'L':
      a //= 90
      for _ in range(a):
        wx, wy = (-wy, wx)
    elif w == 'R':
      a //= 90
      for _ in range(a):
        wx, wy = (wy, -wx)
    else:
      raise Exception('aaa')

  return abs(sx) + abs(sy)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
