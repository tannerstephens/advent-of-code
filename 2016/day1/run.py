#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0].split(', ')


class City:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

    self.d = 0

  def turn_left(self):
    self.d = (self.d - 1) % 4

  def turn_right(self):
    self.d = (self.d + 1) % 4

  def walk(self, blocks):
    dx = 0
    dy = 0

    if self.d == 0:
      dy = 1
    elif self.d == 1:
      dx = 1
    elif self.d == 2:
      dy = -1
    else:
      dx = -1

    self.x += dx * blocks
    self.y += dy * blocks

  def get_location(self):
    return self.x, self.y

  def run_part_1(self, instructions):
    for inst in instructions:
      t = inst[0]

      blocks = int(inst[1:])

      if t == 'L':
        self.turn_left()
      else:
        self.turn_right()

      self.walk(blocks)

    return abs(self.x) + abs(self.y)

  def run_part_2(self, insts):
    seen = set()

    for inst in insts:
      t = inst[0]

      blocks = int(inst[1:])

      if t == 'L':
        self.turn_left()
      else:
        self.turn_right()

      for _ in range(blocks):
        seen.add((self.get_location()))
        self.walk(1)
        if self.get_location() in seen:
          return abs(self.x) + abs(self.y)


def part1():
  pi = parse_input()

  city = City()

  return city.run_part_1(pi)


def part2():
  pi = parse_input()

  city = City()

  return city.run_part_2(pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
