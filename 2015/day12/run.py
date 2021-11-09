#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from re import findall
from json import loads

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]

def part1():
  pi = parse_input()

  return sum(map(int, findall(r'-?\d+', pi)))

def traverse(obj):
  s = 0
  t = type(obj)

  if t is int:
    return obj
  elif t is str:
    return 0
  elif t is list:
    for elem in obj:
      s += traverse(elem)
  elif t is dict:
    if 'red' in obj.values():
      return 0

    for key in obj:
      s += traverse(obj[key])

  return s

def part2():
  pi = parse_input()

  data = loads(pi)

  return traverse(data)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
