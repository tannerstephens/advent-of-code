#!/usr/bin/env python3

from os.path import dirname, realpath
from typing import Union
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [line.split() for line in puzzle_input]


class Scrambler:
  def __init__(self, rules: list[list[str]]) -> None:
    self.rules = rules

  def _swap_position(self, x: int, y: int, s: list[str]) -> list[str]:
    s[x], s[y] = s[y], s[x]

    return s

  def _swap_letters(self, a: str, b: str, s: list[str]) -> list[str]:
    x = s.index(a)
    y = s.index(b)

    return self._swap_position(x, y, s)

  def _rotate(self, right: bool, steps: int, s: list[str]) -> list[str]:
    fixed_steps = (steps % len(s)) * -(2*right - 1)

    s = s[fixed_steps:] + s[:fixed_steps]

    return s

  def _rotate_position(self, a: str, s: list[str]) -> list[str]:
    x = s.index(a)

    steps = x + 1 + (x >= 4)

    return self._rotate(True, steps, s)

  def _reverse(self, x: int, y: int, s: list[str]) -> list[str]:
    return s[:x] + s[x:y+1][::-1] + s[y+1:]

  def _move(self, x: int, y: int, s: list[str]) -> list[str]:
    c = s[x]

    s = s[:x] + s[x+1:]
    s = s[:y] + [c] + s[y:]

    return s

  def _unrotate(self, a: str, s: list[str]) -> list[str]:
    target_index = (7,0,4,1,5,2,6,3)

    end_index = s.index(a)

    start_index = target_index[end_index]

    shift = start_index - end_index

    return self._rotate(start_index > end_index, abs(shift), s)

  def scramble(self, s: Union[str, list[str]]) -> str:
    list_s = list(s)

    for rule in self.rules:
      if rule[0] == 'swap':
        if rule[1] == 'position':
          list_s = self._swap_position(int(rule[2]), int(rule[5]), list_s)
        else:
          list_s = self._swap_letters(rule[2], rule[5], list_s)
      elif rule[0] == 'rotate':
        if rule[1] == 'based':
          list_s = self._rotate_position(rule[6], list_s)
        else:
          list_s = self._rotate(rule[1] == 'right', int(rule[2]), list_s)
      elif rule[0] == 'reverse':
        list_s = self._reverse(int(rule[2]), int(rule[4]), list_s)
      elif rule[0] == 'move':
        list_s = self._move(int(rule[2]), int(rule[5]), list_s)
      elif rule[0] == 'unrotate':
        list_s = self._unrotate(rule[1], list_s)

    return ''.join(list_s)


def reverse_rules(puzzle_input: list[list[str]]) -> list[list[str]]:
  out = []

  for rule in puzzle_input:
    work = rule
    if rule[0] == 'swap':
      pass
    elif rule[0] == 'rotate':
      if rule[1] == 'based':
        work = ['unrotate', rule[6]]
      else:
        work[1] = 'left' if work[1] == 'right' else 'right'
    elif rule[0] == 'reverse':
      pass
    elif rule[0] == 'move':
      work[2], work[5] = work[5], work[2]

    out.append(work)

  return out[::-1]


def part1():
  pi = parse_input()

  scrambler = Scrambler(pi)

  return scrambler.scramble('abcdefgh')

def part2():
  pi = parse_input()

  scrambler = Scrambler(reverse_rules(pi))

  return scrambler.scramble('fbgdceah')


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
