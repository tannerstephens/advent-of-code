#!/usr/bin/env python3

def caught(d, r):
    if r == 0:
        return False
    elif r == 1:
        return True
    elif r == 2:
        return d%2 == 0
    else:
        return (d%(2*(r-1))) == 0

def pass_secretly(delay):
    for step in steps:
        if caught(step[0] + delay, step[1]):
            print(steps.index(step),": ", end="")
            return False
    return True

    

with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

steps = []

for line in data:
    steps.append([int(i) for i in line.split(": ")])
    
delay = 0

while not pass_secretly(delay):
    delay += 1
    print(delay)

print(delay)
    
