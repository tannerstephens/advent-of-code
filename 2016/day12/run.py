#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [line.split() for line in puzzle_input]


class CPU:
  def __init__(self, program: list[list[str]], a: int = 0, b: int = 0, c: int = 0, d: int = 0) -> None:
    self.registers: dict[str, int] = {
      'a': a,
      'b': b,
      'c': c,
      'd': d,
    }

    self.program = program
    self.pc: int = 0

  def cpy(self, x: str, y: str) -> None:
    if x.isdigit():
      self.registers[y] = int(x)
    else:
      self.registers[y] = self.registers[x]

  def inc(self, x: str) -> None:
    self.registers[x] += 1

  def dec(self, x: str) -> None:
    self.registers[x] -= 1

  def jnz(self, x: str, y: str) -> None:
    if x.isdigit():
      n = int(x)
    else:
      n = self.registers[x]

    if n != 0:
      self.pc += int(y) - 1

  def run(self) -> None:
    while self.pc < len(self.program):
      inst = self.program[self.pc]

      if inst[0] == 'cpy':
        self.cpy(inst[1], inst[2])
      elif inst[0] == 'inc':
        self.inc(inst[1])
      elif inst[0] == 'dec':
        self.dec(inst[1])
      elif inst[0] == 'jnz':
        self.jnz(inst[1], inst[2])

      self.pc += 1


def part1():
  pi = parse_input()

  cpu = CPU(pi)

  cpu.run()

  return cpu.registers['a']

def part2():
  pi = parse_input()

  cpu = CPU(pi, c=1)

  cpu.run()

  return cpu.registers['a']

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
