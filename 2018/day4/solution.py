#!/usr/bin/python3

import os
from datetime import datetime

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  events = []

  for line in data:
    work = line.split(" ")
    time = datetime.strptime(" ".join(work[:2]), '[%Y-%m-%d %H:%M]')
    events.append(dict(time=time, event=" ".join(work[2:]).strip()))

  ordered_events = sorted(events, key=lambda k: k["time"])

  asleep_chart = {}

  current_guard = None

  for event in ordered_events:
    if event["event"][0] == "G":
      current_guard = int(event["event"].split("#")[1].split(" ")[0])
      asleep = False
    elif event["event"][0] == "w":
      asleep_stop = event["time"].minute

      if current_guard not in asleep_chart:
        asleep_chart[current_guard] = []
      
      asleep_chart[current_guard].append([False for _ in range(60)])
      for m in range(asleep_start, asleep_stop):
        asleep_chart[current_guard][-1][m] = True
      
    else:
      asleep_start = event["time"].minute

  sleepy_guards = {}

  for guard in asleep_chart:
    sleepy_guards[guard] = 0

    for day in asleep_chart[guard]:
      sleepy_guards[guard] += day.count(True)

  sleepiest_guard = max(sleepy_guards, key=lambda k: sleepy_guards[k])

  time_count = [0 for _ in range(60)]

  for day in asleep_chart[sleepiest_guard]:
    for i,a in enumerate(day):
      if a:
        time_count[i] += 1

  max_value_index = time_count.index(max(time_count))

  return max_value_index * sleepiest_guard

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()


  events = []

  for line in data:
    work = line.split(" ")
    time = datetime.strptime(" ".join(work[:2]), '[%Y-%m-%d %H:%M]')
    events.append(dict(time=time, event=" ".join(work[2:]).strip()))

  ordered_events = sorted(events, key=lambda k: k["time"])

  asleep_chart = {}

  current_guard = None

  for event in ordered_events:
    if event["event"][0] == "G":
      current_guard = int(event["event"].split("#")[1].split(" ")[0])
      asleep = False
    elif event["event"][0] == "w":
      asleep_stop = event["time"].minute

      if current_guard not in asleep_chart:
        asleep_chart[current_guard] = []
      
      asleep_chart[current_guard].append([False for _ in range(60)])
      for m in range(asleep_start, asleep_stop):
        asleep_chart[current_guard][-1][m] = True
      
    else:
      asleep_start = event["time"].minute

  sleep_count = {}

  for guard in asleep_chart:
    sleep_count[guard] = [0 for _ in range(60)]

    for day in asleep_chart[guard]:
      for i,m in enumerate(day):
        if m:
          sleep_count[guard][i] += 1

  highest_count = 0
  highest_minute = -1
  highest_guard = -1

  for guard in sleep_count:
    for i,m in enumerate(sleep_count[guard]):
      if m > highest_count:
        highest_count = m
        highest_minute = i
        highest_guard = guard


  return highest_guard * highest_minute

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
