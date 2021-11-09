#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from re import finditer

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  rules = puzzle_input[:-2]
  start = puzzle_input[-1]

  return rules, start

def build_transformation_dict(rules):
  out = {}

  for rule in rules:
    work = rule.split(' => ')

    if work[0] not in out:
      out[work[0]] = []
    out[work[0]].append(work[1])

  return out

def build_reverse_dict(rules):
  out = {}

  for rule in rules:
    work = rule.split(' => ')

    out[work[1]] = work[0]

  return out

def start_indexes(s, search):
  l = len(search)
  for i in range(len(s)-l+1):
    if s[i:i+l] == search:
      yield i


def part1():
  rules, start = parse_input()

  t_dict = build_transformation_dict(rules)

  transforms = set()

  for key in t_dict:
    for i in start_indexes(start, key):
      for replace in t_dict[key]:
        transforms.add(start[:i] + replace + start[i+len(key):])

  return len(transforms)

def part2():
  rules, m = parse_input()

  r_dict = build_reverse_dict(rules)

  c = 0

  while m != 'e':
    pos = []
    for key in r_dict:
      if key in m:
        pos.append(key)

    use = max(pos, key=len)
    m = m.replace(use, r_dict[use], 1)
    c += 1

  return c




def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
