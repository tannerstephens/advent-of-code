#!/usr/bin/env python3.6

with open("input.txt") as f:
    jumps = [int(i) for i in f.read().split("\n")[:-1]]

index = 0
count = 0

while index < len(jumps):
    count += 1
    step = jumps[index]
    jumps[index] += 1
    index += step

print(count)
