#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from itertools import tee
from collections import defaultdict

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  out = {}

  for line in puzzle_input[2:]:
    k, v = line.split(' -> ')
    out[tuple(k)] = v

  return puzzle_input[0], out

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def parse_polymer(polymer: str) -> list[str]:
  output = defaultdict(int)

  for pair in pairwise(polymer):
    output[pair] += 1

  return output


def evolve(polymer: defaultdict[tuple[str, str], int], template: dict[str, str]):
  new_polymer = defaultdict(int)

  counts = defaultdict(int)

  for key in polymer:
    value = polymer[key]
    r = template[key]

    new_polymer[(key[0], r)] += value
    new_polymer[(r, key[1])] += value

    counts[key[0]] += value
    counts[r] += value

  counts[key[1]] += 1

  return new_polymer, counts


def run(polymer, template, steps=10):
  polymer = parse_polymer(polymer)

  for _ in range(steps):
    polymer, counts = evolve(polymer, template)

  return max(counts.values()) - min(counts.values())

def part1():
  polymer, template = parse_input()

  return run(polymer, template)



def part2():
  polymer, template = parse_input()

  return run(polymer, template, 40)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
