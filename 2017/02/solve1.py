#!/usr/bin/env python3

spreadsheet = []

with open("./input.txt") as f:
    data = f.read().split("\n")[:-1]

for line in data:
    spreadsheet.append([int(num) for num in line.split("\t")])

checksum = 0

for line in spreadsheet:
    small = min(line)
    big = max(line)
    checksum += (big - small)

print(checksum)
