#!/usr/bin/env python3

from math import inf
from os.path import dirname, realpath
from hashlib import md5

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]


class Maze:
  open_doors = {'b', 'c', 'd', 'e', 'f'}

  def __init__(self, passcode: str) -> None:
    self.passcode = passcode

  def get_open_doors(self, steps: str, x: int, y: int) -> tuple[bool, bool, bool, bool]:
    h = md5(f'{self.passcode}{steps}'.encode()).hexdigest()

    return (
      y > 0 and h[0] in self.open_doors,
      y < 3 and h[1] in self.open_doors,
      x > 0 and h[2] in self.open_doors,
      x < 3 and h[3] in self.open_doors,
    )

def solve(maze: Maze, shortest_path: str = None, x: int = 0, y: int = 0, path: str = None, longest_path: str = None) -> tuple[str, str]:
  if path is None:
    path = ''

  if shortest_path is None:
    shortest_path = '~'*1000

  if longest_path is None:
    longest_path = ''

  if x == 3 and y == 3:
    return path, path

  open_doors = maze.get_open_doors(path, x, y)

  for d, o in enumerate(open_doors):
    dx, dy, ds = ((0, -1, 'U'), (0, 1, 'D'), (-1, 0, 'L'), (1, 0, 'R'))[d]

    if o:
      r, l = solve(maze, shortest_path, x + dx, y + dy, path + ds, longest_path)

      if r and (len(r) < len(shortest_path)):
        shortest_path = r

      if l and (len(l) > len(longest_path)):
        longest_path = l

  return shortest_path, longest_path


def part1():
  pi = parse_input()

  maze = Maze(pi)

  return solve(maze)[0]

def part2():
  pi = parse_input()

  maze = Maze(pi)

  return len(solve(maze)[1])


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
