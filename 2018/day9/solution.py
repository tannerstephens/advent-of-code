#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

class Node:
  def __init__(self, val=None, nxt=None, prev=None):
    self.val = val
    self.next = nxt
    self.prev = prev

def play_game(players, points):
  active = Node(0)
  active.next = active
  active.prev = active

  zero = active

  current_marble = 1
  current_player = 0

  scores = {}

  while current_marble <= points:
    if (current_marble % 23) == 0:
      if current_player not in scores:
        scores[current_player] = 0

      remove = active
      
      for _ in range(7):
        remove = remove.prev

      remove.prev.next = remove.next
      remove.next.prev = remove.prev

      active = remove.next

      scores[current_player] += remove.val + current_marble
    else:
      insert_after = active.next
      old_next = insert_after.next

      new_node = Node(current_marble, old_next, insert_after)
      insert_after.next = new_node
      old_next.prev = new_node

      active = new_node

    current_marble += 1
    current_player = (current_player + 1) % players

  return scores


def part1():
  with open(directory + "/input") as f:
    data = f.readlines()[0].strip()

  work = data.split()
  players, points = int(work[0]), int(work[-2])

  scores = play_game(players, points)
  
  return scores[max(scores, key=lambda k: scores[k])]

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()[0].strip()

  work = data.split()
  players, points = int(work[0]), int(work[-2])*100

  scores = play_game(players, points)
  return scores[max(scores, key=lambda k: scores[k])]

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
