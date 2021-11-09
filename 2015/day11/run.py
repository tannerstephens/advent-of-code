#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from string import ascii_lowercase

def make_three_strings():
  three = set()
  for i in range(len(ascii_lowercase)-2):
    three.add(ascii_lowercase[i:i+3])

  return three

three = make_three_strings()
bad = {'i', 'o', 'l'}

a = 97
z = 122

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]

def increment_string(s):
  nums = [ord(c) for c in s[::-1]]

  i = 0

  done = False

  while not done:
    nums[i] += 1

    if nums[i] > z:
      nums[i] = a
      i += 1
    else:
      done = True

  out = ''

  for o in nums[::-1]:
    out += chr(o)

  return out

def password_valid(s):
  req1 = False
  req2 = 0
  req2_skip = None
  for i in range(len(s)-1):
    if s[i] in bad:
      return False

    if not req1 and i <= 5:
      req1 = (s[i:i+3] in three)

    if (i != req2_skip) and (s[i] == s[i+1]):
      req2 += 1
      req2_skip = i+1

  return (req2 >= 2) and req1

def part1():
  s = parse_input()

  while not password_valid(s):
    s = increment_string(s)

  return s

def part2():
  s = increment_string('hepxxzzz')

  while not password_valid(s):
    s = increment_string(s)

  return s

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
