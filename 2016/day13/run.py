#!/usr/bin/env python3

from __future__ import annotations

from math import inf
from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return int(puzzle_input[0])


class Maze:
  def __init__(self, seed: int) -> None:
    self.seed = seed

  def is_wall(self, x: int, y: int) -> bool:
    step_1 = x*x + 3*x + 2*x*y + y + y*y
    step_2 = step_1 + self.seed
    step_3 = bin(step_2)[2:].count('1')

    return bool(step_3 % 2)


def flood_find(maze: Maze, start: tuple[int, int], target: tuple[int, int] = None, stop: float = inf) -> int:
  class Node:
    def __init__(self, x: int, y: int, parent: Node = None) -> None:
      self.parent = parent
      self.x = x
      self.y = y

  seen = set()
  seen.add(start)

  if target is None:
    target = (-5, -5)

  edge_nodes = [Node(start[0], start[1])]

  s = 0

  while True:
    s += 1
    new_nodes = []
    for node in edge_nodes:
      for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
        nx = node.x + dx
        ny = node.y + dy

        if (nx, ny) == target:
          return s

        if nx < 0 or ny < 0:
          continue

        if (nx, ny) in seen:
          continue

        if maze.is_wall(nx, ny):
          continue

        seen.add((nx, ny))

        new_nodes.append(Node(nx, ny, node))

    edge_nodes = new_nodes

    if s == stop:
      return len(seen)



def part1():
  pi = parse_input()

  maze = Maze(pi)

  return flood_find(maze, (1, 1), (31, 39))

def part2():
  pi = parse_input()

  maze = Maze(pi)

  return flood_find(maze, (1, 1), stop=50)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
