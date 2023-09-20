#!/usr/bin/python3.11

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len = len(a)
val = 1

for i in range(1, len):
    val = i * val
print(val)
