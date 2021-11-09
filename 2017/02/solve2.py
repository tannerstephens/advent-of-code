#!/usr/bin/env python3

def find_div(line):
    for i,x in enumerate(line):
        for j,y in enumerate(line):
            if i != j and (x%y == 0):
                big = max([x,y])
                sma = min([x,y])
                return big,sma

spreadsheet = []

with open("./input.txt") as f:
    data = f.read().split("\n")[:-1]

for line in data:
    spreadsheet.append([int(num) for num in line.split("\t")])

checksum = 0

for line in spreadsheet:
    big,sma = find_div(line)
    checksum += big//sma

print(checksum)
