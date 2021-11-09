#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

from re import findall, match

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n\n')



INPUT_VALIDATION = {
  'byr': lambda year: 1920 <= int(year) <= 2002,
  'iyr': lambda year: 2010 <= int(year) <= 2020,
  'eyr': lambda year: 2020 <= int(year) <= 2030,
  'hgt': lambda height: (150 <= int(height[:-2]) <= 193) if height[-2:] == 'cm' else (59 <= int(height[:-2]) <= 76),
  'hcl': lambda color: match(r'^#[0-9a-f]{6}$', color),
  'ecl': lambda color: color in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
  'pid': lambda num: match(r'^\d{9}$', num)
}

REQUIRED_FIELDS = {
  'byr',
  'iyr',
  'eyr',
  'hgt',
  'hcl',
  'ecl',
  'pid'
}

def parse_input():
  out = []

  for line in puzzle_input:
    fields = findall(r'(\S{3}):(\S+)', line)

    out.append({field[0]:field[1] for field in fields})

  return out

def has_all_fields(passport):
  return REQUIRED_FIELDS.issubset(set(passport.keys()))

def is_valid_passport(passport):
  for field in INPUT_VALIDATION:
    try:
      if not INPUT_VALIDATION[field](passport[field]):
        return False
    except KeyError:
      return False

  return True



def part1():
  passports = parse_input()

  return len([1 for passport in passports if has_all_fields(passport)])

def part2():
  passports = parse_input()

  return len([1 for passport in passports if is_valid_passport(passport)])


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
