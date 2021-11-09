#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from re import findall
from itertools import product
from functools import reduce

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  ingredients = []
  for line in puzzle_input:
    ingredients.append([int(v) for v in findall(r'(-?\d+)', line)])

  return ingredients

def tablespoons(num_ingredients, total):
  for elem in product(range(total+1), repeat=num_ingredients):
    if sum(elem) == total:
      yield elem

def calculate_score(ingredients, amounts, calories=None):
  scores = [0, 0, 0, 0]

  c = 0

  for ingredient, amount in zip(ingredients, amounts):
    c += ingredient[-1]*amount
    for col, score in enumerate(scores):
      scores[col] = score+(ingredient[col]*amount)

  return reduce(lambda t, v: t*v if v > 0 else 0, scores) if (calories is None) or (c == calories) else 0

def part1():
  pi = parse_input()

  return max(map(lambda a: calculate_score(pi, a), tablespoons(len(pi), 100)))

def part2():
  pi = parse_input()

  return max(map(lambda a: calculate_score(pi, a, 500), tablespoons(len(pi), 100)))

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
