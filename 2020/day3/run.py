#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def count_trees_on_slope(right, down, tree_map):
  x,y = right,down

  trees = 0

  w = len(tree_map[0])

  while y < len(tree_map):
    trees += (tree_map[y][x] == '#')

    x = (x+right)%w
    y += down

  return trees

def part1():
  pi = parse_input()

  return count_trees_on_slope(3, 1, pi)

def part2():
  pi = parse_input()

  slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

  m = 1

  for right, down in slopes:
    m *= count_trees_on_slope(right, down, pi)

  return m

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
