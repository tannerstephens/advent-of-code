#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

from operator import add, mul

def parse_input():
  for line in puzzle_input:
    yield parse_line(line)

def parse_line(line):
  stack = []

  for c in line[::-1]:
    if c == ' ':
      continue

    if c.isdigit():
      stack.append(int(c))
    else:
      stack.append(c)
  return stack

OPS = {
  '+': add,
  '*': mul
}

def resolve(problem):
  while len(problem) > 1:
    l = problem.pop()

    if l == '(':
      l = resolve(problem)

      if len(problem) == 0:
        return l

    op = problem.pop()

    if op == ')':
      return l

    r = problem.pop()

    if r == '(':
      r = resolve(problem)

    problem.append(OPS[op](l, r))

  return problem.pop()

def solve2(problem):
  skipped = []
  while len(problem) > 1:
    l = problem.pop()

    if l == '(':
      l = solve2(problem)

      if len(problem) == 0:
        skipped += [l]
        break

    op = problem.pop()

    if op == ')':
      return resolve(skipped + [l])

    if op == '*':
      skipped += [l, op]
    else:
      r = problem.pop()

      if r == '(':
        r = solve2(problem)

      problem.append(l+r)

  return resolve(skipped + problem)

def part1():
  pi = parse_input()

  s = 0
  for problem in pi:
    s += resolve(problem)

  return s


def part2():
  pi = parse_input()

  s = 0

  for problem in pi:
    s += solve2(problem)

  return s

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
