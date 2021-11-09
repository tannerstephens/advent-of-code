#/usr/bin/env python3

def get_sum(s,offset):
    total = 0
    l = len(s)
    for i in range(l):
        if s[i] == s[(i+offset)%l]:
            total += int(s[i])

    return total
    
with open("input.txt") as f:
    data = f.readline().split()[0]



print("1a:",get_sum(data,1))
print("1b:",get_sum(data,len(data)//2))

