#!/usr/bin/env python3

import shutil, glob

nxt = 0

for file in glob.glob("./[0-9][0-9]"):
    num = int(file.split("\\")[1])
    if num > nxt:
        nxt = num

nxt += 1

name = str(nxt).zfill(2)

shutil.copytree("./day","./"+name)
