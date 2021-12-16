#!/usr/bin/env python3

from __future__ import annotations

from os.path import dirname, realpath
from math import prod

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  decode = {c: bin(i)[2:].zfill(4) for i, c in enumerate('0123456789ABCDEF')}

  return ''.join(decode[c] for c in puzzle_input[0])


class Packet:
  def __init__(self, bits: str):
    self.version = int(bits[:3], 2)
    self.type_id = int(bits[3:6], 2)

    self.value = None
    self.sub_packets: list[Packet] = []
    self.remaining_bits = ''

    self._parse_remaining_bits(bits[6:])

  def _parse_remaining_bits(self, remaining_bits: str):
    if self.type_id == 4:
      self._parse_literal_value(remaining_bits)
    else:
      self._parse_operator(remaining_bits)

  def _parse_literal_value(self, remaining_bits: str):
    v_b = ''

    for i in range(0, len(remaining_bits), 5):
      v_b += remaining_bits[i+1:i+5]

      if remaining_bits[i] == '0':
        self.value = int(v_b, 2)
        self.remaining_bits = remaining_bits[i+5:]
        return

  def _parse_operator(self, remaining_bits: str):
    if remaining_bits[0] == '0':
      self._operator_type_zero(remaining_bits[1:])
    else:
      self._operator_type_one(remaining_bits[1:])

  def _operator_type_zero(self, bits: str):
    sub_packets_length = int(bits[:15], 2)

    packet_data = bits[15:15+sub_packets_length]
    self.remaining_bits = bits[15+sub_packets_length:]

    while packet_data:
      self.sub_packets.append(Packet(packet_data))
      packet_data = self.sub_packets[-1]._get_remaining_bits()

  def _operator_type_one(self, bits: str):
    num_sub_packets = int(bits[:11], 2)

    packet_data = bits[11:]

    for _ in range(num_sub_packets):
      self.sub_packets.append(Packet(packet_data))
      packet_data = self.sub_packets[-1]._get_remaining_bits()

    self.remaining_bits = packet_data

  def _get_remaining_bits(self):
    return self.remaining_bits

  def sum_version(self) -> int:
    return self.version + sum(packet.sum_version() for packet in self.sub_packets)

  def evaluate(self) -> int:
    if self.type_id == 0:
      return sum(packet.evaluate() for packet in self.sub_packets)
    elif self.type_id == 1:
      return prod(packet.evaluate() for packet in self.sub_packets)
    elif self.type_id == 2:
      return min(packet.evaluate() for packet in self.sub_packets)
    elif self.type_id == 3:
      return max(packet.evaluate() for packet in self.sub_packets)
    elif self.type_id == 4:
      return self.value
    elif self.type_id == 5:
      return 1 if self.sub_packets[0].evaluate() > self.sub_packets[1].evaluate() else 0
    elif self.type_id == 6:
      return 1 if self.sub_packets[0].evaluate() < self.sub_packets[1].evaluate() else 0
    elif self.type_id == 7:
      return 1 if self.sub_packets[0].evaluate() == self.sub_packets[1].evaluate() else 0

def part1():
  pi = parse_input()

  packet = Packet(pi)

  return packet.sum_version()

def part2():
  pi = parse_input()

  packet = Packet(pi)

  return packet.evaluate()

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
