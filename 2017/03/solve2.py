#!/usr/bin/env python3

def get_bigger(num):
    grid = {str([0,0]):1,str([1,0]):1}

    x = 1
    y = 0
    dx = 0
    dy = 1
    layer = False

    while grid[str([x,y])] <= num:
        x += dx
        y += dy

        if abs(x) == abs(y):
            if x > 0 and y > 0:
                dx = -1
                dy = 0
            elif x < 0 and y > 0:
                dx = 0
                dy = -1
            elif x < 0 and y < 0:
                dx = 1
                dy = 0
            else:
                layer = True
        elif layer:
            dx = 0
            dy = 1
            layer = False

        nxt = 0

        check = [[x,y+1],[x+1,y+1],[x+1,y],[x+1,y-1],[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1]]
        for look in check:
            if str(look) in grid:
                nxt += grid[str(look)]

        grid[str([x,y])] = nxt

    return grid[str([x,y])]



puzzle = 368078

val = get_bigger(puzzle)

print(val)