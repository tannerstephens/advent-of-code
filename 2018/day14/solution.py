#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def part1():
  with open(directory + "/input") as f:
    data = int(f.readlines()[0])

  scoreboard = [3,7]

  elf1 = 0
  elf2 = 1

  while len(scoreboard) < data + 12:
    (tens, ones) = divmod(scoreboard[elf1] + scoreboard[elf2], 10)

    if tens:
      scoreboard += [tens,ones]
    else:
      scoreboard += [ones]

    elf1 = (elf1 + scoreboard[elf1] + 1) % len(scoreboard)
    elf2 = (elf2 + scoreboard[elf2] + 1) % len(scoreboard)

  out = ""

  for score in scoreboard[data:data+10]:
    out += str(score)

  return out

def part2():
  with open(directory + "/input") as f:
    data = [int(x) for x in f.readlines()[0][:-1]]

  scoreboard = [3,7]

  elf1 = 0
  elf2 = 1


  l = 2

  combos = set()

  while True:
    (tens, ones) = divmod(scoreboard[elf1] + scoreboard[elf2], 10)
    if tens:
      scoreboard.append(tens)
      l += 1

      a = scoreboard[-len(data):]
      if a == data:
        return l-len(data)
    
    scoreboard.append(ones)
    l += 1

    a = scoreboard[-len(data):]
    if a == data:
      return l-len(data)

    elf1 = (elf1 + scoreboard[elf1] + 1) % l
    elf2 = (elf2 + scoreboard[elf2] + 1) % l


def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
