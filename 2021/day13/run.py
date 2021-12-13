#!/usr/bin/env python3


from os.path import dirname, realpath
from re import compile

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  pi = iter(puzzle_input)

  points: list[tuple[int, int]] = []

  while (line := next(pi)) != '':
    x,y = line.split(',')
    points.append((int(x), int(y)))

  insts: list[tuple[str, int]] = []

  r = compile(r'([xy])=(\d+)')

  for line in pi:
    xy, n = r.search(line).groups()
    insts.append((xy, int(n)))

  return points, insts


class InfiniteArray:
  def __init__(self, starting_value_factory = lambda: None, starting_length = 100):
    self.starting_value_factory = starting_value_factory

    self.values = [starting_value_factory() for _ in range(starting_length)]

  def _extend(self, target_length):
    e = target_length - len(self.values) + 1
    self.values.extend([self.starting_value_factory() for _ in range(e)])

  def __getitem__(self, key):
    if isinstance(key, int):
      if key >= len(self.values):
        self._extend(key)

    return self.values[key]

  def __setitem__(self, key, value):
    if key >= len(self.values):
      self._extend(key)

    self.values[key] = value

  def __len__(self):
    return len(self.values)

  def __iter__(self):
    return iter(self.values)

  def count(self, value):
    return self.values.count(value)



class Paper:
  def __init__(self, points):
    self.grid = InfiniteArray(lambda: InfiniteArray(lambda: False))

    for x,y in points:
      self.grid[y][x] = True

  def __repr__(self):
    out = ''

    for line in self.grid:
      out += ''.join(map(lambda v: '#' if v else ' ', line)) + '\n'

    return out

  def count(self):
    return sum(line.count(True) for line in self.grid)

  def _fold_left(self, index: int):
    for y in range(len(self.grid)):
      if len(self.grid[y]) > index+1:
        for offset in range(len(self.grid[y]) - index):
          self.grid[y][index - offset - 1] |= self.grid[y][index + offset + 1]

        new_grid = InfiniteArray(lambda: False, 0)
        new_grid.values = self.grid[y][:index]
        self.grid[y] = new_grid

  def _fold_up(self, index: int):
    for offset in range(len(self.grid) - index):
      for x in range(len(self.grid[index + offset + 1])):
        self.grid[index - offset - 1][x] |= self.grid[index + offset + 1][x]

    new_grid = InfiniteArray(lambda: InfiniteArray(lambda: False), 0)
    new_grid.values = self.grid[:index]
    self.grid = new_grid

  def fold(self, direction: str, index: int):
    if direction == 'x':
      self._fold_left(index)
    elif direction == 'y':
      self._fold_up(index)


def part1():
  points, insts = parse_input()

  paper = Paper(points)

  xy, index = insts[0]

  paper.fold(xy, index)

  return paper.count()

def part2():
  points, insts = parse_input()

  paper = Paper(points)

  for xy, index in insts:
    paper.fold(xy, index)

  return '\n' + repr(paper)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
