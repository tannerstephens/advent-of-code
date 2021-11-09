#!/usr/bin/env python3

puzzle = 349
pos = 0
for i in range(1,50000001):
    pos = ((puzzle + pos) % i)+1
    if pos == 1:
        val = i

print(val)

