#!/usr/bin/python3.11

i, s = int(input("Enter an integer: ")), input("Enter an string: ");
[quit() if i == 0 else print(i) if [c for c in s if c in "aeiouAEIOU"] else print(i) if i >= 42 else print(s)]
