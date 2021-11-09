#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from itertools import permutations
from math import inf

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  lines = []

  for line in puzzle_input:
    work = line.split()

    lines.append((work[0], work[2], int(work[-1])))

  return lines

def create_distance_map(pi):
  distance_map = {}

  for line in pi:
    if line[0] not in distance_map:
      distance_map[line[0]] = {}

    if line[1] not in distance_map:
      distance_map[line[1]] = {}

    distance_map[line[0]][line[1]] = line[2]
    distance_map[line[1]][line[0]] = line[2]

  return distance_map

def get_route_length(distance_map, route):
  d = 0
  for i in range(len(route) - 1):
    d += distance_map[route[i]][route[i+1]]

  return d

## !!! - SO MUCH SLOWER
# def recursive_route_length(distance_map, route, lookup={}):
#   if len(route) == 1:
#     return 0

#   key = str(route)

#   if key in lookup:
#     return lookup[key]

#   res = distance_map[route[0]][route[1]] + recursive_route_length(distance_map, route[1:], lookup)
#   lookup[key] = res

#   return res


def get_shortest_distance(distance_map, systems):
  m = inf

  for route in permutations(systems, len(systems)):
    d = get_route_length(distance_map, route)

    if d < m:
      m = d

  return m

def get_longest_distance(distance_map, systems):
  m = 0

  for route in permutations(systems, len(systems)):
    d = get_route_length(distance_map, route)

    if d > m:
      m = d

  return m

def get_systems(pi):
  systems = set()

  for line in pi:
    systems.add(line[0])
    systems.add(line[1])

  return systems

def part1():
  pi = parse_input()

  distance_map = create_distance_map(pi)

  systems = get_systems(pi)

  return get_shortest_distance(distance_map, systems)

def part2():
  pi = parse_input()

  distance_map = create_distance_map(pi)

  systems = get_systems(pi)

  return get_longest_distance(distance_map, systems)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
