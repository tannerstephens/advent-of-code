#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  for line in puzzle_input:
    if line[:3] == 'mas':
      yield [
        'mask',
        line[7:]
      ]
    else:
      work = line[4:].split('] = ')
      yield [
        'mem',
        int(work[0]),
        int(work[1])
      ]

def mask(n, mask):
  n_bits = list(bin(n)[2:].zfill(len(mask)))

  for i, m in enumerate(mask):
    if m != 'X':
      n_bits[i] = m

  return int(''.join(n_bits), 2)

def mask2(n, mask):
  n_bits = list(bin(n)[2:].zfill(len(mask)))

  return _mask2(n_bits, mask, 0, '')

def _mask2(n_bits, mask, i, c):
  for j, m in enumerate(mask[i:]):
    if m == '0':
      c += n_bits[i+j]
    elif m == '1':
      c += '1'
    else:
      return _mask2(n_bits, mask, i+j+1, c+'0') + _mask2(n_bits, mask, i+j+1, c+'1')

  return [c]

def part1():
  pi = parse_input()

  m = None

  mem = {}

  for inst in pi:
    if inst[0] == 'mask':
      m = inst[1]
    else:
      mem[inst[1]] = mask(inst[2], m)

  return sum(mem.keys())

def part2():
  pi = parse_input()

  m = None

  mem = {}

  for inst in pi:
    if inst[0] == 'mask':
      m = inst[1]
    else:
      addrs = mask2(inst[1], m)

      for addr in addrs:
        mem[addr] = inst[2]

  return sum(mem.values())

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
