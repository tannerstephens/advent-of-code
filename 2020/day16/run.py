#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n\n')

from re import findall

from pprint import pprint

def parse_input():
  rules = {}
  rules_input = puzzle_input[0].split('\n')

  for rule_line in rules_input:
    work = findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', rule_line)[0]
    rules[work[0]] = [[int(work[1]), int(work[2])], [int(work[3]), int(work[4])]]

  my_ticket = list(map(int, puzzle_input[1].split('\n')[1].split(',')))

  def nearby_ticket_generator():
    nearby_lines = puzzle_input[2].split('\n')[1:-1]

    for line in nearby_lines:
      yield list(map(int, line.split(',')))

  return {
    'rules': rules,
    'me': my_ticket,
    'nearby': nearby_ticket_generator()
  }

def matches_rule(n, rule):
  (low0, high0), (low1, high1) = rule

  return (low0 <= n <= high0) or (low1 <= n <= high1)

def get_invalid_values(ticket, rules):
  for n in ticket:
    good = False
    for rule in rules:
      if matches_rule(n, rules[rule]):
        good = True
        break
    if not good: yield n

def is_valid(ticket, rules):
  return len(list(get_invalid_values(ticket, rules))) == 0

def part1():
  pi = parse_input()

  s = 0

  for ticket in pi['nearby']:
    s += sum(get_invalid_values(ticket, pi['rules']))

  return s

def update_possible(field_possibilities, i, rem, solved):
  for j in range(len(field_possibilities)):
    if len(field_possibilities[j]) == 1:
      continue
    field_possibilities[j].discard(rem)
    if len(field_possibilities[j]) == 1:
      (solved[j], ) = field_possibilities[j]
      update_possible(field_possibilities, j, solved[j], solved)


def part2():
  pi = parse_input()
  nearby_tickets = list(filter(lambda ticket: is_valid(ticket, pi['rules']), pi['nearby']))

  field_possibilities = [set(pi['rules'].keys()) for _ in nearby_tickets[0]]

  solved = [None for _ in nearby_tickets[0]]

  for ticket in nearby_tickets:
    for i, n in enumerate(ticket):
      if solved[i] is not None:
        continue

      new = set()
      for rule in field_possibilities[i]:
        if matches_rule(n, pi['rules'][rule]): new.add(rule)

      if len(new) == 0:
        print(ticket, i, n)

      field_possibilities[i] = new

      if len(field_possibilities[i]) == 1:
        (solved[i], ) = field_possibilities[i]
        update_possible(field_possibilities, i, solved[i], solved)

  r = 1

  for i, key in enumerate(solved):
    if 'dep' == key[:3]:
      r *= pi['me'][i]

  return r

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
