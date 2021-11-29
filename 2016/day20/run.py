#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[int(n) for n in line.split('-')] for line in puzzle_input]


def clean_ranges(pi: list[list[int]]) -> list[list[int]]:
  sorted_pi = sorted(pi)

  work = sorted_pi[0]

  out = []

  for line in sorted_pi[1:]:
    if line[0] <= work[1] + 1:
      work[1]  = max(work[1], line[1])

    else:
      out.append(work)
      work = line

  out.append(work)

  return out

def part1():
  pi = parse_input()

  sorted_ranges = sorted(pi)

  prev = sorted_ranges[0]

  for nxt in sorted_ranges[1:]:
    if nxt[0] > prev[1]+1:
      return prev[1] + 1

    prev = nxt

def part2():
  pi = parse_input()

  cleaned = clean_ranges(pi)

  t = 0

  for i, r in enumerate(cleaned[:-1]):
    t += cleaned[i+1][0] - r[1] - 1

  t += 4294967295 - cleaned[-1][1]

  return t


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
