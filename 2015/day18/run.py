#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[True if c == '#' else False for c in line] for line in puzzle_input]

LOOK = (
  (-1, -1),
  (0, -1),
  (1, -1),
  (-1, 0),
  (1, 0),
  (-1, 1),
  (0, 1),
  (1, 1)
)

def get_alive_neighbors(grid, x, y):
  alive = 0

  for dx, dy in LOOK:
    try:
      lx = x+dx
      ly = y+dy

      if lx < 0 or ly < 0:
        continue

      alive += grid[lx][ly]
    except IndexError:
      continue

  return alive



def part1():
  grid = parse_input()

  for _ in range(100):
    count_grid = [[get_alive_neighbors(grid, x, y) for y in range(len(grid))] for x in range(len(grid))]

    for y in range(len(grid)):
      for x in range(len(grid)):
        grid[x][y] = True if (grid[x][y] and count_grid[x][y] in [2, 3]) or (count_grid[x][y] == 3) else False

  count = 0
  for line in grid:
    count += line.count(True)

  return count

def part2():
  grid = parse_input()

  on = (
    (0,0),
    (0, len(grid)-1),
    (len(grid)-1, 0),
    (len(grid)-1, len(grid)-1)
  )

  for x,y in on:
    grid[x][y] = True

  for _ in range(100):
    count_grid = [[get_alive_neighbors(grid, x, y) for y in range(len(grid))] for x in range(len(grid))]

    for y in range(len(grid)):
      for x in range(len(grid)):
        grid[x][y] = True if (grid[x][y] and count_grid[x][y] in [2, 3]) or (count_grid[x][y] == 3) else False

    for x,y in on:
      grid[x][y] = True

  count = 0
  for line in grid:
    count += line.count(True)

  return count

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
