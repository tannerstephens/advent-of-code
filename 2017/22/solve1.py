#!/usr/bin/env python3

from math import floor

with open("input.txt") as f:
    grid = [list(l.strip()) for l in f.readlines()]

padding = 1000
xsize = len(grid)

for i in range(xsize):
    grid[i] = ["." for i in range(padding)] + grid[i] + ["." for i in range(padding)]

grid = [["." for i in range(padding*2+xsize)] for j in range(padding)] + grid + [["." for i in range(padding*2+xsize)] for j in range(padding)]


d = 0
x = y = floor(len(grid)/2)
count = 0

for i in range(10000):
    if grid[y][x] == "#":
        #right
        grid[y][x] = "."
        d = (d+1)%4
    else:
        #left
        grid[y][x] = "#"
        d = (d-1)%4
        count += 1

    if d == 0:
        dx = 0
        dy = -1
    elif d == 1:
        dx = 1
        dy = 0
    elif d == 2:
        dx = 0
        dy = 1
    else:
        dx = -1
        dy = 0

    x += dx
    y += dy

print(count)

    
