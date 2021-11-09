#!/usr/bin/env python3

from __future__ import annotations
from os.path import dirname, realpath
from math import inf


dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]


class Player:
  def __init__(self, hp=50, mana=500):
    self.hp = hp
    self.mana = mana
    self.temp_armor = 0

  def copy(self) -> Player:
    return Player(self.hp, self.mana)

  def attack(self, damage):
    self.hp -= (damage - self.temp_armor)
    self.temp_armor = 0

  def add_temp_armor(self, temp_armor):
    self.temp_armor += temp_armor

class Boss:
  def __init__(self, hp, strength):
    self.hp = hp
    self.strength = strength

  def copy(self) -> Boss:
    return Boss(self.hp, self.strength)


class Effect:
  def __init__(self, name: str, turns: int, armor=0, damage=0, mana=0):
    self.name = name
    self.turns = turns
    self.armor = armor
    self.damage = damage
    self.mana = mana

  def __eq__(self, o: object) -> bool:
    return isinstance(o, Effect) and o.name == self.name

  def copy(self):
    return Effect(self.name, self.turns, self.armor, self.damage, self.mana)

  def apply(self, player: Player, boss: Boss) -> bool:
    '''Applies effects and returns False when depleted'''

    player.add_temp_armor(self.armor)
    boss.hp -= self.damage
    player.mana += self.mana
    self.turns -= 1

    return self.turns != 0

  def __repr__(self):
    return f'{self.name} - {self.turns} turns left'


class Spell:
  def __init__(self, name: str, mana_cost: int, damage=0, healing=0, effect: Effect = None):
    self.name = name
    self.mana_cost = mana_cost
    self.damage = damage
    self.healing = healing
    self.effect = effect

  def available(self, player_mana: int, active_effects: list[Effect]):
    if self.mana_cost > player_mana:
      return False

    if self.effect is not None and self.effect in active_effects:
      return False

    return True

  def cast(self, player: Player, boss: Boss, active_effects: list[Effect]) -> int:
    player.mana -= self.mana_cost

    boss.hp -= self.damage
    player.hp += self.healing

    if self.effect is not None:
      active_effects.append(self.effect.copy())

    return self.mana_cost

  def __repr__(self):
    return f'{self.name} - {self.mana_cost} Mana'


class Game:
  def __init__(self, player: Player, boss: Boss, spells: list[Spell] = None, active_effects: list[Effect] = None, mana_spent=0, hard=False):
    self.player = player
    self.boss = boss
    self.mana_spent = mana_spent
    self.hard = hard

    self.spells = spells
    if self.spells is None:
      self._register_default_spells()

    self.active_effects = active_effects or []

  def _register_default_spells(self):
    self.spells = (
      Spell('Magic Missile', 53, damage=4),
      Spell('Drain', 73, damage=2, healing=2),
      Spell('Shield', 113, effect=Effect('Shield', 6, armor=7)),
      Spell('Poison', 173, effect=Effect('Poison', 6, damage=3)),
      Spell('Recharge', 229, effect=Effect('Recharge', 5, mana=101))
    )

  def take_turn(self, spell: Spell) -> bool:
    # Player Turn

    self.mana_spent += spell.cast(self.player, self.boss, self.active_effects)

    if self.boss.hp <= 0:
      return True, self.player.hp <= 0

    # Boss Turn

    self._apply_effects()

    if self.boss.hp <= 0:
      return True, self.player.hp <= 0

    self.player.attack(self.boss.strength)

    # Player Turn

    if self.hard:
      self.player.hp -= 1

    if self.player.hp > 0:
      self._apply_effects()

    return self.boss.hp <= 0, self.player.hp <= 0


  def _apply_effects(self):
    non_depleted_effects = []

    for effect in self.active_effects:
      if effect.apply(self.player, self.boss):
        non_depleted_effects.append(effect)

    self.active_effects = non_depleted_effects

  def get_available_spells(self):
    return filter(lambda spell: spell.available(self.player.mana, self.active_effects), self.spells)

  def copy(self) -> Game:
    player_copy = self.player.copy()
    boss_copy = self.boss.copy()
    active_effects_copy = [e.copy() for e in self.active_effects]

    return Game(player_copy, boss_copy, self.spells, active_effects_copy, self.mana_spent, self.hard)


def find_minimum_mana_win(game: Game, layer=0) -> int:
  local_minimum = inf

  for spell in game.get_available_spells():
    game_copy = game.copy()

    boss_dead, player_dead = game_copy.take_turn(spell)

    if player_dead:
      continue

    if boss_dead:
      if game_copy.mana_spent < local_minimum:
        local_minimum = game_copy.mana_spent
    else:
      r_min = find_minimum_mana_win(game_copy, layer+1)

      if r_min < local_minimum:
        local_minimum = r_min

  return local_minimum


def parse_input():
  boss = {}

  for line in puzzle_input:
    key, value_s = line.split(': ')
    boss[key] = int(value_s)

  return Boss(boss['Hit Points'], boss['Damage'])

def part1():
  boss = parse_input()
  player = Player()

  game = Game(player, boss)

  return find_minimum_mana_win(game)

def part2():
  boss = parse_input()
  player = Player(hp=49)

  game = Game(player, boss, hard=True)

  return find_minimum_mana_win(game)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
