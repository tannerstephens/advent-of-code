#!/usr/bin/env python3

def get(val, mem):
    try:
        int(val)
        d = True
    except ValueError:
        d = False

    if d:
        return int(val)
    else:
        return mem.get(val,0)

with open("input.txt") as f:
    commands = [i.split() for i in f.readlines()]

p0 = True
pc_0 = 0
mem_0 = {"p" : 0}
snd_0 = []

p1 = True
pc_1 = 0
mem_1 = {"p" : 1}
snd_1 = []

snd_1_count = 0

running = True

while running:
    # --- Program 0 --- #
    if p0:
        cmd = commands[pc_0]

        if cmd[1] not in mem_0:
            mem_0[cmd[1]] = 0

        p0_waiting = False

        if cmd[0] == "rcv":
            if len(snd_1):
                mem_0[cmd[1]] = snd_1.pop(0)
                pc_0 += 1
            else:
                p0_waiting = True
        else:
            if cmd[0] == "snd":
                snd_0.append(get(cmd[1], mem_0))
            elif cmd[0] == "set":
                mem_0[cmd[1]] = get(cmd[2], mem_0)
            elif cmd[0] == "add":
                mem_0[cmd[1]] += get(cmd[2], mem_0)
            elif cmd[0] == "mul":
                mem_0[cmd[1]] *= get(cmd[2], mem_0)
            elif cmd[0] == "mod":
                mem_0[cmd[1]] %= get(cmd[2], mem_0)
            if cmd[0] == "jgz":
                if get(cmd[1], mem_0) > 0:
                    pc_0 += get(cmd[2], mem_0)
                else:
                    pc_0 += 1
            else:
                pc_0 += 1
        

    # --- Program 0 --- #

    # --- Program 1 --- #
    if p1:
        cmd = commands[pc_1]

        if cmd[1] not in mem_1:
            mem_1[cmd[1]] = 0

        p1_waiting = False

        if cmd[0] == "rcv":
            if len(snd_0):
                mem_1[cmd[1]] = snd_0.pop(0)
                pc_1 += 1
            else:
                p1_waiting = True
        else:
            if cmd[0] == "snd":
                snd_1.append(get(cmd[1], mem_1))
                snd_1_count += 1
            elif cmd[0] == "set":
                mem_1[cmd[1]] = get(cmd[2], mem_1)
            elif cmd[0] == "add":
                mem_1[cmd[1]] += get(cmd[2], mem_1)
            elif cmd[0] == "mul":
                mem_1[cmd[1]] *= get(cmd[2], mem_1)
            elif cmd[0] == "mod":
                mem_1[cmd[1]] %= get(cmd[2], mem_1)
            if cmd[0] == "jgz":
                if get(cmd[1], mem_1) > 0:
                    pc_1 += get(cmd[2], mem_1)
                else:
                    pc_1 += 1
            else:
                pc_1 += 1

    # --- Program 1 --- #

    if (p0_waiting or not p0) and (p1_waiting or not p1):
        running = False
        print("DEADLOCK")

    if pc_0 > len(commands)-1 or pc_0 < 0:
        p0 = False
    if pc_1 > len(commands)-1 or pc_1 < 0:
        p1 = False

    if (not p0) and (not p1):
        running = False
        
        
print(snd_1_count)
