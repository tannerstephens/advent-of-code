#!/usr/bin/env python3

from __future__ import annotations

from itertools import combinations
from math import inf
from os.path import dirname, realpath
from re import findall
from typing import Sequence

dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input() -> list[list[str]]:
  return [findall(r'a (.)\S+ (.)', line) for line in puzzle_input]


class Component:
  component_type = 'undefined'

  def __init__(self, element: str) -> None:
    self.element = element

  def __str__(self) -> str:
    return f'{self.element}{self.component_type[0]}'

  def __repr__(self) -> str:
    return str(self)

  def __gt__(self, obj) -> bool:
    raise NotImplementedError


class Generator(Component):
  component_type = 'Generator'

  def __gt__(self, obj) -> bool:
    return True


class Microchip(Component):
  component_type = 'Microchip'

  def __gt__(self, obj) -> bool:
    if obj is self:
      return False

    if type(obj) == Generator:
      return self.element == obj.element

    return False


class Floor:
  def __init__(self, floor_num: int, components: list[Component] = None):
    self.components = components or []
    self.floor_num = floor_num

  def __iter__(self):
    return iter(self.components)

  def __len__(self):
    return len(self.components)

  def __str__(self) -> str:
    return f'|F{self.floor_num}| {" ".join(map(str, self.components))}'

  def add_component(self, component: Component):
    self.components.append(component)

  def remove_component(self, component: Component):
    self.components.remove(component)

  def copy(self) -> Floor:
    return Floor(self.floor_num, self.components[:])

  def is_valid(self) -> bool:
    if not any(isinstance(c, Generator) for c in self.components):
      return True

    return all(any(c > c2 for c2 in self.components) for c in self.components)


class Building:
  def __init__(self, floors: list[Floor], working_floor: int = None, ticks: int = None, moves = None) -> None:
    self.floors = floors
    self.working_floor = working_floor or 0
    self.ticks = ticks or 0
    self.moves = moves or []

  def __repr__(self) -> str:
    return '\n'.join(str(floor) + (' <' if floor.floor_num == self.working_floor else '') for floor in self.floors[::-1])

  def is_valid(self) -> bool:
    return all(floor.is_valid() for floor in self.floors)

  def is_solved(self) -> bool:
    if len(self.floors[-1]) == 0:
      return False

    return all(len(floor) == 0 for floor in self.floors[:-1])

  def get_working_floor(self) -> Floor:
    return self.floors[self.working_floor]

  def can_move_up(self) -> bool:
    return self.working_floor < len(self.floors) - 1

  def can_move_down(self) -> bool:
    return any(len(floor) > 0 for floor in self.floors[:self.working_floor])

  def move_up(self, components: Sequence[Component]) -> None:
    if len(components) == 0:
      raise ValueError('components must have len() > 0')

    for c in components:
      self.floors[self.working_floor].remove_component(c)
      self.floors[self.working_floor + 1].add_component(c)

    self.working_floor += 1
    self.ticks += 1
    self.moves.append(('up', components))

  def move_down(self, components: Sequence[Component]) -> None:
    if len(components) == 0:
      raise ValueError('components must have len() > 0')

    for c in components:
      self.floors[self.working_floor].remove_component(c)
      self.floors[self.working_floor - 1].add_component(c)

    self.working_floor -= 1
    self.ticks += 1
    self.moves.append(('down', components))

  def get_state(self) -> str:
    out = []

    for floor in self.floors:
      seen = set()

      g = 0
      m = 0
      p = 0

      for c in floor:
        if c.component_type == Generator.component_type:
          g += 1
        else:
          m += 1

        if c.element in seen:
          g -= 1
          m -= 1
          p += 1
        else:
          seen.add(c.element)

      out.append(f'P{p}G{g}M{m}')

      if floor.floor_num == self.working_floor:
        out[-1] += '!'

    return '|'.join(out)

  def copy(self) -> Building:
    floors_copy = list(map(lambda floor: floor.copy(), self.floors))

    return Building(floors_copy, self.working_floor, self.ticks, self.moves[:])


def solve(building: Building, current_minimum: float = inf, seen: dict[str, int] = None) -> float:
  if seen is None:
    seen = dict()

  if not building.is_valid():
    return inf

  if building.is_solved():
    return building.ticks

  if building.ticks > current_minimum:
    return inf

  state = building.get_state()

  if state in seen and seen[state] <= building.ticks:
    return inf

  seen[state] = building.ticks

  working_floor = building.get_working_floor()

  for n in (1,2):
    for components_to_move in combinations(working_floor, n):
      if building.can_move_up():
        bc = building.copy()
        bc.move_up(components_to_move)
        r = solve(bc, current_minimum, seen)
        current_minimum = min(current_minimum, r)

      if building.can_move_down():
        bc = building.copy()
        bc.move_down(components_to_move)
        r = solve(bc, current_minimum, seen)
        current_minimum = min(current_minimum, r)

  return current_minimum


def puzzle_input_to_floors(pi: list[list[str]]) -> list[Floor]:
  return [Floor(i, [Generator(component[0]) if component[1] == 'g' else Microchip(component[0]) for component in line]) for i, line in enumerate(pi)]


def part1():
  pi = parse_input()

  building = Building(puzzle_input_to_floors(pi))

  return solve(building)

def part2():
  pi = parse_input()

  pi[0] += [['e', 'g'], ['e', 'm'], ['d', 'g'], ['d', 'm']]

  building = Building(puzzle_input_to_floors(pi))

  return solve(building)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
