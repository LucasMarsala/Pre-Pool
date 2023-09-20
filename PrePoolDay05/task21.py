#!/usr/bin/python3.11

first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
magic = [* zip ( first_name , last_name [:: -1]) ]

print(* zip ( first_name , last_name [:: -1]) )
print ( magic [0])
print ( magic [3])
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])

# Nous avons deux list. Zip permet de fusionner les deux list en tuple
# Ensuite, on donne les elements de chaque tableau.
# La list last_name est cependant inverse.
# Dans le premier cas on affiche l'element 0 de chaque list donc Jackie et Chan
# Dans le deuxime cas, on a Sylvester Stallon
# Et dans le dernier cas, on a Arnold Schwarzenegger.
# Pour le 3eme et 4eme cas, nous demandons des elements specific.
# On demande la premiere paire de nom  et prenom. donc Bruce Willis. Puis on demande l'element 0, donc uniquement son prenom
# Tandis que dans le 4eme cas on demande uniquement le nom de famille.
