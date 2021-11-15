#!/usr/bin/env python3

from os.path import dirname, realpath
from re import match
from collections import defaultdict
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  bots = []
  values = []

  for line in puzzle_input:
    if line[0] == 'b':
      bots.append(match(r'(bot \d+).+((?:bot|output) \d+).+((?:bot|output) \d+)', line).groups())
    else:
      values.append(match(r'value (\d+).+(bot \d+)', line).groups())

  return bots, values


class Output:
  def __init__(self):
    self.processed_values = []
    self.values = []

  def put_value(self, value):
    self.processed_values.append(value)
    self.values.append(value)

  def __repr__(self):
    return f'Output({self.values})'


class Bot(Output):
  def __init__(self, low=None, high=None):
    super().__init__()

    self.low: Output = low
    self.high: Output = high

  def set_low(self, low):
    self.low = low

  def set_high(self, high):
    self.high = high

  def put_value(self, value):
    super().put_value(value)

    if len(self.values) == 2:
      self.low.put_value(min(self.values))
      self.high.put_value(max(self.values))

      self.values = []

  def __repr__(self):
    return f'Bot({self.processed_values})'

def build_bot_tree(bots):
  bot_tree = defaultdict(Bot)

  for bot_line in bots:
    if 'output' in bot_line[1]:
      bot_tree[bot_line[1]] = Output()

    if 'output' in bot_line[2]:
      bot_tree[bot_line[2]] = Output()

    low = bot_tree[bot_line[1]]
    high = bot_tree[bot_line[2]]

    bot_tree[bot_line[0]].set_low(low)
    bot_tree[bot_line[0]].set_high(high)

  return bot_tree

def run(bots, values):
  bot_tree = build_bot_tree(bots)

  for v, bot in values:
    v = int(v)

    bot_tree[bot].put_value(v)

  return bot_tree


def part1():
  bots, values = parse_input()

  bot_tree = run(bots, values)

  return filter(lambda bot_key: 61 in bot_tree[bot_key].processed_values and 17 in bot_tree[bot_key].processed_values, bot_tree).__next__().split(' ')[1]

def part2():
  bots, values = parse_input()

  bot_tree = run(bots, values)

  return int(bot_tree['output 0'].values[0]) * int(bot_tree['output 1'].values[0]) * int(bot_tree['output 2'].values[0])

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
