#!/usr/bin/env python3

with open("input.txt") as f:
    jumps = [int(i) for i in f.read().split("\n")[:-1]]

index = 0
count = 0

while index < len(jumps):
    count += 1
    step = jumps[index]
    if step >= 3:
        jumps[index] -= 1
    else:
        jumps[index] += 1
    index += step

print(count)
