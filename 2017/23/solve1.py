#!/usr/bin/env python3

def get(reg,r):
    try:
        int(r)
        num = True
    except:
        num = False

    if num:
        return int(r)
    else:
        return reg[r]

def main():
    with open("input.txt") as f:
        instructions = [i[:-1].split(" ") for i in f.readlines()]


    reg = {}

    for d in range(97,105):
        reg[chr(d)] = 0

    running = True
    pc = 0
    count = 0

    while running:
        inst = instructions[pc]
        
        if inst[0] == "set":
            reg[inst[1]] = get(reg,inst[2])
        elif inst[0] == "sub":
            reg[inst[1]] -= get(reg,inst[2])
        elif inst[0] == "mul":
            reg[inst[1]] *= get(reg,inst[2])
            count += 1
        if inst[0] == "jnz":
            if get(reg, inst[1]) != 0:
                pc += get(reg, inst[2])
            else:
                pc += 1
        else:
            pc += 1

        if pc < 0 or pc >= len(instructions):
            running = False

    print(count)
            
main()
    
