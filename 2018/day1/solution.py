#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  with open(directory + "/input") as f:
    data = [int(l) for l in f.readlines()]

  return sum(data)

def part2():
  with open(directory + "/input") as f:
    data = [int(l) for l in f.readlines()]

  f = 0
  visited = set()
  i = 0
  while f not in visited:
    visited.add(f)
    f += data[i]
    i = (i+1) % len(data)

  return f

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()


