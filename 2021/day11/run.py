#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[int(n) for n in line] for line in puzzle_input]


def flood_flash(octopi: list[list[int]], edge: list[tuple[int, int]]) -> int:
  seen = set(edge)

  while edge:
    new_edge = []

    for x, y in edge:
      for dx in range(-1, 2):
        for dy in range(-1, 2):
          if dx == 0 and dy == 0:
            continue

          nx = x + dx
          ny = y + dy

          if nx < 0 or nx >= len(octopi[0]) or ny < 0 or ny >= len(octopi):
            continue

          if (nx, ny) in seen:
            continue

          octopi[ny][nx] = (octopi[ny][nx] + 1) % 10

          if octopi[ny][nx] == 0:
            new_edge.append((nx, ny))
            seen.add((nx, ny))

    edge = new_edge

  return len(seen)

def part1():
  octopi = parse_input()

  count = 0

  for step in range(100):
    flashes = []

    for y in range(len(octopi)):
      for x in range(len(octopi[0])):
        octopi[y][x] = (octopi[y][x] + 1) % 10

        if octopi[y][x] == 0:
          flashes.append((x, y))

    count += flood_flash(octopi, flashes)

  return count


def part2():
  octopi = parse_input()

  c = 0
  step = 0

  while c != 100:
    step += 1
    flashes = []

    for y in range(len(octopi)):
      for x in range(len(octopi[0])):
        octopi[y][x] = (octopi[y][x] + 1) % 10

        if octopi[y][x] == 0:
          flashes.append((x, y))

    c = flood_flash(octopi, flashes)

  return step

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
