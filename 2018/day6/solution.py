#!/usr/bin/python3

import os, math

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  extra = 0

  with open(directory + "/input") as f:
    data = f.readlines()

  coords = []

  for line in data:
    work = line.split(", ")
    coords.append((int(work[0]) + extra, int(work[1][:-1]) + extra))

  w = max(coords, key=lambda k: k[0])[0] + extra
  h = max(coords, key=lambda k: k[1])[1] + extra

  base = 65

  counts = {}

  for x in range(w):
    for y in range(h):
      m = math.inf
      k = None
      for i,coord in enumerate(coords):
        distance = abs(coord[0] - x) + abs(coord[1] - y)

        if distance == m:
          k = "."
        elif distance < m:
          m = distance
          k = chr(base + i)

      if k not in counts:
        counts[k] = 1
      else:
        counts[k] += 1

      if (x==0 or x==(w-1) or y == 0 or y==(h-1)):
        counts[k] = -math.inf

  return counts[max(counts, key=lambda k: counts[k])]


def part2():
  extra = 0

  with open(directory + "/input") as f:
    data = f.readlines()

  coords = []

  for line in data:
    work = line.split(", ")
    coords.append((int(work[0]) + extra, int(work[1][:-1]) + extra))

  w = max(coords, key=lambda k: k[0])[0] + extra
  h = max(coords, key=lambda k: k[1])[1] + extra

  search = 10000

  safe_area_size = 0

  for x in range(w):
    for y in range(h):
      d_sum = 0
      good = True
      for i,coord in enumerate(coords):
        distance = abs(coord[0] - x) + abs(coord[1] - y)

        d_sum += distance

        if d_sum >= search:
          good = False
          break

      if good:
        safe_area_size += 1

        

  return safe_area_size

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
