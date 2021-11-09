#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.readline()[:-1]

steps = data.split(",")

x = y = z = 0

far = 0

for step in steps:
    if step == "n":
        x += 1
        z -= 1
    elif step == "ne":
        x += 1
        y -= 1
    elif step == "se":
        y -= 1
        z += 1
    elif step == "s":
        x -= 1
        z += 1
    elif step == "sw":
        x -= 1
        y += 1
    elif step == "nw":
        y += 1
        z -= 1

    current = max([abs(x),abs(y),abs(z)])

    if current > far:
        far = current

print(max([abs(x),abs(y),abs(z)]))
print(far)




    
    
