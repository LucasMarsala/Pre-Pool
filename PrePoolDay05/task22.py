#!/usr/bin/python3.11

import random
import time

startingTime = time.time()

a = [] * 1000000

for i in range(0, 1000000):
    a.insert(i, i)
print(a)

duration = time.time() - startingTime
print(duration)
