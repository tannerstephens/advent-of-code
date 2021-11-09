#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

class Cell:
  def __init__(self):
    self.power_level = 0

mem = {}

def get_val(grid, xs, ys, size=3):
  if (xs,ys,size) in mem:
    return mem[(xs,ys,size)]
  elif size == 1:
    return grid[xs][ys].power_level
  else:
    s = get_val(grid,xs,ys,size-1)
    
    l = xs + size - 1

    for y in range(size):
      s += grid[l][ys+y].power_level

    l = ys + size - 1

    for x in range(size-1):
      s += grid[xs+x][l].power_level
    
    mem[(xs,ys,size)] = s
    return s

  return s

def new_get_val(sum_grid, x, y, size=3):
  if x == 0 and y == 0:
    return sum_grid[x+size-1][y+size-1]
  elif x == 0:
    return sum_grid[x+size-1][y+size-1] - sum_grid[x+size-1][y-1]
  elif y == 0:
    return sum_grid[x+size-1][y+size-1] - sum_grid[x-1][y+size-1]
  else:
    return sum_grid[x+size-1][y+size-1] + sum_grid[x-1][y-1] - sum_grid[x-1][y+size-1] - sum_grid[x+size-1][y-1]

def make_sum_grid(grid):
  size = len(grid)

  sum_grid = [[0 for _ in range(size)] for _ in range(size)]

  for x in range(size):
    for y in range(size):
      if x == 0 and y == 0:
        sum_grid[x][y] = grid[x][y].power_level
      elif x == 0:
        sum_grid[x][y] = sum_grid[x][y-1] + grid[x][y].power_level
      elif y == 0:
        sum_grid[x][y] = sum_grid[x-1][y] + grid[x][y].power_level
      else:
        sum_grid[x][y] = sum_grid[x-1][y] + sum_grid[x][y-1] - sum_grid[x-1][y-1] + grid[x][y].power_level

  return sum_grid



def part1():
  with open(directory + "/input") as f:
    data = int(f.readlines()[0])

  grid = [[Cell() for _ in range(300)] for _ in range(300)]

  for x,row in enumerate(grid):
    for y,cell in enumerate(row):
      r_id = x + 11

      cell.power_level = r_id * (y+1)
      cell.power_level += data

      cell.power_level *= r_id
      work = str(cell.power_level)[::-1]

      if len(work) < 3:
        cell.power_level = -5
      else:
        cell.power_level = int(work[2]) - 5

  most_power = 0
  bx = by = None

  sum_grid = make_sum_grid(grid)

  for x in range(300-3):
    for y in range(300-3):
      val = new_get_val(sum_grid,x,y)


      if val > most_power:
        most_power = val
        bx = x+1
        by = y+1



  return str(bx) + "," + str(by)

def part2():
  with open(directory + "/input") as f:
    data = int(f.readlines()[0])

  grid = [[Cell() for _ in range(300)] for _ in range(300)]

  for x,row in enumerate(grid):
    for y,cell in enumerate(row):
      r_id = x + 11

      cell.power_level = r_id * (y+1)
      cell.power_level += data

      cell.power_level *= r_id
      work = str(cell.power_level)[::-1]

      if len(work) < 3:
        cell.power_level = -5
      else:
        cell.power_level = int(work[2]) - 5

  most_power = 0
  bx = by = bs = None

  sum_grid = make_sum_grid(grid)

  for size in range(1,300):
    for x in range(300-size):
      for y in range(300-size):
        val = new_get_val(sum_grid,x,y,size)

        if val > most_power:
          most_power = val
          bx = x+1
          by = y+1
          bs = size


  return str(bx) + "," + str(by) + "," + str(bs)

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
