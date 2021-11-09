#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]

def look_and_say(s):
  out = ''

  look = s[0]
  say = 1
  for c in s[1:]:
    if c != look:
      out += f'{say}{look}'
      look = c
      say = 1
    else:
      say += 1

  out += f'{say}{look}'
  return out

def part1():
  pi = parse_input()

  for _ in range(40):
    pi = look_and_say(pi)

  return len(pi)

def part2():
  pi = parse_input()

  for _ in range(50):
    pi = look_and_say(pi)

  return len(pi)


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
