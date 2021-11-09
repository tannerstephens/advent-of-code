#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

def parse_input():
  return [[puzzle_input[i], int(puzzle_input[i+1])] for i in range(0, len(puzzle_input), 2)]

class VM:
  def __init__(self, insts=[]):
    self.insts = insts

  def run(self):
    acc = 0
    header = 0
    l = len(self.insts)

    seen = set()

    while header != l:
      inst = self.insts[header]

      if header in seen:
        return False, acc

      seen.add(header)

      if inst[0] == 'acc':
        acc += inst[1]
      elif inst[0] == 'jmp':
        header += inst[1] - 1

      header += 1

    return True, acc

def part1():
  pi = parse_input()

  return VM(pi).run()[1]

def part2():
  pi = parse_input()

  replace = {'nop': 'jmp', 'jmp': 'nop'}

  vm = VM(pi)

  for i in range(len(pi)):
    inst = pi[i]

    if inst[0] in replace:
      vm.insts[i][0] = replace[inst[0]]

      status, res = vm.run()

      if(status):
        return res

      vm.insts[i][0] = replace[inst[0]]


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
