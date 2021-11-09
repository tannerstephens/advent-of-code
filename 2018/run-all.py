#!/usr/bin/python3

import importlib.util, glob
from datetime import datetime

def loadDay(directory):
  spec = importlib.util.spec_from_file_location("aoc.fun", directory + "solution.py")
  day = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(day)

  return (day.part1, day.part2)

def timeFunction(f):
  start = datetime.now()
  r = f()
  t = (datetime.now() - start).total_seconds()
  return (r,t)

def runDay(directory):
  f = loadDay(directory)
  p1 = timeFunction(f[0])
  p2 = timeFunction(f[1])

  return p1, p2

def main():
  print("\u001b[32;1mAdvent \u001b[34;1mof \u001b[31;1mCode \u001b[0m2018")

  dirs = sorted(list(glob.glob("./day*/")), key=lambda k: int(k.split("day")[1][:-1]))

  for directory in dirs:
    p1,p2 = runDay(directory)
    day = directory.split("day")[1][:-1]
    print("\u001b[33;1mDay", day)
    print("\u001b[36;1m  Part 1")
    print("\u001b[32m   ", p1[0])
    print("\u001b[0m   ", p1[1])
    print("\u001b[36;1m  Part 2")
    print("\u001b[32m   ", p2[0])
    print("\u001b[0m   ", p2[1])
    print("")

if __name__ == "__main__":
  main()
