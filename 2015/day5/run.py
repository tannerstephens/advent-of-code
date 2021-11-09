#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

VOWELS = {'a', 'e', 'i', 'o', 'u'}
BAD_STRINGS = {'ab', 'cd', 'pq', 'xy'}

def is_nice(s):
  vowels = int(s[-1] in VOWELS)
  has_double = False
  has_bad = False
  for i in range(len(s)-1):
    vowels += s[i] in VOWELS
    has_double = has_double or (s[i] == s[i+1])
    has_bad = has_bad or (s[i:i+2] in BAD_STRINGS)

  return (vowels >= 3) and (has_double) and (not has_bad)

def is_actually_nice(s):
  space_repeat = False
  pair = False

  for i in range(len(s)-2):
    pair = pair or (s[i:i+2] in s[i+2:])
    space_repeat = space_repeat or (s[i] == s[i+2])

    if pair and space_repeat:
      return True

  return False

def parse_input():
  return puzzle_input[:]

def part1():
  pi = parse_input()

  nice = 0

  for line in pi:
    nice += is_nice(line)

  return nice

def part2():
  pi = parse_input()

  nice = 0

  for line in pi:
    nice += is_actually_nice(line)

  return nice

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
