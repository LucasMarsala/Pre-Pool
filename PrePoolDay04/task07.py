#!/usr/bin/python3.11

try:
  str = input("Entrer a string: ")

  for i in str:
      print(i, i, sep='', end='')
except:
  print("Exception thrown")
