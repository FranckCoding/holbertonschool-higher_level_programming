#!/usr/bin/python3
for element in range(25, -1, -1):
    if element % 2 != 0:
        dif = 32
    print(chr(element + 65 + dif), end="")
