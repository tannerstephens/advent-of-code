#!/usr/bin/env python3

with open("input.txt") as f:
    data = [i.strip() for i in f.readlines()][3:]

sm = {}

for i in range(0,len(data),10):
    state = data[i].split("state ")[1][0]
    sm[state] = []

    for j in range(i,i+8,4):
        a = [int(data[j+2].split("lue ")[1][:-1])]
        if 'left' in data[j+3]:
            a.append(-1)
        else:
            a.append(1)
        a.append(data[j+4][-2])
        sm[state].append(a)
        
        

state = "A"
steps = 12302209
tape = [0 for i in range(1000)]
tc = 0

for i in range(steps):
    insts = sm[state][tape[tc]]
    tape[tc] = insts[0]
    tc += insts[1]

    if tc < 0:
        tc = 0
        tape = [0] + tape
    elif tc >= len(tape):
        tape = tape + [0]

    state = insts[2]

print(tape.count(1))
    
