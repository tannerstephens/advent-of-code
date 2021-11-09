#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

# Stack-based reduce is faster because List.pop() is O(1) at end of list and O(N) in middle

def reduce(poly):
  string = poly
  stack = [string.pop()]
  while string:
      if not stack:
          stack.append(string.pop())
      if stack[len(stack)-1] == string[len(string)-1].swapcase():
          stack.pop()
          string.pop()
      else:
          stack.append(string.pop())
  return stack

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  poly = list(data[0].strip())

  poly = reduce(poly)
  
  return len(poly)

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()[0].strip()

  data = "".join(reduce(list(data)))

  units = []

  for o in range(65,91):
    c = chr(o)
    unit = (c.lower(),c.upper())
    if unit not in units:
      units.append(unit)
  
  lens = dict()

  for unit in units:
    test_poly = list(data.replace(unit[0], "").replace(unit[1], ""))

    rpoly = reduce(test_poly)

    lens[str(unit)] = len(rpoly)
  

  return lens[min(lens, key = lambda k: lens[k])]

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
