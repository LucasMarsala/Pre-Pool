#!/usr/bin/python3.11

try:
  str = input("Entrer a string: ")

  if (str == "open sesame"):
      print("access granted")
  elif (str == "will you open, you goddamn !¤*@¡"):
      print("access fucking granted")
  else:
      print("permission denied")
except:
  print("Exception thrown")
