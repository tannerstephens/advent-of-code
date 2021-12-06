#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [int(n) for n in puzzle_input[0].split(',')]


class ReproductionGroup:
  def __init__(self) -> None:
    self.next = None
    self.n = 0


class School:
  def __init__(self, starting_fish: list[int]) -> None:
    self.reproduction_groups = [ReproductionGroup() for _ in range(9)]

    for fish in starting_fish:
      self.reproduction_groups[fish].n += 1

    for i, group in enumerate(self.reproduction_groups):
      if i == 0:
        group.next = self.reproduction_groups[6]
      else:
        group.next = self.reproduction_groups[i-1]

  def tick(self):
    zero_amnt = self.reproduction_groups[0].n
    six_amnt = self.reproduction_groups[6].n

    for i, group in enumerate(self.reproduction_groups):
      if i == 7:
        group.next.n += group.n
      elif i == 6:
        group.next.n = six_amnt
      else:
        group.next.n = group.n

    self.reproduction_groups[8].n = zero_amnt

  def count_fish(self):
    return sum(group.n for group in self.reproduction_groups)

  def __repr__(self) -> str:
    return '[' + ', '.join(str(group.n) for group in self.reproduction_groups) + ']'


def simulate(pi: list[int], days: int) -> int:
  school = School(pi)

  for _ in range(days):
    school.tick()

  return school.count_fish()

def part1():
  pi = parse_input()

  return simulate(pi, 80)



def part2():
  pi = parse_input()

  return simulate(pi, 256)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
