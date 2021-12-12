#!/usr/bin/env python3

from os.path import dirname, realpath
from collections import defaultdict
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  graph: defaultdict[str, list[str]] = defaultdict(list)

  for line in puzzle_input:
    left, right = line.split('-')

    graph[left].append(right)
    graph[right].append(left)

  return graph


def dfs(graph: dict[str, list[str]], current_node: str, seen: set = None, two = False, limit_hit = False):
  if seen is None:
    seen = set()

  if current_node == 'start' and current_node in seen:
    return 0

  if current_node in seen and ((limit_hit and two) or (not two)):
    return 0

  if current_node == 'end':
    return 1

  if current_node.islower():
    if current_node in seen:
      limit_hit = True
    else:
      seen.add(current_node)

  valid_paths = 0

  for node in graph[current_node]:
    valid_paths += dfs(graph, node, seen.copy(), two, limit_hit)

  return valid_paths

def part1():
  pi = parse_input()

  return dfs(pi, 'start')

def part2():
  pi = parse_input()

  return dfs(pi, 'start', two=True)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
