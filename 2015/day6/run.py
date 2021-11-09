#!/usr/bin/env python3

from os.path import dirname, realpath
from functools import reduce
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]


FUNCTIONS = {
  'on': lambda n, b: n|b,
  'off': lambda n, b: n&b,
  'toggle': lambda n, b: n^b
}

def parse_input():
  actions = []
  for line in puzzle_input:
    work = line.split(' ')

    if work[0] == 'toggle':
      action = 'toggle'
      start = list(map(int, work[1].split(',')))
      stop = list(map(int, work[3].split(',')))
    else:
      action = work[1]
      start = list(map(int, work[2].split(',')))
      stop = list(map(int, work[4].split(',')))

    actions.append((action, start, stop))

  return actions

def make_light_grid():
  return [0 for _ in range(1000)]

def get_x_bin_string(action):
  left = action[1][0]
  right = action [2][0]

  return ('0'*(left-1)) + ('1'*(right-left+1)) + ('0'*(999-right))

def convert_bin_for_action(action, b):
  if action[0] == 'on' or action[0] == 'toggle':
    return b

  if action[0] == 'off':
    new_b = ''

    for c in b:
      new_b += '1' if c == '0' else '0'

    return new_b

def y_range(action):
  start = action[1][1]
  end = action[2][1]


  return range(start, end+1)

def part1():
  pi = parse_input()

  grid = make_light_grid()

  for action in pi:
    b = get_x_bin_string(action)

    b = convert_bin_for_action(action, b)

    b_n = int(b, 2)

    for y in y_range(action):
      grid[y] = FUNCTIONS[action[0]](grid[y], b_n)

  return reduce(lambda t, l: t + bin(l).count('1'), grid, 0)

CHANGE = {'off': -1, 'on': 1, 'toggle': 2}

def part2():
  pi = parse_input()

  grid = [[0 for __ in range(1000)] for _ in range(1000)]

  for action in pi:
    change = CHANGE[action[0]]

    for y in range(action[1][1], action[2][1]+1):
      for x in range(action[1][0], action[2][0]+1):
        grid[y][x] = max(grid[y][x] + change, 0)

  return reduce(lambda t, l: t + sum(l), grid, 0)




def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
