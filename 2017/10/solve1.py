#!/usr/bin/env python3

import pprint

with open("input.txt") as f:
    lengths = [int(i) for i in f.readline()[:-1].split(",")]

nums = list(range(256))
pos = 0
skip = 0

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

print(nums[0]*nums[1])
    
        
