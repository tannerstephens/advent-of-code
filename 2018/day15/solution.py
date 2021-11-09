#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

class Node:
  def __init__(self, x, y, d):
    self.x = x
    self.y = y
    self.d = d

class Queue:
  def __init__(self):
    self.q = []
  
  def push(self, val):
    self.q.insert(0, val)
  
  def pop(self):
    return self.q.pop()

  def front(self):
    return self.q[0]

  def empty(self):
    return len(self.q) == 0

def BFS(cave, sx, sy, tx, ty):
  if cave[sy][sx] != "." or cave[ty][tx] != ".":
    return -1
  
  visited = [[None for _ in range(len(cave))] for _ in range(len(cave[0]))]

  visited[sy][sx] = 0

  q = Queue()
  q.push(Node(sx,sy,0))

  while not q.empty():
    c = q.front()

    if c.x == tx and c.y == ty:
      return visited
    
    q.pop()

    for move in ((0,1),(0,-1),(1,0),(-1,0)):
      (dx,dy) = move

      x = c.x + dx
      y = c.y + dy

      if x < 0 or x >= len(cave[0]) or y < 0 or y >= len(cave):
        continue
      
      if cave[y][x] != ".":
        continue
      
      if visited[y][x] != None:
        continue
      
      visited[y][x] = c.d + 1
      q.push(Node(x,y,c.d + 1))
  
  return -1

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()
  return None

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()
  return None

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
