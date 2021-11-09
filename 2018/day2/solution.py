#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  counts = {2: 0, 3: 0}

  for item in data:
    ck = [2,3]
    letters = set(item)

    for c in letters:
      for k in ck:
        if item.count(c) == k:
          counts[k] += 1
          ck.remove(k)
          continue

  return counts[2]*counts[3]

def part2():
  
  def difference(id1, id2):
    different = 0
    for ck in zip(id1, id2):
      if ck[0] != ck[1]:
        different += 1
    
    return different

  def findKeys(data):
    for item1 in data:
      for item2 in data:
        if item2 == item1:
          continue
        else:
          if difference(item1, item2) == 1:
            return item1, item2


  with open(directory + "/input") as f:
    data = f.readlines()

  item1, item2 = findKeys(data)

  out = ""

  for c in zip(item1, item2):
    if c[0] == c[1]:
      out += c[0]

  return out.strip()


def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
