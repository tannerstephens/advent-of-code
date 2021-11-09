#!/usr/bin/env python3

puzzle = 349
buf = [0]

pos = 0

for i in range(1,2018):
    pos = ((puzzle + pos) % len(buf))+1
    buf.insert(pos,i)

i = buf.index(2017) + 1

print(buf[i])

