#!/usr/bin/env python3

def access(val):
    try:
        int(val)
        isd = True
    except:
        isd = False

    if isd:
        return int(val)
    else:
        if val in mem:
            return mem[val]
        else:
            mem[val] = 0
            return 0

with open("input.txt") as f:
    commands = [i.split() for i in f.readlines()]

mem = {}

last = 0

pc = 0

while pc < len(commands):
    cmd = commands[pc]
    if cmd[1] not in mem:
        mem[cmd[1]] = 0
    if cmd[0] == "snd":
        last = access(cmd[1])
    elif cmd[0] == "set":
        mem[cmd[1]] = access(cmd[2])
    elif cmd[0] == "add":
        mem[cmd[1]] += access(cmd[2])
    elif cmd[0] == "mul":
        mem[cmd[1]] *= access(cmd[2])
    elif cmd[0] == "mod":
        mem[cmd[1]] %= access(cmd[2])
    elif cmd[0] == "rcv":
        if access(cmd[1]) != 0:
            print(last)
    if cmd[0] == "jgz":
        if access(cmd[1]) > 0:
            pc += access(cmd[2])
        else:
            pc += 1
    else:
        pc += 1
    
