#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

INSTS = {'AND', 'LSHIFT', 'RSHIFT', 'OR', 'NOT'}

def parse_input():
  return [parse_instruction(line.split(' ')) for line in puzzle_input]

def parse_instruction(inst):
  if inst[0] in INSTS:
    return (inst[0], inst[1], inst[-1])

  if inst[1] in INSTS:
    return (inst[1], inst[0], inst[2], inst[-1])

  return ('VAL', inst[0], inst[-1])

def build_dep_tree(insts):
  dep_tree = {}

  for inst in insts:
    dep_tree[inst[-1]] = inst

  return dep_tree

def run_circuit(dep_tree, target, res={}, b=False):
  if target not in dep_tree:
    r = int(target)

  else:
    if target in res:
      return res[target]

    inst = dep_tree[target]

    action = inst[0]

    if action == 'AND':
      r = run_circuit(dep_tree, inst[1], res, b)&run_circuit(dep_tree, inst[2], res, b)

    if action == 'OR':
      r = run_circuit(dep_tree, inst[1], res, b)|run_circuit(dep_tree, inst[2], res, b)

    if action == 'NOT':
      r = ~run_circuit(dep_tree, inst[1], res, b)

    if action == 'LSHIFT':
      r = run_circuit(dep_tree, inst[1], res, b) << run_circuit(dep_tree, inst[2], res, b)

    if action == 'RSHIFT':
      r = run_circuit(dep_tree, inst[1], res, b) >> run_circuit(dep_tree, inst[2], res, b)

    if action == 'VAL':
      r = run_circuit(dep_tree, inst[1], res, b)

  res[target] = r
  return r

def part1():
  pi = parse_input()

  dep_tree = build_dep_tree(pi)

  return run_circuit(dep_tree, 'a')

def part2():
  pi = parse_input()

  dep_tree = build_dep_tree(pi)

  del dep_tree['b']
  dep_tree['b'] = ('VAL', '46065', 'b')

  r = run_circuit(dep_tree, 'a', res={})

  return r

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
