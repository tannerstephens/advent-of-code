#!/usr/bin/env python3

import argparse
from glob import glob
from importlib.util import spec_from_file_location, module_from_spec
from os import path
from re import match
from shutil import copytree
from time import time

DIR = path.dirname(path.abspath(__file__))

def load_all_days():
  days = {}

  for day_path in glob(f'{DIR}/day*/run.py'):
    day = int(match('.+day(\d\d?)', day_path)[1])
    spec = spec_from_file_location(f'day{day}', day_path)
    day_module = module_from_spec(spec)
    spec.loader.exec_module(day_module)

    days[day] = day_module

  return days

def create_from_template(day_num):
  copytree(f'{DIR}/template', f'{DIR}/day{day_num}')

def exec_time(f):
  start = time()
  res = f()
  t = time() - start

  ms = round(t * 1000, 2)

  return (ms, res)

def run_day(days, day_num):
  part1_time, part1_res = exec_time(days[day_num].part1)
  part2_time, part2_res = exec_time(days[day_num].part2)

  print(f'Day {day_num}')
  print(f'  Part 1: {part1_res} - {part1_time} ms')
  print(f'  Part 2: {part2_res} - {part2_time} ms\n')

def run_all_days(days):
  day_keys = list(days.keys())
  day_keys = sorted(day_keys, key=int)

  for day in day_keys:
    run_day(days, day)

def parse_arguments():
  parser = argparse.ArgumentParser()

  parser.add_argument('-d', '--day', help='Run a specific day', type=int)
  parser.add_argument('-r', '--run', help='Alias for --day', type=int, dest='day')
  parser.add_argument('-c', '--create', help='Create a new day folder from the template', type=int)
  parser.add_argument('-a', '--all', help='Run all days', action='store_true')

  return parser.parse_args()

def main():
  days = load_all_days()
  args = parse_arguments()

  if args.create:
    if args.create in days:
      print(f'ERROR! Day "{args.create}" already created!')
      return

    create_from_template(args.create)

  elif args.day:
    run_day(days, args.day)

  elif args.all:
    run_all_days(days)

  else:
    latest_day = max(days.keys(), key=int)
    run_day(days, latest_day)


if __name__ == '__main__':
  main()
