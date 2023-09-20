#!/usr/bin/python3.11

my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list.extend(my_second_list)
print(my_first_list)
# Ce code va ajouter a fin de la premiere list, les valeurs de la seconde list.
# Nous aurons [4 , 5 , 6, 1, 2, 3] dans my_first_list et [1 , 2 , 3] dans my_second_list

my_first_list = [7 , 8 , 9]
my_second_list = [4 , 5 , 6]
my_first_list = [*my_first_list , *my_second_list ]
# Ce code va assigner les valeurs des lists my_first_list et my_second_list dans my_first_list
# * est comme un deferencement en C
