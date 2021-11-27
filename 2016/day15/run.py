#!/usr/bin/env python3

from os.path import dirname, realpath
from re import findall
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input() -> list[list[int]]:
  return [[int(m) for m in findall(r'(\d+).+?(\d+).+?(\d+)\.', line)[0]] for line in puzzle_input]


class Wheel:
  def __init__(self, wheel_num: int, num_positions: int, offset: int) -> None:
    self.wheel_num = wheel_num
    self.num_positions = num_positions
    self.offset = offset

  def __repr__(self) -> str:
    return f'Wheel #{self.wheel_num} - {self.num_positions} @ {self.offset}'

  def in_correct_position(self, tick: int) -> bool:
    return (self.offset + tick) % self.num_positions == (-self.wheel_num) % self.num_positions


def make_wheels(pi: list[list[int]]):
  return [Wheel(*line) for line in pi]

def solve(wheels: list[Wheel]) -> int:
  inc = 1
  tick = 1

  correct = []

  while wheels:
    for wheel in filter(lambda wheel: wheel.in_correct_position(tick), wheels):
      correct.append(wheel)
      inc *= wheel.num_positions
      wheels.remove(wheel)

    tick += inc

  return tick - inc


def part1():
  pi = parse_input()

  wheels = make_wheels(pi)

  return solve(wheels)

def part2():
  pi = parse_input()

  wheels = make_wheels(pi)

  wheels.append(Wheel(7, 11, 0))

  return solve(wheels)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
