#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def convert_to_absolute(number: float) -> float:
    # prendre un nombre et retourner sa valeur absolue
    number_list = list(str(number))
    if "-" not in number_list:
        return number
    else:
        # enlever le premier index qui a le "-"
        number_list.pop(0)
        # joindre la liste pour donner un str
        new_num_str = "".join(number_list)
        # mettre le nombre sous la forme d'un float 
        abs_num = float(new_num_str)

        return abs_num


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    # besoin de créer une nouvelle liste pour recevoir ces noms
    name_list = []

    # transformer les prefixes en listes 
    prefixes_list = list(prefixes)

    for i in range(0, len(prefixes_list)):
        name = prefixes_list[i] + suffixe
        name_list.append(name)

    return name_list



import math 
def prime_integer_summation() -> int:
    # somme des 100 premiers nombres premiers excluant 1 
    prime_list = [2, 3, 5]
    number = 6

    # besoin de savoir s'il y a un nombre qui divise par 1 et la racine carré du nombre 
    while len(prime_list) < 100:
        is_prime = True
        for i in range(0, len(prime_list)):
            if number % prime_list[i] == 0:
                is_prime = False
                number += 1 
                break

        if is_prime == True:
            prime_list.append(number)
            number += 1 


    # somme
    somme = 0
    for i in range(0, len(prime_list)):
        somme = somme + prime_list[i]

    return somme 




def factorial(number: int) -> int:
    num = 1 

    multiplication = 1
    while num <= number:
        multiplication = multiplication * num
        num += 1

    return multiplication


def use_continue() -> None:
    for i in range(1, 11):
        if i != 5:
            print(i)
        else:
            continue


def verify_ages(groups: List[List[int]]) -> List[bool]:
    new_list = []
    for i in range(0, len(groups)):
        for j in range(0, len(groups[i])):
            if 3 < len(groups[i]) <= 10:
                if groups[i][j] >= 18:
                    if groups[i][j] <= 70: 
                        if groups[i][j] != 50:
                            new_list.append(True)
                            break
                        else: 
                            if 25 in groups[i]:
                                new_list.append(True)
                                break
                            else:
                                new_list.append(False)
                                break
                    else: 
                        if 25 in groups[i]:
                            new_list.append(True)
                            break
                        else:
                            new_list.append(False)
                            break
                else:
                    if 25 in groups[i]:
                        new_list.append(True)
                        break
                    else:
                        new_list.append((False))
                        break
            else:
                new_list.append((False))
                break

                            
    return new_list




def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
