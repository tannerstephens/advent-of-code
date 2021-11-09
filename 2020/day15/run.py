#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

def take_turn(last, history, turn):
  work = history[last]

  if work[0] == 1:
    z = history[0]
    z[0] += 1
    z[2] = z[1]
    z[1] = turn
    return 0
  else:
    n = work[1] - work[2]
    if n not in history:
      history[n] = [0, None, None]
    w = history[n]
    w[0] += 1
    w[2] = w[1]
    w[1] = turn
    return n

def play_game(seed, last_turn):
  history = {}

  turn_num = 0
  last = 0

  for n in seed:
    history[n] = [1, turn_num, None]
    turn_num += 1
    last = n

  while turn_num != last_turn:
    last = take_turn(last, history, turn_num)
    turn_num += 1

  return last

def parse_input():
  return map(int, puzzle_input[0].split(','))

def part1():
  nums = parse_input()

  return(play_game(nums, 2020))

def part2():
  nums = parse_input()

  return(play_game(nums, 30000000))

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
