#!/usr/bin/python3.11

try:
  int = int(input("Entrer an integer: "))

  if (int == 42) or (int <= 21) or (int % 3) or ((int / 2) < 21) or (int % 2) >= 45):
      print("OK")
  else:
      print("You got wrong my poor friend!")
except:
  print("Please, enter an integer")
