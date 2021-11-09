#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

from re import findall

def parse_input():
  out = []

  for line in puzzle_input:
    work = findall(r'Sue \d+: (.+): (\d+), (.+): (\d+), (.+): (\d+)', line)[0]

    out.append({
      work[0]: int(work[1]),
      work[2]: int(work[3]),
      work[4]: int(work[5])
    })

  return out

aunty = {
  'children': 3,
  'cats': 7,
  'samoyeds': 2,
  'pomeranians': 3,
  'akitas': 0,
  'vizslas': 0,
  'goldfish': 5,
  'trees': 3,
  'cars': 2,
  'perfumes': 1
}

def is_aunty(sue):
  for key in sue:
    if aunty[key] != sue[key]:
      return False
  return True

def is_actually_aunty(sue):
  for key in sue:
    if key in ['cats', 'trees']:
      if aunty[key] >= sue[key]:
        return False

    elif key in ['pomeranians', 'goldfish']:
      if aunty[key] <= sue[key]:
        return False

    elif aunty[key] != sue[key]:
      return False

  return True

def part1():
  pi = parse_input()

  for i, sue in enumerate(pi):
    if is_aunty(sue):
      return i+1

def part2():
  pi = parse_input()

  for i, sue in enumerate(pi):
    if is_actually_aunty(sue):
      return i+1

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
