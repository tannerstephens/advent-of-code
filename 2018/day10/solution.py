#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

class Particle:
  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self. vy = vy
  
  def tick(self):
    self.x += self.vx
    self.y += self.vy

  def untick(self):
    self.x -= self.vx
    self.y -= self.vy

def parse_line(line):
  work = line.split("<")

  xy = work[1].split(", ")
  x = int(xy[0])
  y = int(xy[1].split(">")[0])

  xy = work[2].split(", ")
  vx = int(xy[0])
  vy = int(xy[1].split(">")[0])

  return x,y,vx,vy


def get_grid_size(particles):
  w = max(particles, key=lambda k: k.x).x
  h = max(particles, key=lambda k: k.y).y
  wm = min(particles, key=lambda k: k.x).x
  hm = min(particles, key=lambda k: k.y).y

  w = (w-wm)
  h = (h-hm)

  return (w,h)

def print_particles(particles):
  w = max(particles, key=lambda k: k.x).x
  h = max(particles, key=lambda k: k.y).y
  wm = min(particles, key=lambda k: k.x).x
  hm = min(particles, key=lambda k: k.y).y
  grid = [[" " for _ in range(h-hm+1)] for _ in range(w-wm+1)]

  for p in particles:
    grid[p.x-wm][p.y-hm] = "█"

  out = ""

  for r in grid:
    out += "".join(r) + "\n"

  return out

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  particles = []

  for line in data:
    x,y,vx,vy = parse_line(line)

    particles.append(Particle(y,x,vy,vx))

  (w,h) = get_grid_size(particles)

  size = w*h

  

  while True:
    for p in particles:
      p.tick()

    (w,h) = get_grid_size(particles)

    new_size = w*h

    if new_size > size:
      for p in particles:
        p.untick()
      return "\n" + print_particles(particles).strip()
    else:
      size = new_size

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()

  particles = []

  for line in data:
    x,y,vx,vy = parse_line(line)

    particles.append(Particle(y,x,vy,vx))

  (w,h) = get_grid_size(particles)

  size = w*h

  count = 0

  while True:
    count += 1
    for p in particles:
      p.tick()

    (w,h) = get_grid_size(particles)

    new_size = w*h

    if new_size > size:
      return count - 1
    else:
      size = new_size

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
