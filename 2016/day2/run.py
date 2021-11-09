#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]


class Keypad:
  keys = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]

  def __init__(self, x=1, y=1):
    self.y = y
    self.x = x

  def move(self, direction):
    if direction == 'U':
      self.y -= 1
    elif direction == 'D':
      self.y += 1
    elif direction == 'L':
      self.x -= 1
    elif direction == 'R':
      self.x += 1

    if self.x < 0:
      self.x = 0
    elif self.x > 2:
      self.x = 2

    if self.y < 0:
      self.y = 0
    elif self.y > 2:
      self.y = 2

  def get_key(self):
    return self.keys[self.y][self.x]

  def solve(self, insts):
    out = ''

    for line in insts:
      for d in line:
        self.move(d)

      out += f'{self.get_key()}'

    return out


class WorseKeypad(Keypad):
  keys = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
  ]

  def __init__(self):
    super().__init__(0, 2)

  def move(self, direction):
    dx = 0
    dy = 0

    if direction == 'U':
      dy = -1
    elif direction == 'D':
      dy = 1
    elif direction == 'L':
      dx = -1
    elif direction == 'R':
      dx = 1

    if (0 <= self.x + dx <= 4) and (0 <= self.y + dy <= 4) and self.keys[self.y + dy][self.x + dx] is not None:
      self.x += dx
      self.y += dy



def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()

  keypad = Keypad()

  return keypad.solve(pi)

def part2():
  pi = parse_input()

  keypad = WorseKeypad()

  return keypad.solve(pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
