#!/usr/bin/env python3

def collide(particles):
    dead = []
    for i,particle1 in enumerate(particles):
        for j,particle2 in enumerate(particles):
            if i == j:
                continue
            else:
                if (particle1[0] == particle2[0]) and particle1 not in dead:
                    dead.append(particle1)

    for p in dead:
        particles.remove(p)

    return len(dead)
            

with open("input.txt") as f:
    data = [i.split(", ") for i in f.readlines()]

particles = []

for j,i in enumerate(data):
    p = [int(j) for j in i[0].split("<")[1].replace(">","").split(",")]
    v = [int(j) for j in i[1].split("<")[1].replace(">","").split(",")]
    a = [int(j) for j in i[2].split("<")[1].replace(">","").split(",")]

    particle = [p,v,a,j]

    particles.append(particle)

count = 0

collide(particles)

while count < 1000:
    dists = []

    for particle in particles:
        for i in range(3):
            particle[1][i] += particle[2][i]
            particle[0][i] += particle[1][i]


    if collide(particles) == 0:
        count += 1
    else:
        count = 0


print(len(particles))

    
