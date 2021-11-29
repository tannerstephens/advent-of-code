#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return int(puzzle_input[0])



def play(num_elves: int) -> int:
  elf_circle = [i+1 for i in range(num_elves)]

  while len(elf_circle) > 1:
    if len(elf_circle) % 2 == 0:
      elf_circle = elf_circle[::2]
    else:
      elf_circle = elf_circle[2::2]

  return elf_circle[0]


def play2(num_elves: int) -> int:
  class Elf:
    def __init__(self, prev, next, i: int) -> None:
      self.i = i
      self.next = next
      self.prev = prev

    def __repr__(self) -> str:
      return f'Elf #{self.i}'

  prev = None

  elf_one = Elf(None, None, 1)
  prev = elf_one

  mid = None

  for i in range(1, num_elves):
    n = Elf(prev, None, i+1)
    prev.next = n
    prev = n

    if i == num_elves // 2:
      mid = n

  prev.next = elf_one
  elf_one.prev = prev
  elf = elf_one

  l = num_elves

  while l != 1:
    p = mid.prev
    n = mid.next

    mid.prev.next = mid.next
    mid.next.prev = mid.prev

    l -= 1

    mid = mid.next

    if l % 2 == 0:
      mid = mid.next

    elf = elf.next

  return elf.i

def part1():
  elves = parse_input()

  return play(elves)

def part2():
  pi = parse_input()

  return play2(pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
