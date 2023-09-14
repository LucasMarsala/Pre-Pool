#!/usr/bin/python3.11

try:
  n = int(input("Entrer an integer: "))
  max_value = int(n / 2) + 1

  for a in range(2, max_value):
      for i in range(max_value, 0, -1):
          if ((i * a) < n):
              print(i * a, sep=' ', end=' ')
      print()

except:
  print("Please, enter an integer")
