#!/usr/bin/env python3

from math import inf
from os.path import dirname, realpath

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[int(n) for n in line] for line in puzzle_input]


def bfs(pi: list[list[int]]) -> int:
  scores = [[999999999999 for x in pi[0]] for y in pi]

  scores[0][0] = 0

  edge = [(0,0)]

  while edge:
    new_edge = set()

    m = 99999999999

    for x, y in edge:
      e_score = scores[y][x]

      if e_score > m:
        new_edge.append((x, y))
        continue

      for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= len(pi[0]) or ny < 0 or ny >= len(pi):
          continue

        n_score = pi[ny][nx] + e_score

        if n_score < scores[ny][nx]:
          scores[ny][nx] = n_score

          n_score = min(m, n_score)

          new_edge.add((nx, ny))

    edge = new_edge

  return scores[-1][-1]


def get_min_node(visited, scores, possible):
  m = inf

  m_c = None

  for x,y in possible:
    if visited[y][x]:
      continue

    if scores[y][x] < m:
      m = scores[y][x]
      m_c = (x, y)

  return m_c


def dijkstra(pi: list[list[int]]) -> int:
  visited = [[False for x in pi[0]] for y in pi]
  scores = [[inf for x in pi[0]] for y in pi]

  scores[0][0] = 0

  nxt = (0,0)

  possible = set()

  while not visited[-1][-1]:
    x,y = nxt
    c_score = scores[y][x]

    for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
      nx = x + dx
      ny = y + dy

      if nx < 0 or nx >= len(pi[0]) or ny < 0 or ny >= len(pi):
        continue

      if visited[ny][nx]:
        continue

      scores[ny][nx] = min(scores[ny][nx], c_score + pi[ny][nx])

      possible.add((nx, ny))

    visited[y][x] = True

    nxt = get_min_node(visited, scores, possible)
    possible.discard(nxt)

  return scores[-1][-1]

def part1():
  pi = parse_input()

  return bfs(pi)

def build_big_pi(pi: list[list[int]]):
  out = [[None for x in range(len(pi[0])*5)] for y in range(len(pi)*5)]

  for y, line in enumerate(pi):
    for x, v in enumerate(line):
      for dx in range(5):
        for dy in range(5):
          nv = ((v + dx + dy) % 10) + ((v + dx + dy) > 9)

          out[y + len(pi)*dy][x + len(pi[0])*dx] = nv

  return out

def part2():
  pi = parse_input()

  big_pi = build_big_pi(pi)

  return dijkstra(big_pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
