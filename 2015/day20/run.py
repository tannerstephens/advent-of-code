#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return int(puzzle_input[0])

def num_presents(house_num):
  f = {house_num}

  for i in range(1, house_num//2):
    if house_num%i == 0:
      f.add(i)
      f.add(house_num//i)

  return sum(f)

def part1():
  pi = parse_input()

  houses = [0 for _ in range(pi//10)]

  for elf in range(1, len(houses)):
    for house in range(elf, len(houses), elf):
      houses[house] += elf*10

  for i, house in enumerate(houses):
    if house >= pi:
      return i

def part2():
  pi = parse_input()

  houses = [0 for _ in range(pi//10)]

  for elf in range(1, len(houses)):
    c = 0
    for house in range(elf, len(houses), elf):
      houses[house] += elf*11
      c += 1

      if c == 50:
        break

  for i, house in enumerate(houses):
    if house >= pi:
      return i

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
