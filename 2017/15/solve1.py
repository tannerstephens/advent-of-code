#!/usr/bin/env python3

def gen(n,m):
    while True:
        n = (n*m)%2147483647
        yield n

with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

ap = int(data[0].split("with ")[1])
bp = int(data[1].split("with ")[1])

am = 16807
bm = 48271

A = gen(ap,am)
B = gen(bp,bm)

bitand = 65535

judge = 0

for i in range(40000000):
    if next(A) & bitand == next(B) & bitand:
        judge += 1
print(judge)
