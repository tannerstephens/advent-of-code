#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  out = {}

  for line in puzzle_input:
    work = line.split(' ')

    name = work[0]
    speed = int(work[3])
    active = int(work[6])
    rest = int(work[13])

    out[name] = [speed, active, rest]

  return out

def get_distance(deer, time):
  full_cycle_time = deer[1] + deer[2]
  full_cycles = time//full_cycle_time

  remaining_time = time - (full_cycle_time*full_cycles)

  if remaining_time > deer[1]:
    extra = deer[1]
  else:
    extra = remaining_time

  distance = deer[0]*deer[1]*full_cycles + deer[0]*max(0, extra)

  return distance

def part1():
  pi = parse_input()

  time = 2503

  return max(map(lambda d: get_distance(pi[d], time), pi))

def part2():
  pi = parse_input()

  deer = {}

  for deer_name in pi:
    deer[deer_name] = 0

  for t in range(1, 2503):
    distances = list(map(lambda d: (d, get_distance(pi[d], t)), pi))

    lead = max(distances, key=lambda e: e[1])

    for d in distances:
      if d[1] == lead[1]:
        deer[d[0]] += 1

  return deer[max(deer, key=lambda d: deer[d])]


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
