#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def make_tree(nums, parent=None):
  if parent == None:
    parent = 1
  else:
    parent += 1

  header = nums[:2]

  nums[:] = nums[2:]

  if header[0] == 0:
    metadata = nums[:header[1]]
    tree = {parent : {"nodes" : [], "metadata" : metadata}}
    nums[:] = nums[header[1]:]
  else:
    tree = {parent : {"nodes" : []}}
    for _ in range(header[0]):
      tree[parent]["nodes"].append(make_tree(nums, parent))
    metadata = nums[:header[1]]
    nums[:] = nums[header[1]:]
    tree[parent]["metadata"] = metadata
  
  return tree

def sum_metadata(tree):
  k = list(tree.keys())[0]

  ms = sum(tree[k]["metadata"])

  for node in tree[k]["nodes"]:
    ms += sum_metadata(node)
  
  return ms

def complex_sum(tree):
  k = list(tree.keys())[0]

  if len(tree[k]["nodes"]) == 0:
    return sum(tree[k]["metadata"])

  s = 0

  for entry in tree[k]["metadata"]:
    if entry == 0:
      continue
    
    index = entry - 1
    if index >= len(tree[k]["nodes"]):
      continue

    s += complex_sum(tree[k]["nodes"][index])

  return s

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()[0].strip()

  nums = [int(i) for i in data.split()]

  tree = make_tree(nums)
  return sum_metadata(tree)

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()[0].strip()

  nums = [int(i) for i in data.split()]

  tree = make_tree(nums)

  return complex_sum(tree)

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
