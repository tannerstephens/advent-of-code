#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

m = {}

for line in data:
    name = line.split(" ")[0]
    weight = int(line.split("(")[1].split(")")[0])
    if "->" in line:
        children = line.split(" -> ")[1].split(", ")
    else:
        children = []

    if name in m:
        m[name]["weight"] = weight
        m[name]["children"] = children
    else:
        m[name] = {"weight" : weight, "children" : children}

    for child in children:
        if child in m:
            m[child]["parent"] = name
        else:
            m[child] = {"parent" : name}


while "parent" in m[name]:
    name = m[name]["parent"]

print(name)
    
