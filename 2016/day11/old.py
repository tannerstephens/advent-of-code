#!/usr/bin/env python3

from __future__ import annotations

from math import inf
from os.path import dirname, realpath
from re import findall

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

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
  component_type = 'Gernerator'

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


class ComponentContainer:
  def __init__(self, components: list[Component] = None):
    self.components = components or []

  def __iter__(self):
    return iter(self.components)

  def __len__(self):
    return len(self.components)

  def add_component(self, component: Component):
    self.components.append(component)

  def remove_component(self, component: Component):
    self.components.remove(component)

  def copy(self) -> ComponentContainer:
    raise NotImplementedError



class Floor(ComponentContainer):
  def __init__(self, floor_num: int, components: list[Component] = None):
    super().__init__(components=components)

    self.floor_num = floor_num

  def __str__(self) -> str:
    return f'|F{self.floor_num}| {" ".join(map(str, self.components))}'

  def copy(self) -> Floor:
    return Floor(self.floor_num, self.components[:])


class Elevator(ComponentContainer):
  def __init__(self, max_components: int = 2, components: list[Component] = None):
    super().__init__(components=components)

    self.max_components = max_components

  def __str__(self) -> str:
    return f'E[{" ".join(map(str, self.components))}]'

  def can_add_component(self) -> bool:
    return len(self.components) < self.max_components

  def has_components(self) -> bool:
    return len(self.components) > 0

  def add_component(self, component: Component):
    if len(self.components) < self.max_components:
      return super().add_component(component)
    else:
      raise Exception('Unable to add component, max reached')

  def copy(self) -> Elevator:
    return Elevator(self.max_components, self.components[:])


class Building:
  def __init__(self, floors: list[Floor], elevator: Elevator = None, elevator_floor: int = None, ticks: int = None, moves=None) -> None:
    self.floors = floors
    self.elevator = elevator or Elevator()
    self.elevator_floor = elevator_floor or 0
    self.ticks = ticks or 0
    self.moves = moves or []

  def __str__(self) -> str:
    elevator_str = str(self.elevator)

    return '\n'.join(
      [
        (f'{elevator_str} ' if self.elevator_floor == i else ' ' * (len(elevator_str) + 1)) + str(floor)
        for i, floor in enumerate(self.floors)
      ]
    )

  def __repr__(self) -> str:
    return str(self)

  def is_valid(self) -> bool:
    for floor in self.floors:
      if floor.floor_num == self.elevator_floor:
        iterator = floor.components + self.elevator.components
      else:
        iterator = floor.components

      generators = list(filter(lambda c: type(c) is Generator, iterator))
      microchips = filter(lambda c: type(c) is Microchip, iterator)

      if len(generators) == 0:
        continue

      for microchip in microchips:
        good = False
        for generator in generators:
          if microchip > generator:
            good = True

        if not good:
          return False

    return True

  def is_solved(self) -> bool:
    if self.elevator_floor == len(self.floors) - 1 and len(self.floors[-1]):
      for floor in self.floors:
        if floor.floor_num != len(self.floors) - 1:
          if len(floor):
            return False
      return True
    else:
      return False

  def elevator_can_move(self) -> bool:
    return len(self.elevator.components) > 0

  def elevator_can_move_up(self) -> bool:
    return self.elevator_can_move() and self.elevator_floor < len(self.floors) - 1

  def elevator_can_move_down(self) -> bool:
    if self.elevator_can_move():
      min_floor = 0
      for floor in self.floors:
        if len(floor) == 0 and min_floor == floor.floor_num:
          min_floor = floor.floor_num + 1

      return self.elevator_floor > min_floor
    return False

  def move_elevator_up(self) -> None:
    self.elevator_floor += 1
    self.ticks += 1

  def move_elevator_down(self) -> None:
    self.elevator_floor -= 1
    self.ticks += 1

  def get_elevator_floor(self) -> Floor:
    return self.floors[self.elevator_floor]

  def get_state(self):
    n = 0

    m = {}

    out = []

    for floor in self.floors:
      w = []
      for c in floor:
        if c.element in m:
          use = m[c.element]
        else:
          use = n
          m[c.element] = n
          n += 1

        if type(c) is Generator:
          w.append(f'G{use}')
        else:
          w.append(f'M{use}')

      if floor.floor_num == self.elevator_floor:
        for c in self.elevator:
          if c.element in m:
            use = m[c.element]
          else:
            use = n
            m[c.element] = n
            n += 1

          if type(c) is Generator:
            w.append(f'EG{use}')
          else:
            w.append(f'EM{use}')
      out.append(' '.join(sorted(w)))

    return '\n'.join(out)

  def copy(self) -> Building:
    floors_copy = list(map(lambda floor: floor.copy(), self.floors))

    elevator_copy = self.elevator.copy()

    return Building(floors_copy, elevator_copy, self.elevator_floor, self.ticks, self.moves[:])


def get_possible_moves(building: Building) -> list[str]:
  moves = []

  if building.elevator_can_move_up():
    moves.append('meu') # Move elevator up

  if building.elevator.can_add_component() and len(building.get_elevator_floor()) > 0:
    moves.append('lev') # Load elevator

  if building.elevator.has_components():
    moves.append('uev') # Unload elevator

  if building.elevator_can_move_down():
    moves.append('med') # Move elevator down

  return moves


def puzzle_input_to_floors(pi: list[list[str]]) -> list[Floor]:
  return [Floor(i, [Generator(component[0]) if component[1] == 'g' else Microchip(component[0]) for component in line]) for i, line in enumerate(pi)]


def solve(building: Building, current_minimum: float = 41, seen: dict[str, float] = None, rec=0) -> float:
  rec += 1

  if seen is None:
    seen = dict()

  if not building.is_valid():
    return inf

  if building.is_solved():
    return building.ticks

  if building.ticks >= current_minimum:
    return inf

  if building.get_state() in seen and seen[building.get_state()] <= building.ticks:
    return inf

  seen[building.get_state()] = building.ticks

  possible_moves = get_possible_moves(building)

  r = inf

  for move in possible_moves:
    if move == 'med':
      bc = building.copy()
      bc.moves.append('med')
      bc.move_elevator_down()
      r = solve(bc, current_minimum, seen, rec)

    elif move == 'meu':
      bc = building.copy()
      bc.moves.append('meu')
      bc.move_elevator_up()
      r = solve(bc, current_minimum, seen, rec)

    elif move == 'lev':
      for c in building.get_elevator_floor():
        bc = building.copy()
        bc.moves.append('lev ' + str(c))
        bc.elevator.add_component(c)
        bc.get_elevator_floor().remove_component(c)
        r = solve(bc, current_minimum, seen, rec)

        if r < current_minimum:
          current_minimum = r

    elif move == 'uev':
      for c in building.elevator:
        bc = building.copy()
        bc.moves.append('uev ' + str(c))
        bc.elevator.remove_component(c)
        bc.get_elevator_floor().add_component(c)
        r = solve(bc, current_minimum, seen, rec)

        if r < current_minimum:
          current_minimum = r

    if r < current_minimum:
      current_minimum = r
  return current_minimum

def part1():
  pi = parse_input()

  building = Building(puzzle_input_to_floors(pi))

  return solve(building)

def part2():
  pi = parse_input()

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
