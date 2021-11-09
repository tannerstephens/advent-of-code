#!/usr/bin/env python3

def ping(node = None):
    if node == None:
        node = "0"

    if not graph[node]["has"]:
        graph[node]["has"] = True
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
    graph[this] = {"conn" : nums, "has" : False}

ping()

count = 1

new = {}

for i in graph:
    if not graph[i]["has"]:
        new[i] = dict(graph[i])

while new:
    count += 1
    graph = dict(new)
    new = {}
    ping(list(graph.keys())[0])

    for i in graph:
        if not graph[i]["has"]:
            new[i] = dict(graph[i])
    

print(count)
