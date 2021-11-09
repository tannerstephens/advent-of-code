#!/usr/bin/env python3

def get_pos(num):
    if num == 1:
        return 0,0
    if num == 2:
        return 1,0
    else:
        x = 1
        y = 0
        dx = 0
        dy = 1
        layer = False

        for i in range(2,puzzle):
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
        return x,y



puzzle = 368078

x,y = get_pos(puzzle)

print(abs(x) + abs(y))