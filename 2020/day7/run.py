#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

from re import findall

def parse_input():
  out = []

  for line in puzzle_input:
    work = line[:-1].split(' contain ')
    out.append([work[0], work[1].split(',')])

  return out

def get_bag_type(bag_string):
  bag_string = bag_string.strip()
  return findall(r'(\d?) ?(.+) bag', bag_string)[0]

class Bag:
  def __init__(self, bag_type):
    self.type = bag_type
    self.children = []
    self.parents = []

  def __repr__(self):
    return self.type

def create_bag_map(pi):
  bag_map = {}

  for bag in pi:
    bag_type = get_bag_type(bag[0])[1]

    if bag_type not in bag_map:
      bag_map[bag_type] = Bag(bag_type)

    for child in bag[1]:
      num, child_type = get_bag_type(child)

      if child_type == 'no other':
        num = 0

      if child_type not in bag_map:
        bag_map[child_type] = Bag(child_type)

      bag_map[bag_type].children.append((int(num), bag_map[child_type]))
      bag_map[child_type].parents.append(bag_map[bag_type])

  return bag_map


def count_super_parents(bag, seen=set()):
  seen.add(bag.type)

  count = 0

  for parent in bag.parents:
    if parent.type not in seen:
      count += count_super_parents(parent, seen) + 1

  return count


def count_internal_bags(bag, lookup={}):
  if bag.type in lookup:
    return lookup[bag.type]

  total = 0

  for num, child in bag.children:
    total += num*(count_internal_bags(child, lookup) + 1)

  lookup[bag.type] = total

  return total

def part1():
  pi = parse_input()

  bag_map = create_bag_map(pi)

  shiny_gold = bag_map['shiny gold']

  return count_super_parents(shiny_gold)

def part2():
  pi = parse_input()

  bag_map = create_bag_map(pi)

  shiny_gold = bag_map['shiny gold']

  return count_internal_bags(shiny_gold)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
