#!/usr/bin/env python3

import pprint

def tol(l):
    return "".join(l)
        

def flip(l):
    size = int(len(l)**.5)
    if size == 2:
        horiz = [l[1],l[0],
                 l[3],l[2]]
        vert = [l[2],l[3],
                l[0],l[1]]
    else:
        horiz = [l[2],l[1],l[0],
                 l[5],l[4],l[3],
                 l[8],l[7],l[6]]
        vert = [l[6],l[7],l[8],
                l[3],l[4],l[5],
                l[0],l[1],l[2]]

    return (horiz, vert)

def rotate(l):
    size = int(len(l)**.5)
    if size == 2:
        out = [l[2],l[0],
               l[3],l[1]]
    else:
        out = [l[6],l[3],l[0],
               l[7],l[4],l[1],
               l[8],l[5],l[2]]

    return out

def partition(lst):
    fsize = int(len(lst)**.5)

    if fsize in [2,3]:
        return [lst]

    else:
        if fsize%2 == 0:
            step = 2
        else:
            step = 3

        parts = [[None for j in range(step*step)] for i in range((fsize//step)**2)]

        isize = int(len(parts[0])**.5)
        osize = int(len(parts)**.5)
        size = osize * isize

        pi = 0

        look = [i for i in range(fsize-isize,fsize*fsize,size*step)]

        for i,p in enumerate(parts):
            k = -1
            z = 0
            for j,q in enumerate(p):
                if j%isize == 0:
                    k += 1
                    z = 0
                assert parts[i][j] == None
                parts[i][j] = lst[pi+z+k*size]
                z += 1
            if pi in look:
                if isize == 2:
                    pi += (isize + size)
                else:
                    pi += (isize + 2*size)
            else:
                pi += isize
            
    return parts

def join(parts):
    inside = int(len(parts[0])**.5)
    outside = int(len(parts)**.5)
    size = outside * inside

    l = [None for i in range(size*size)]

    pi = 0
    idex = {}
    nxt = 0

    for i in range(len(parts)):
        idex[i] = 0

    for i in range(size*size):
        if i%inside == 0 and i != 0:
            pi += 1
        
        if pi%outside == 0 and pi != nxt:
            if i%(size*inside) == 0:
                nxt = pi
            else:
                pi -= outside
        assert l[i] == None
        l[i] = parts[pi][idex[pi]]
        idex[pi] += 1

    return l

def main():   
    with open("input.txt") as f:
        data = [i.strip() for i in f.readlines()]

    rules = {}
    seen = []
    for line in data:
        work = line.split(" => ")
        start = list("".join(work[0].split("/")))        
        end = list("".join(work[1].split("/")))
        tmp = list(flip(list(start))) + [start]


        for f in tmp:
            rules[tol(f)] = end
            tmp2 = f[:]
            for i in range(3):
                tmp2 = rotate(tmp2)[:]
                rules[tol(tmp2)] = end
    assert rules[".#.#"] == list("#.#..##.#")

    pattern = [".","#",".",".",".","#","#","#","#"]

    for i in range(18):
        nxt = []        
        for p in partition(pattern):
            #print(p)
            work = rules[tol(p)]
            nxt.append(work)


        pattern = join(nxt)[:]

        print(i+1, pattern.count("#"))

    return rules

r = main()

