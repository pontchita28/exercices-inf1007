#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
    # TODO: Calculer la puissance dissipée par la résistance.
    puissance = (voltage ** 2) / resistance
    return puissance

def orthogonal(v1, v2):
    # TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
    # v1[0] et v2[0] pour accéder au X
    # v1[1] et v2[1] pour accéder au Y
    total = 0
    for i in range(0, len(v1)):
        for j in range(0, len(v2)):
            produit = v1[i] + v2[j]
            total += produit
    if total == 0:
        return True
    else:
        return False


def point_in_circle(point, circle_center, circle_radius):
    # TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
    # point[0] et circle_center[0] pour accéder au X
    # point[1] et circle_center[1] pour accéder au Y
    # pour ce faire, on va voir si la distance entre le centre du cercle
    # est plus petite que la distance entre le point et le centre du cercle
    # d=√((x2 – x1)² + (y2 – y1)²).

    d = math.sqrt(((point[0] - circle_center[0])**2) + (point[1]- circle_center[1])**2)
    
    if d <= circle_radius:
        return True
    else:
        return False 


def cash(value):
    # TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ 
    # à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près. 
    # Il faut remplir les variables twenties, tens, fives, twos, ones, quarters, dimes 
    # et nickels avec le quantité de chaque dénomination.
    # transforme the value into a list 
    value_list = list(str(value))

    new_list = []
    # append all the numbers that are after the index of 
    # the .
    # look for the index of the "."
    index_dot = value_list.index(".")

    # slice commence au point indiqué
    new_list = value_list[index_dot+1: ]

    # joindre la mouvelle liste pour savoir quel est 
    # la valeur de la décimale
    dec_str = "".join(new_list)

    # transformer dec_str en int
    dec = int(dec_str)

    # while dec % 5 == 0: on va faire + 1
    while dec % 5 != 0:
        dec+=1

        
    # ajouter la mouvelle décimale à la liste
    # enlever toutes les valeurs qui se trouvent 
    # après la décimale
    value_list2 = value_list[:index_dot]
    # mettre la valeur sous forme de int
    entier_str = "".join(value_list2)

    # nouveau chiffre aussi mis en float 
    total = float(entier_str + "." + str(dec))

    twenties = 0
    tens = 0
    fives = 0
    twos = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickels = 0

    if total >= 20:
        # number of 20s 
        twenties = math.floor(total // 20)

        # reste for the number of 10s
        rest_10 = total - (twenties * 20)

        total = rest_10 

        print(twenties)

    elif total >= 10:
        # number of 10s 
        tens = math.floor(total // 10)

        # reste pour le # de 5 
        rest_5 = total - (tens * 10)

        total = rest_5

        print(tens)

    elif total >= 5:
        # nombre de 5s
        fives = math.floor(total // 5)

        # reste pour # 1$
        rest_1 = total - (fives * 5)

        total = rest_1


    
    elif total >= 2:
        # nombre de 5s
        twos = math.floor(total // 2)

        # reste pour # 1$
        rest_1 = total - (fives * 2)

        total = rest_1



    elif total >= 1:
        # nombres de 1s
        ones = math.floor(total // 1)

        # reste pour 25c
        reste_25c = total - (ones * 1)

        total = reste_25c
        

    elif total >= 0.25:
        # nombres de 25c 
        quarters = math.floor(total // 0.25)

        # reste pour 10c 
        reste_10c = total - (quarters * 0.25)

        total = reste_10c




    elif total >= 0.10:
        # nombre de 10c
        dimes = math.floor(total//0.10)

        # reste pour 5c 
        reste_5c = total - (dimes * 0.10)

        total = reste_5c


    elif total >= 0.05:
        # nombre de 5c
        nickels = math.floor(total//0.05)


    return twenties, tens, fives, twos, ones, quarters, dimes, nickels



def format_base(value, base, digit_letters):
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres.
    # `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    result = ""
    if value > 0:
        if base == 16:
            # pour le transformer en hex
            result = hex(value)

            return result
        
        if base == 10:
            result = value

            return result
        
        if base == 2:
            result = bin(value)

            return result
        
    if value < 0:
        # find the absolute value
        abs_value = abs(value)
        # TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
        if base == 16:
            # pour le transformer en hex
            result = hex(abs_value)

            return result
        
        if base == 10:
            result = abs_value

            return result
        
        if base == 2:
            result = bin(abs_value)

            return result
        
        if value == 0:
            result = 0
            
            return result


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(point_in_circle([-1, 1], [1, -1], 2))
    print(cash(137.38))
    print(format_base(-42, 16, "0123456789ABCDEF"))
