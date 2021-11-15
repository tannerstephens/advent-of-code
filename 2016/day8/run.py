#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [line.split(' ') for line in puzzle_input]


class Screen:
  def __init__(self, width=50, height=6) -> None:
    self.width = width
    self.height = height

    self.pixels = [[False for x in range(width)] for y in range(height)]

  def rect(self, width, height, pixel_fn=lambda pixel: True):
    for y in range(height):
      for x in range(width):
        self.pixels[y][x] = pixel_fn(self.pixels[y][x])

  def rotate_row(self, row, by):
    old_row = self.pixels[row]
    new_row = [None] * self.width

    for i, v in enumerate(old_row):
      new_row[(i+by) % self.width] = v

    self.pixels[row] = new_row

  def rotate_column(self, column, by):
    new_column = [None]*self.height

    for i, v in enumerate(self.pixels):
      new_column[(i + by) % self.height] = v[column]

    for i in range(self.height):
      self.pixels[i][column] = new_column[i]

  def run_line(self, line):
    if line[0] == 'rect':
      w,h = [int(v) for v in line[1].split('x')]

      self.rect(w,h)
    else:
      row_col = int(line[2][2:])
      by = int(line[-1])

      if line[1] == 'row':
        self.rotate_row(row_col, by)
      else:
        self.rotate_column(row_col, by)

  def count_pixels(self):
    count = 0

    for row in self.pixels:
      count += row.count(True)

    return count

  def __repr__(self):
    out = ''
    for row in self.pixels:
      out += ''.join(map(lambda p: '#' if p else ' ', row)) + '\n'

    return out

def part1():
  pi = parse_input()

  screen = Screen()

  for line in pi:
    screen.run_line(line)

  return screen.count_pixels()

def part2():
  return 'VISUAL PUZZLE'



def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
