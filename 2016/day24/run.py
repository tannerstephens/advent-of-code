#!/usr/bin/env python3

from os.path import dirname, realpath
from itertools import chain, permutations
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [list(line) for line in puzzle_input]


def get_number_positions(pi: list[list[str]]) -> dict:
  out = {}

  for y, line in enumerate(pi):
    for x, c in enumerate(line):
      if c.isdigit():
        out[c] = (x,y)

  return out


def get_distance_to_all_numbers(maze: list[list[str]], start: tuple[int, int]) -> dict:
  distances = {}

  seen = {start}

  edge = [start]

  s = 0

  while edge:
    next_edge = []

    s += 1

    for x,y in edge:
      for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx > len(maze[0]) or ny < 0 or ny > len(maze):
          continue

        if (nx, ny) in seen:
          continue

        if maze[ny][nx] == '#':
          continue

        seen.add((nx, ny))

        if maze[ny][nx].isdigit():
          distances[maze[ny][nx]] = s
          continue

        next_edge.append((nx, ny))

    edge = next_edge

  return distances


def get_distances_from_each_number_to_each_number(maze: list[list[str]], starts: dict[str, tuple[int, int]]) -> dict:
  out = {}

  for n, start in starts.items():
    out[n] = get_distance_to_all_numbers(maze, start)

  return out


def traveling_salesman(distances: dict[str, dict[str, int]], start: str, extra: list[str] = None) -> int:
  remaining_keys = list(distances.keys())
  remaining_keys.remove(start)

  if extra is None:
    extra = []

  min_dist = 99999999999

  for path in permutations(remaining_keys, len(remaining_keys)):
    d = 0
    last = '0'

    path_iter = chain(path, extra)

    for c in path_iter:
      d += distances[last][c]
      last = c

    if d < min_dist:
      min_dist = d

  return min_dist



def part1():
  pi = parse_input()

  number_positions = get_number_positions(pi)

  distances = get_distances_from_each_number_to_each_number(pi, number_positions)

  return traveling_salesman(distances, '0')

def part2():
  pi = parse_input()

  number_positions = get_number_positions(pi)

  distances = get_distances_from_each_number_to_each_number(pi, number_positions)

  return traveling_salesman(distances, '0', extra=['0'])

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
