#!/usr/bin/env python3

from collections import deque
from hashlib import md5
from os.path import dirname, realpath
from re import findall, search
from typing import Generator

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]


class OTP:
  def __init__(self, salt: str, stretch=False) -> None:
    self.salt = salt
    self.index = 0

    self.stretch_enabled = stretch

    self.posibilities: deque[tuple[str, list[str]]] = deque()
    self.fives: deque[str] = deque() # ['a', 'd', 'f']


  def stretch(self, h: str) -> str:
    for _ in range(2016):
      h = md5(h.encode()).hexdigest()

    return h

  def get_hash(self) -> str:
    h = md5(f'{self.salt}{self.index}'.encode()).hexdigest()

    return self.stretch(h) if self.stretch_enabled else h

  def keys(self) -> Generator[tuple[str, int], None, None]:
    while True:
      h = self.get_hash()

      found_fives = findall(r'(.)\1{4}', h)

      self.fives += found_fives
      self.posibilities.append((h, found_fives))

      if len(self.posibilities) == 1001:
        h, found_fives = self.posibilities.popleft()

        for _ in found_fives:
          self.fives.popleft()

        found = search(r'(.)\1\1', h)

        if found and found.group(1) in self.fives:
          yield h, self.index - 1000

      self.index += 1


def part1():
  salt = parse_input()

  otp = OTP(salt)

  gen = otp.keys()

  i = None

  for _ in range(64):
    h, i = next(gen)

  return i

def part2():
  salt = parse_input()

  otp = OTP(salt, True)

  c = 0

  gen = otp.keys()

  i = None

  for _ in range(64):
    h, i = next(gen)

  return i

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
