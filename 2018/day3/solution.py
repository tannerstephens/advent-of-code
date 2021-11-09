#!/usr/bin/python3

import os, pprint

directory = os.path.dirname(os.path.realpath(__file__))

def parse_input(data):
  claims = []
  
  for line in data:
    work = line.split(" ")
    cid = int(work[0][1:])
    left = int(work[2].split(",")[0])
    top = int(work[2].split(",")[1][:-1])
    width = int(work[3].split("x")[0])
    height = int(work[3].split("x")[1])

    claims.append(dict(cid=cid, left=left,top=top,width=width,height=height))
  
  return claims

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  claims = parse_input(data)

  claimed = set()
  double_claimed = set()

  for claim in claims:
    for x in range(claim["left"], claim["left"] + claim["width"]):
      for y in range(claim["top"], claim["top"] + claim["height"]):
        if (x,y) in claimed and (x,y) not in double_claimed:
          double_claimed.add((x,y))
        else:
          claimed.add((x,y))
  

  return len(double_claimed)

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()

  claims = parse_input(data)

  claimed = {}

  overlaps = []

  cids = []

  for claim in claims:
    cids.append(claim["cid"])
    for x in range(claim["left"], claim["left"] + claim["width"]):
      for y in range(claim["top"], claim["top"] + claim["height"]):
        if (x,y) in claimed:
          if claim["cid"] not in overlaps:
            overlaps.append(claim["cid"])

          if claimed[(x,y)] not in overlaps:
            overlaps.append(claimed[(x,y)])
        else:
          claimed[(x,y)] = claim["cid"]

  for cid in cids:
    if cid not in overlaps:
      return cid

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
