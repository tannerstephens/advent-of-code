def is_prime(n):
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(n**.5)+1,2):
            if n%i == 0:
                return False
        return True
            


h = 0
for b in range(106700, 123700 + 1,17):
    if not is_prime(b):
        h += 1

print(h)
