#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]


DIR_MAP = {'^': (0,1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}

def part1():
  pi = parse_input()

  x = y = 0

  visited = {(0,0): 1}

  for c in pi[0]:
    d = DIR_MAP[c]

    x += d[0]
    y += d[1]

    if (x,y) not in visited:
      visited[(x,y)] = 1
    else:
      visited[(x,y)] += 1

  return len(visited.keys())

def part2():
  pi = parse_input()

  x = y = rx = ry = 0

  visited = {(0,0)}

  for i in range(0,len(pi[0]), 2):
    sd = DIR_MAP[pi[0][i]]
    rsd = DIR_MAP[pi[0][i+1]]

    x += sd[0]
    y += sd[1]

    rx += rsd[0]
    ry += rsd[1]

    visited.add((x,y))
    visited.add((rx,ry))

  return len(visited)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
