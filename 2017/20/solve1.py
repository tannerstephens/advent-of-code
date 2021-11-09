#!/usr/bin/env python3

def distance(particle):
    out = 0
    for d in particle[0]:
        out += abs(d)

    return out

with open("input.txt") as f:
    data = [i.split(", ") for i in f.readlines()]

particles = []

for i in data:
    p = [int(j) for j in i[0].split("<")[1].replace(">","").split(",")]
    v = [int(j) for j in i[1].split("<")[1].replace(">","").split(",")]
    a = [int(j) for j in i[2].split("<")[1].replace(">","").split(",")]

    particle = [p,v,a]

    particles.append(particle)

count = 0
closest = None

while count < 1000:
    dists = []

    for particle in particles:
        dists.append(distance(particle))
        for i in range(3):
            particle[1][i] += particle[2][i]
            particle[0][i] += particle[1][i]

    current = dists.index(min(dists))

    if current == closest:
        count += 1
    else:
        count = 0
        closest = current

print(current)

    
