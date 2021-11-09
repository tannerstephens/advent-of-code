#!/usr/bin/env python3

def find_big(l):
    m = 0
    ind = 0

    for i,v in enumerate(l):
        if v > m:
            m = v
            ind = i

    return ind

def redis(l,i):
    v = l[i]
    work = l[:]
    work[i] = 0

    while v > 0:
        i += 1
        work[i%len(l)] += 1
        v -= 1

    return work

with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\t")]

been = []
count = 0

while data not in been:
    been.append(data)
    count += 1
    i = find_big(data)
    data = redis(data,i)[:]

print(count)
print(len(been) - been.index(data))
