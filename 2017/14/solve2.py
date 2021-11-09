#!/usr/bin/env python3

def knot(data):
    lengths = []

    for c in data:
        lengths.append(ord(c))

    lengths += [17,31,73,47,23]

    nums = list(range(256))
    pos = 0
    skip = 0

    for j in range(64):
        for l in lengths:
            if l <= 255:
                work = []
                for i in range(pos,pos+l):
                    work.append(nums[i%256])
                work = work[::-1]
                for i in range(pos,pos+l):
                    nums[i%256] = work[i-pos]

                pos += (l + skip)%256
                skip += 1

    sparse = nums[:]
    dense = []

    for i in range(0,256,16):
        x = sparse[i]
        for j in range(1,16):
            x = x^sparse[i+j]

        dense.append(x)

    out = ""

    for i in dense:
        out += hex(i)[2:].zfill(2)


    return out

def h2b(h):
    b = bin(int(h,16))[2:].zfill(len(h)*4)
    return b

def count_regions():
    r = 0
    for x in range(128):
        for y in range(128):
            r += map_regions(x,y,r)

    return r
            

def map_regions(x,y,n):
    if disk[x][y]["value"] == "0":
        return 0
    if disk[x][y]["region"] != None:
        return 0

    disk[x][y]["region"] = n
    maps = []
    if x != 0:
        maps.append([-1,0])
    if x != 127:
        maps.append([1,0])
    if y != 0:
        maps.append([0,-1])
    if y != 127:
        maps.append([0,1])

    for m in maps:
        map_regions(x+m[0], y+m[1], n)

    return 1


puzzle = "wenycdww"

disk = []

for i in range(128):
    h = knot(puzzle + "-" + str(i))
    b = h2b(h)
    row = []

    for c in  b:
        row.append({"value" : c, "region" : None})
    disk.append(row)

print(count_regions())


