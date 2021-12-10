#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[int(n) for n in line] for line in puzzle_input]


def low_points(pi: list[list[int]]) -> list[int]:
  for y, line in enumerate(pi):
    for x, n in enumerate(line):
      if x > 0 and n >= pi[y][x-1]:
        continue
      if y > 0 and n >= pi[y-1][x]:
        continue
      if x < len(line) - 1 and n >= pi[y][x+1]:
        continue
      if y < len(pi) - 1 and n >= pi[y+1][x]:
        continue

      yield (x,y,n)

def part1():
  pi = parse_input()

  return sum(n[2]+1 for n in low_points(pi))

def get_basin_size(pi: list[list[int]], x: int, y: int) -> int:
  seen = {(x,y)}

  edge = [(x, y)]

  while edge:
    new_edge = []

    for x, y in edge:
      n = pi[y][x]

      for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
        nx = x+dx
        ny = y+dy

        if nx < 0 or nx >= len(pi[0]):
          continue

        if ny < 0 or ny >= len(pi):
          continue

        if (nx, ny) in seen:
          continue

        if pi[ny][nx] > n and pi[ny][nx] != 9:
          seen.add((nx,ny))
          new_edge.append((nx, ny))

    edge = new_edge

  return len(seen)

def part2():
  pi = parse_input()

  basin_sizes = sorted(get_basin_size(pi, x, y) for x,y,_ in low_points(pi))

  return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
