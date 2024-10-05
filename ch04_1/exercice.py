#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    # prendre la longeur de la chaine
    longeur = len(string)
    
    # si la longueur % 2 == 0: retourner vrai
    # sinon, faux

    if longeur % 2 ==0:
        return True
    else:
        return False


def remove_third_char(string: str) -> str:
    # on va transformer le string en liste
    # enlever le 3ème index 
        # list.pop(2)
    # join la liste pour faire un str
    # retourner le str

    # liste pour le string 
    string_list = list(string)

    # enlever le 3ème index de la liste
    string_list.pop(2)

    # join la liste pour avoir un str
    new_str = "".join(string_list)

    return (new_str)



def replace_char(string: str, old_char: str, new_char: str) -> str:
    # on a le str complet et le transformer en liste
    # besoin de prendre l'index du old_char
    # à cet index, on va le remplacer avec le new_char 
    
    
    # transformation du str en liste
    string_list = list(string)

    # besoin de le faire pour toutes les occurences du old_char 
    
    # créer une liste d'index 
    index_list = []

    # retrouver l'index du old_char à chaque fois dans tout le mot
    i = 0
    for b in range(i, len(string_list)):
        if string_list[b] == old_char:
            index_list.append(b)
            i += 1


    for j in range(0, len(index_list)):
        for k in range(0, len(string_list)):
            if index_list[j] == k:
                string_list[k] = new_char


    new_str = "".join(string_list)

    return new_str



def get_number_of_char(string: str, char: str) -> int:
    # besoin de trouver toutes les occurences d'un char 
    string_list = list(string)

    count = 0
    for b in range(0, len(string_list)):
        if string_list[b] == char:
            count += 1 
    
    return count



def get_number_of_words(sentence: str, word: str) -> int:
    # compter le nombre de fois qu'un mot apparait dans une phrase 
    # comme c'est une phrase, on peut la split en liste avec " "
    sentence_list = sentence.split(" ")

    count = 0
    for i in range(0, len(sentence_list)):
        if sentence_list[i] == word:
            count += 1 
    
    return count


get_number_of_words("Comment allez vous aller chez vous", "vous")


"""
def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
"""