#!/usr/bin/env python3

def rem(l,r):
    o = l[:]
    o.remove(r)
    return o

def strength(br):
    s = 0

    for seg in br:
        s += seg[1]

    return s

def make_bridge(seg,look,br=None):
    if br == None:
        br = []
    
    best = None
    best_s = 0
    for s in seg:
        if look in s[0]:
            l = s[0][(s[0].index(look)+1)%2]
            cur = make_bridge(rem(seg,s),l,br + [s])
            s = strength(cur)
            if s > best_s:
                best = cur[:]
                best_s = s

    if best == None:
        return br
    else:
        return best
    


with open("input.txt") as f:
    data = [i.strip() for i in f.readlines()]

segments = []

for line in data:
    w = line.split("/")
    segments.append([[int(w[0]), int(w[1])], int(w[0]) + int(w[1])])

bridge = make_bridge(segments,0)

print(strength(bridge))



        
