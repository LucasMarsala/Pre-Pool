#!/usr/bin/python3.11

i, s = int(input("Enter an integer: ")), input("Enter an string: ");
[quit() if i == 0 else print(i) if s in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] else print(i) if i >= 42 else print(s)]
