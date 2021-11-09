#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

class Cart:
  def __init__(self,x,y,d):
    self.x = x
    self.y = y
    self.d = d
    self.turn = -1
    self.alive = True

  def move(self, map):
    if self.d == 0:
      self.y -= 1
    elif self.d == 1:
      self.x += 1
    elif self.d == 2:
      self.y += 1
    else:
      self.x -= 1

    
    m = map[self.y][self.x]

    if m in ["/", "\\"]:
      if m == "/":
        if self.d in [0,2]:
          self.d += 1
        else:
          self.d -= 1
      else:
        if self.d in [0,2]:
          self.d = (self.d-1) % 4
        else:
          self.d = (self.d+1) % 4

    elif m == "+":
      self.d = (self.d + self.turn) % 4

      self.turn += 1
      if self.turn == 2:
        self.turn = -1

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  track = []
  carts = []

  cart_dirs = ["^", ">", "v", "<"]

  for y, row in enumerate(data):
    working_row = []
    for x, c in enumerate(row):
      if c in cart_dirs:
        d = cart_dirs.index(c)

        if d == 0 or d == 2:
          m = "|"
        else:
          m = "-"
        carts.append(Cart(x,y,d))
        working_row.append(m)
      else:
        working_row.append(c)
    track.append(working_row)

  positions = set()
  while True:
    carts = sorted(carts, key=lambda k: (k.y, k.x))
    old_positions = positions
    positions = set()
    for cart in carts:
      old_pos = (cart.x, cart.y)

      cart.move(track)
      pos = (cart.x, cart.y)

      if pos in positions or pos in old_positions:
        return str(pos[0]) + "," + str(pos[1])
      else:
        positions.add(pos)
        if old_pos in old_positions:
          old_positions.remove(old_pos)

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()

  track = []
  carts = []

  cart_dirs = ["^", ">", "v", "<"]

  for y, row in enumerate(data):
    working_row = []
    for x, c in enumerate(row):
      if c in cart_dirs:
        d = cart_dirs.index(c)

        if d == 0 or d == 2:
          m = "|"
        else:
          m = "-"
        carts.append(Cart(x,y,d))
        working_row.append(m)
      else:
        working_row.append(c)
    track.append(working_row)

  while len(carts) > 1:

    carts = sorted(carts, key=lambda k: (k.y, k.x))

    for cart in carts:
      cart.move(track)

      for cart2 in carts:
        if cart == cart2:
          continue
        if cart2.alive:
          if cart2.x == cart.x and cart2.y == cart.y:
            cart.alive = False
            cart2.alive = False
    new_carts = []
    for cart in carts:
      if cart.alive:
        new_carts.append(cart)
    
    carts = new_carts
  
  c = carts[0]

  return str(c.x) + "," + str(c.y)

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
