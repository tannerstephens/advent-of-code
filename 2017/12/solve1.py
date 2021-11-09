#!/usr/bin/env python3

def ping(node = None):
    if node == None:
        node = "0"

    if not graph[node]["zero"]:
        graph[node]["zero"] = True
        for conn in graph[node]["conn"]:
            ping(conn)
        return
    else:
        return
        

with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

graph = {}

for line in data:
    nums = line.split(" <-> ")[1].split(", ")
    this = line.split(" ")[0]
    graph[this] = {"conn" : nums, "zero" : False}

ping()

count = 0

for i in graph:
    if graph[i]["zero"]:
        count += 1

print(count)
