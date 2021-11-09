#!/usr/bin/env python3

from os.path import dirname, realpath
from typing import List

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [line.split() for line in puzzle_input]

class CPU:
  def __init__(self, program: List[List[str]], a=0, b=0):
    self.registers = {
      'a': a,
      'b': b
    }

    self.program = program
    self.pc = 0

    self.ops = {
      'hlf': self.hlf,
      'tpl': self.tpl,
      'inc': self.inc,
      'jmp': self.jmp,
      'jie': self.jie,
      'jio': self.jio,
    }

  def tick(self):
    instr = self.program[self.pc]

    op = instr[0]

    self.ops[op](instr)

    self.pc += 1

    return self.pc >= 0 and self.pc < len(self.program)

  def run(self):
    while self.tick():
      pass

  def hlf(self, instr: List[str]):
    self.registers[instr[1]] //= 2

  def tpl(self, instr: List[str]):
    self.registers[instr[1]] *= 3

  def inc(self, instr):
    self.registers[instr[1]] += 1

  def jmp(self, instr):
    self.pc += int(instr[1]) - 1

  def jie(self, instr):
    if self.registers[instr[1][0]] % 2 == 0:
      self.pc += int(instr[2]) - 1

  def jio(self, instr):
    if self.registers[instr[1][0]] == 1:
      self.pc += int(instr[2]) - 1



def part1():
  program = parse_input()

  cpu = CPU(program)

  cpu.run()

  return cpu.registers['b']

def part2():
  program = parse_input()

  cpu = CPU(program, a=1)

  cpu.run()

  return cpu.registers['b']

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
