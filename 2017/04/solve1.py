#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().split("\n")

passwords = []

for line in data:
    passwords.append(line.split(" "))


valid = 0

for password in passwords:
    if len(password) > 1:
        good = True
        for word in password:
            if password.count(word) > 1:
                good = False

        if good:
            valid += 1
    

print(valid)
