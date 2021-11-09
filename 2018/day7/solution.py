#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  prereqs = {}

  for line in data:
    req = line[5]
    stp = line[-13]

    if req not in prereqs:
      prereqs[req] = []

    if stp not in prereqs:
      prereqs[stp] = [req]
    else:
      prereqs[stp].append(req)
  
  available = []
  not_done = []

  for node in prereqs:
    not_done.append(node)
    if len(prereqs[node]) == 0:
      available.append(node)

  order = []

  while not_done:
    available = sorted(available, reverse=True)
    current = available.pop()
    not_done.remove(current)
    order.append(current)

    for node in prereqs:
      if node in order or node in available:
        continue
      else:
        if current in prereqs[node]:
          prereqs[node].remove(current)

          if len(prereqs[node]) == 0:
            available.append(node)

  return "".join(order)

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()

  prereqs = {}

  for line in data:
    req = line[5]
    stp = line[-13]

    if req not in prereqs:
      prereqs[req] = []

    if stp not in prereqs:
      prereqs[stp] = [req]
    else:
      prereqs[stp].append(req)
  
  available = []
  not_done = []

  for node in prereqs:
    not_done.append(node)
    if len(prereqs[node]) == 0:
      available.append(node)


  workers = [None for _ in range(5)]
  elapsed_time = 0
  order = []

  while not_done:
    available = sorted(available, reverse=True)

    while None in workers and available:
      w = workers.index(None)
      step = available.pop()
      time = ord(step) - 4
      workers[w] = [step, time]
      order.append(step)

    just_done = []

    for w,worker in enumerate(workers):
      if worker == None:
        continue
      elif worker[1] == 1:
        done = worker[0]
        workers[w] = None
        not_done.remove(done)
        just_done.append(done)
      else:
        worker[1] -= 1

    for node in prereqs:
      for nname in just_done:
        if node in order or node in available:
          continue
        else:
          if nname in prereqs[node]:
            prereqs[node].remove(nname)

            if len(prereqs[node]) == 0:
              available.append(node)

    elapsed_time += 1

  return elapsed_time

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
