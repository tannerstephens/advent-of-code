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
    if x.lstrip('-').isdigit():
      self.registers[y] = int(x)
    else:
      self.registers[y] = self.registers[x]

  def inc(self, x: str) -> None:
    self.registers[x] += 1

  def dec(self, x: str) -> None:
    self.registers[x] -= 1

  def jnz(self, x: str, y: str) -> None:

    if x.lstrip('-').isdigit():
      n = int(x)
    else:
      n = self.registers[x]

    if y.lstrip('-').isdigit():
      s = int(y)
    else:
      s = self.registers[y]

    if n != 0:
      self.pc += s - 1

  def tgl(self, x: str) -> None:
    if x.lstrip('-').isdigit():
      n = int(x)
    else:
      n = self.registers[x]

    target = self.pc + n

    if target < 0 or target >= len(self.program):
      return

    if len(self.program[target]) == 2:
      if self.program[target][0] == 'inc':
        self.program[target][0] = 'dec'
      else:
        self.program[target][0] = 'inc'

    elif len(self.program[target]) == 3:
      if self.program[target][0] == 'jnz':
        self.program[target][0] = 'cpy'
      else:
        self.program[target][0] = 'jnz'

  def opt(self):
    self.registers['a'] += self.registers['b'] * self.registers['d']
    self.registers['d'] = 0
    self.registers['c'] = 0

  def run(self) -> None:
    while self.pc < len(self.program):
      inst = self.program[self.pc]

      try:
        if inst[0] == 'cpy':
          self.cpy(inst[1], inst[2])
        elif inst[0] == 'inc':
          self.inc(inst[1])
        elif inst[0] == 'dec':
          self.dec(inst[1])
        elif inst[0] == 'jnz':
          self.jnz(inst[1], inst[2])
        elif inst[0] == 'tgl':
          self.tgl(inst[1])
        elif inst[0] == 'opt':
          self.opt()
      except (KeyError, ValueError):
        pass

      self.pc += 1


def optimize(lines: list[str]):
  repl = [
    'cpy b c',
    'inc a',
    'dec c',
    'jnz c -2',
    'dec d',
    'jnz d -5',
  ]

  for i in range(len(lines[:-len(repl)])):
    if lines[i:i+len(repl)] == repl:
      return lines[:i] + ['opt'] + ['nop']*5 + lines[i+len(repl):]

  return []


def part1():
  opt_puzzle_input = optimize(puzzle_input)
  pi = [line.split() for line in opt_puzzle_input]

  cpu = CPU(pi, a=7)

  cpu.run()

  return cpu.registers['a']

def part2():
  opt_puzzle_input = optimize(puzzle_input)
  pi = [line.split() for line in opt_puzzle_input]

  cpu = CPU(pi, a=12)

  cpu.run()

  return cpu.registers['a']

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
