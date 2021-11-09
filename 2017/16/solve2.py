#!/usr/bin/env python3

def spin(l,x):
    work = l[-x:]
    return work + l[:-x]

def exchange(l,a,b):
    work = l[:]
    temp = work[a]
    work[a] = work[b]
    work[b] = temp
    
    return work

def partner(l,a,b):
    ia = l.index(a)
    ib = l.index(b)

    work = l[:]

    temp = work[ia]
    work[ia] = work[ib]
    work[ib] = temp

    return work

with open("input.txt") as f:
    insts = f.readline()[:-1].split(",")

programs = [chr(i) for i in range(97,113)]

seen = []

for i in range(1000000000):
    if "".join(programs) in seen:
        break
    seen.append("".join(programs))
    for inst in insts:
        op = inst[0]
        args = inst[1:].split("/")

        if op == "s":
            programs = spin(programs, int(args[0]))
        elif op == "x":
            programs = exchange(programs, int(args[0]), int(args[1]))
        elif op == "p":
            programs = partner(programs, args[0], args[1])
         
print(seen[1000000000%i])
