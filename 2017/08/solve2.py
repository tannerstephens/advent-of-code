#!/usr/bin/env python3

#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

instructions = []

for line in data:
    instructions.append(line.split(" "))

memory = {}

all_max = 0

for i in instructions:
    if i[0] not in memory:
        memory[i[0]] = 0
    if i[4] not in memory:
        memory[i[4]] = 0 

    do_op = False

    if i[5] == ">":
        if memory[i[4]] > int(i[6]):
            do_op = True
    elif i[5] == ">=":
        if memory[i[4]] >= int(i[6]):
            do_op = True
    elif i[5] == "<":
        if memory[i[4]] < int(i[6]):
            do_op = True
    elif i[5] == "<=":
        if memory[i[4]] <= int(i[6]):
            do_op = True
    elif i[5] == "==":
        if memory[i[4]] == int(i[6]):
            do_op = True
    elif i[5] == "!=":
        if memory[i[4]] != int(i[6]):
            do_op = True

    if do_op:
        if i[1] == "inc":
            memory[i[0]] += int(i[2])
        else:
            memory[i[0]] -= int(i[2])

        if memory[i[0]] > all_max:
            all_max = memory[i[0]]

print(all_max)

