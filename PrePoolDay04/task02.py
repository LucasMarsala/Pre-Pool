#!/usr/bin/python3.11

try:
  int = int(input("Entrer an integer: "))

  if (int % 2):
      print("The integer is odd")
  else:
      print("The integer is even")
except:
  print("Please, enter an integer")
