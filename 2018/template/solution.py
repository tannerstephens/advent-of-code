#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()
  return None

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()
  return None

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
