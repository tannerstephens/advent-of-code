#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from numpy import array
from numpy.linalg import lstsq

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

def parse_input():
  return int(puzzle_input[0]), puzzle_input[1].split(',')

def next_multiple(c, n):
  m = c%n

  return c + n - m

def part1():
  start, busses = parse_input()

  busses = map(int, filter(lambda b: b != 'x', busses))

  bus_id = min(busses, key=lambda n: next_multiple(start, n))

  return (next_multiple(start, bus_id) - start) * bus_id


def part2():
  busses = parse_input()[1]

  busses = list(map(lambda n: int(n) if n != 'x' else 'x', busses))

  increase = busses[0]

  t = next_multiple(100000000000000, increase)

  for i, bus in enumerate(busses[1:]):
    if bus == 'x':
      continue

    # While t + index_of_bus (i.e. bus ordering) mod bus_id != 0
    # check next valid time
    while (t+i+1)%bus != 0:
      t += increase

    # increase by super_multiple, to keep all previous mod resaults the same
    increase *= bus

  return t


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
