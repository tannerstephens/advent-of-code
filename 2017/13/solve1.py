#!/usr/bin/env python3

def caught(d, r):
    if r == 0:
        return False
    elif r == 1:
        return True
    else:
        return (d%(2*(r-1))) == 0

with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

sev = 0

for line in data:
    work = [int(i) for i in line.split(": ")]
    if caught(work[0], work[1]):
        sev += work[0] * work[1]

print(sev)
    
