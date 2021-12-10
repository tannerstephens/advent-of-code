#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [line for line in puzzle_input]

PUSH = {'(', '[', '{', '<'}

REVERSE = {
  ')': '(',
  ']': '[',
  '}': '{',
  '>': '<',
}

def find_syntax_error(line: str, cache: dict = None) -> str:
  stack = []

  for c in line:
    if c in PUSH:
      stack.append(c)
    else:
      r = stack.pop()
      if REVERSE[c] != r:
        return c

  if cache is not None:
    cache[line] = stack

  return ''

def part1():
  pi = parse_input()

  count = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0,
    '': 0
  }

  for line in pi:
    c = find_syntax_error(line)

    count[c] += 1

  return 3*count[')'] + 57*count[']'] + 1197*count['}'] + 25137*count['>']


CLOSE = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

def complete_line(line: str, stacks: dict) -> str:
  stack = stacks[line]

  return ''.join(map(lambda c: CLOSE[c], stack[::-1]))

SCORES = {')': 1, ']': 2, '}': 3, '>': 4}

def score_closer(closer: str) -> int:
  score = 0

  for c in closer:
    score *= 5
    score += SCORES[c]

  return score


def part2():
  pi = parse_input()

  stacks = {}

  incomplete_lines = filter(lambda line: find_syntax_error(line, stacks) == '', pi)

  closers = map(lambda line: complete_line(line, stacks), incomplete_lines)

  scores = sorted(map(score_closer, closers))

  return scores[len(scores) // 2]

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
