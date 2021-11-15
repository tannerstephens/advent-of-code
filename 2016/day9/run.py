#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]


def decompress(data):
  out = ''

  while len(data) > 0:
    try:
      next_paren = data.index('(')
    except:
      next_paren = -1

    if next_paren >= 0:
      out += data[:next_paren]
      work, data = data[next_paren+1:].split(')', 1)

      l, times = [int(v) for v in work.split('x')]

      out += ''.join([data[:l]]*times)
      data = data[l:]

    else:
      out += data
      data = ''

  return out


def calculate_full_decompress_length(data):
  l = 0

  while len(data) > 0:
    try:
      next_paren = data.index('(')
    except:
      next_paren = -1

    if next_paren >= 0:
      l += next_paren

      work, data = data[next_paren+1:].split(')', 1)
      ln, times = [int(v) for v in work.split('x')]

      l += calculate_full_decompress_length(data[:ln])*times
      data = data[ln:]
    else:
      l += len(data)
      data = ''

  return l


def part1():
  pi = parse_input()

  return len(decompress(pi))

def part2():
  pi = parse_input()

  return calculate_full_decompress_length(pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
