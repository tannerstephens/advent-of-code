#!/usr/bin/env python3

def get_weight(p):
    if "above" not in m[p]:
        w = m[p]["weight"]
        m[p]["above"] = []
        for child in m[p]["children"]:
            m[p]["above"].append(get_weight(child))
    return sum(m[p]["above"]) + m[p]["weight"]

def check_weight(p):
    get_weight(p)

    n = False
    for i,w in enumerate(m[p]["above"]):
        if m[p]["above"].count(w) == 1:
            n = True
            break
    if n:
        next_branch = m[p]["children"][i]
    else:
        parent = m[p]["parent"]
        for w in m[parent]["above"]:
            if m[parent]["above"].count(w) > 1:
                for j in m[parent]["above"]:
                    if j != w:
                        bad = j
                dif = w-bad
                return m[p]["weight"] + dif
        

    return check_weight(next_branch) 

    
        
        

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

print(check_weight(name))
