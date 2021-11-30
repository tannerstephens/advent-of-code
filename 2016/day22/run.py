#!/usr/bin/env python3

from os.path import dirname, realpath
from re import findall
from typing import Union

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[int(i) for i in findall(r'x(\d+)-y(\d+)\s+(\d+).\s+(\d+).\s+(\d+)', line)[0]] for line in puzzle_input[2:]]


class Node:
  def __init__(self, x: int, y: int, size: int, used: int, available: int) -> None:
    self.x = x
    self.y = y
    self.size = size
    self.used = used
    self.available = available

  def __repr__(self) -> str:
    return f'/dev/grid/node-x{self.x}-y{self.y}\t{self.size}T\t{self.used}T\t{self.available}T'


def build_grid(nodes: list[Node]) -> list[list[Node]]:
  width = max(nodes, key=lambda node: node.x).x + 1
  height = max(nodes, key=lambda node: node.y).y + 1

  grid: list[list[Node]] = [[nodes[0] for y in range(height)] for x in range(width)]

  for node in nodes:
    grid[node.x][node.y] = node

  return grid


def convert_to_maze(grid: list[list[Node]], wall_threshold: int, target: Node) -> tuple[list[list[str]], tuple[int, int]]:
  out = [['.' for _ in range(len(grid))] for _ in range(len(grid[0]))]

  z = (0,0)

  for x, col in enumerate(grid):
    for y, g in enumerate(col):
      if g == target:
        out[y][x] = 'G'
      elif g.used == 0:
        out[y][x] = '_'
        z = (y,x)
      elif g.used > wall_threshold:
        out[y][x] = '#'

  return out, z


def part1():
  pi = parse_input()

  nodes = [Node(*line) for line in pi]

  c = 0

  for A in nodes:
    for B in nodes:
      if A == B:
        continue

      if A.used == 0:
        continue

      if A.used <= B.available:
        c += 1

  return c

def part2():
  pi = parse_input()

  nodes = [Node(*line) for line in pi]

  wall_threshold = 400

  steps = 0

  y_0_nodes = filter(lambda node: node.y == 0, nodes)
  target = max(y_0_nodes, key=lambda node: node.x)

  grid = build_grid(nodes)
  maze, (y,x) = convert_to_maze(grid, wall_threshold, target)

  while maze[y-1][x] != '#':
    steps += 1
    y -= 1

  while maze[y-1][x] == '#':
    steps += 1
    x -= 1

  steps += y
  steps += target.x - 1 - x
  steps += (target.x - 1) * 5 + 1

  return steps

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
