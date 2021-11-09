#!/usr/bin/env python3

def anagram_exists(passphrase):
    words = []
    for word in password:
        words.append("".join(sorted(word)))

    for word in words:
        if words.count(word) > 1:
            return True

    return False

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

        if good and not anagram_exists(password):
            valid += 1

print(valid)
