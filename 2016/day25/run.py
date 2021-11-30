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

    self.clk = None

  def getval(self, x: str) -> int:
    if x.lstrip('-').isdigit():
      n = int(x)
    else:
      n = self.registers[x]

    return n

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

  def out(self, x: str):
    if x.lstrip('-').isdigit():
      n = int(x)
    else:
      n = self.registers[x]

    self.clk = n


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
        elif inst[0] == 'out':
          self.out(inst[1])
          self.pc += 1
          return

      except (KeyError, ValueError):
        pass

      self.pc += 1



def part1():
  pi = parse_input()

  for i in range(1,2016):
    cpu = CPU(pi, a=i)
    cpu.run()
    look = 0

    c = 0

    while cpu.clk == look:
      c += 1

      if c == 100:
        return i

      if look == 0:
        look = 1
      else:
        look = 0

      cpu.run()

def part2():
  return 'Freebie'

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
