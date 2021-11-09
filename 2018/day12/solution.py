#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  state = ["."] * 5 + list(data[0].split(": ")[1].strip()) + ["."]*5

  zero = 5

  rules = {}

  for line in data[2:]:
    work = line.split(" => ")

    rules[work[0]] = work[1].strip()


  for gen in range(20):
    next_state = state[:]
    for i in range(2,len(state)-2):
      search = "".join(state[i-2:i+3])
      next_state[i] = rules[search]
    state = next_state

    if "#" in state[:5] or "#" in state[-5:]:
      state = ["."]*5 + state + ["."]*5
      zero += 5

  total = 0

  for i in range(len(state)):
    if state[i] == "#":
      total += i - zero

  return total

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()

  state = ["."] * 5 + list(data[0].split(": ")[1].strip()) + ["."]*5

  zero = 5

  rules = {}

  for line in data[2:]:
    work = line.split(" => ")

    rules[work[0]] = work[1].strip()

  last_inc = 0
  last = 0
  count = 0
  gen = 0

  while True:
    next_state = state[:]
    for i in range(2,len(state)-2):
      search = "".join(state[i-2:i+3])
      next_state[i] = rules[search]
    state = next_state

    gen += 1

    total = 0

    for i in range(len(state)):
      if state[i] == "#":
        total += i - zero

    inc = total - last

    if inc == last_inc:
      last = total
      count += 1

      if count == 100:
        return (50000000000-gen)*inc + total
    else:
      last_inc = inc
      last = total
      count = 0

    if "#" in state[:5] or "#" in state[-5:]:
      state = ["."]*5 + state + ["."]*5
      zero += 5

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
