#!/usr/bin/env python3

with open("input.txt") as f:
    lines = [i[:-1] for i in f.readlines()]

def new_dir(m,x,y,d):
    if d in [0,2]:
        dirs = [1,3]
    else:
        dirs = [0,2]

    for d in dirs:
        if d == 0:
            change = [0,-1]
        elif d == 1:
            change = [1,0]
        elif d == 2:
            change = [0,1]
        else:
            change = [-1,0]

        if m[y+change[1]][x+change[0]] != " ":
            return d

    return None

x = lines[0].index("|")
y = 0

d = 2

change = [0,1]

letters = ""

steps = 1

while True:
    if d == 0:
        change = [0,-1]
    elif d == 1:
        change = [1,0]
    elif d == 2:
        change = [0,1]
    else:
        change = [-1,0]

    x += change[0]
    y += change[1]

    if lines[y][x] == " ":
        x -= change[0]
        y -= change[1]
    
        d = new_dir(lines,x,y,d)

        if d == None:
            break

    else:
        steps += 1
        if lines[y][x] not in ["|","-","+"]:
            letters += lines[y][x]

print(letters,steps)
