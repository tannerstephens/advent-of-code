#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read()

class CrazyInt:
  def __init__(self, v):
    self.v = v

  def __add__(self, o):
    return CrazyInt(self.v + o.v)

  def __sub__(self, o):
    return CrazyInt(self.v * o.v)

class CrazyInt2:
  def __init__(self, v):
    self.v = v

  def __add__(self, o):
    return CrazyInt2(self.v * o.v)

  def __mul__(self, o):
    return CrazyInt2(self.v + o.v)

def part1_parse():
  work = puzzle_input.translate({
    42: '-',
    48: 'CrazyInt(0)',
    49: 'CrazyInt(1)',
    50: 'CrazyInt(2)',
    51: 'CrazyInt(3)',
    52: 'CrazyInt(4)',
    53: 'CrazyInt(5)',
    54: 'CrazyInt(6)',
    55: 'CrazyInt(7)',
    56: 'CrazyInt(8)',
    57: 'CrazyInt(9)'
  })

  return work.split('\n')[:-1]

def part2_parse():
  work = puzzle_input.translate({
    42: '+',
    43: '*',
    48: 'CrazyInt2(0)',
    49: 'CrazyInt2(1)',
    50: 'CrazyInt2(2)',
    51: 'CrazyInt2(3)',
    52: 'CrazyInt2(4)',
    53: 'CrazyInt2(5)',
    54: 'CrazyInt2(6)',
    55: 'CrazyInt2(7)',
    56: 'CrazyInt2(8)',
    57: 'CrazyInt2(9)'
  })

  return work.split('\n')[:-1]

def part1():
  pi = part1_parse()

  s = 0

  for line in pi:
    s += eval(line).v

  return s

def part2():
  pi = part2_parse()

  s = 0

  for line in pi:
    s += eval(line).v

  return s

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
