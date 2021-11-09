#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from collections import defaultdict

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

class Cube:
  def __init__(self, alive, x, y, z):
    self.alive = alive
    self.neighbors = []
    self.x = x
    self.y = y
    self.z = z

    self.next = alive

  def determine_next_state(self, cube_map):
    if len(self.neighbors):
      alive = sum(map(lambda n: n.alive, self.neighbors))
    else:
      # print(self.x, self.y, self.z)
      alive = 0
      for lx in range(self.x-1, self.x+2):
        for ly in range(self.y-1, self.y+2):
          for lz in range(self.z-1, self.z+2):
            if (lx == self.x) and (ly == self.y) and (lz == self.z):
              continue

            # print(lx, ly, lz)

            if cube_map[lz][ly][lx] is None:
              cube_map[lz][ly][lx] = Cube(False, lx, ly, lz)

            self.neighbors.append(cube_map[lz][ly][lx])

            alive += cube_map[lz][ly][lx].alive

            # print(cube_map[lz][ly][lx].alive)

    # print(alive)
    # input()

    if self.alive:
      self.next = (alive in (2,3))
    else:
      self.next = (alive == 3)

  def tick(self):
    self.alive = self.next

  def __repr__(self):
    if self.alive: return '#'
    return '.'


class Cube4:
  def __init__(self, alive, x, y, z, w):
    self.alive = alive
    self.neighbors = []
    self.x = x
    self.y = y
    self.z = z
    self.w = w

    self.next = alive

  def determine_next_state(self, cube_map):
    if len(self.neighbors):
      alive = sum(map(lambda n: n.alive, self.neighbors))
    else:
      # print(self.x, self.y, self.z)
      alive = 0
      for lx in range(self.x-1, self.x+2):
        for ly in range(self.y-1, self.y+2):
          for lz in range(self.z-1, self.z+2):
            for lw in range(self.w-1, self.w+2):
              if (lx == self.x) and (ly == self.y) and (lz == self.z) and (lw == self.w):
                continue

            # print(lx, ly, lz)

              if cube_map[lz][ly][lx][lw] is None:
                cube_map[lz][ly][lx][lw] = Cube4(False, lx, ly, lz, lw)

              self.neighbors.append(cube_map[lz][ly][lx][lw])

              alive += cube_map[lz][ly][lx][lw].alive

            # print(cube_map[lz][ly][lx].alive)

    # print(alive)
    # input()

    if self.alive:
      self.next = (alive in (2,3))
    else:
      self.next = (alive == 3)

  def tick(self):
    self.alive = self.next

  def __repr__(self):
    if self.alive: return '#'
    return '.'

def parse_input():
  return puzzle_input[:]

def print_cube_map(mnx, mxx, mny, mxy, mnz, mxz, cube_map):
  for z in range(mnz, mxz):
    print(f'z={z}')
    for y in range(mny, mxy):
      for x in range(mnx, mxx):
        print(cube_map[z][y][x], end='')

      print()
    print()

def part1():
  pi = parse_input()

  cube_map = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

  min_x = 0
  min_y = 0
  min_z = 0
  max_x = len(pi[0])
  max_y = len(pi)
  max_z = 1

  for y, line in enumerate(pi):
    for x, c in enumerate(line):
      cube_map[0][y][x] = Cube(c == '#', x, y, 0)

  for turn in range(6):
    # print(f'Turn {turn + 1}')
    # print_cube_map(min_x, max_x, min_y, max_y, min_z, max_z, cube_map)
    for z in range(min_z-1, max_z+1):
      for y in range(min_y-1, max_y+1):
        for x in range(min_x-1, max_x+1):
          if cube_map[z][y][x] is None:
            cube_map[z][y][x] = Cube(False, x, y, z)
          cube_map[z][y][x].determine_next_state(cube_map)

    for z in range(min_z-1, max_z+1):
      for y in range(min_y-1, max_y+1):
        for x in range(min_x-1, max_x+1):
          cube_map[z][y][x].tick()

    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1


  t = 0
  for z in range(min_z, max_z):
    for y in range(min_y, max_y):
      for x in range(min_x, max_x):
        t += cube_map[z][y][x].alive

  return t



def part2():
  pi = parse_input()

  cube_map = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None))))

  min_x = 0
  min_y = 0
  min_z = 0
  max_x = len(pi[0])
  max_y = len(pi)
  max_z = 1
  min_w = 0
  max_w = 1

  for y, line in enumerate(pi):
    for x, c in enumerate(line):
      cube_map[0][y][x][0] = Cube4(c == '#', x, y, 0, 0)

  for turn in range(6):
    # print(f'Turn {turn + 1}')
    # print_cube_map(min_x, max_x, min_y, max_y, min_z, max_z, cube_map)
    for z in range(min_z-1, max_z+1):
      for y in range(min_y-1, max_y+1):
        for x in range(min_x-1, max_x+1):
          for w in range(min_w-1, max_w+1):
            if cube_map[z][y][x][w] is None:
              cube_map[z][y][x][w] = Cube4(False, x, y, z, w)
            cube_map[z][y][x][w].determine_next_state(cube_map)

    for z in range(min_z-1, max_z+1):
      for y in range(min_y-1, max_y+1):
        for x in range(min_x-1, max_x+1):
          for w in range(min_w-1, max_w+1):
            cube_map[z][y][x][w].tick()

    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1
    min_w -= 1
    max_w += 1


  t = 0
  for z in range(min_z, max_z):
    for y in range(min_y, max_y):
      for x in range(min_x, max_x):
        for w in range(min_w, max_w):
          t += cube_map[z][y][x][w].alive

  return t

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
