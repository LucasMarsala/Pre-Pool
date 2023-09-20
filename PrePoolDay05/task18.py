#!/usr/bin/python3.11

[x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
# // permet de diviser x par deux mais de garder uniquement un int en valeur
# Donc si X est un nombre pair, on le divise par 2 et on garde le nombre
# sinon, on multiplie x par 2 et on fait ca pour chaque element de la liste.
