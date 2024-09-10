#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    # TODO completer la fonction ici
    # utiliser fonction ord pour transformer les caractères en ASCIII       
    # lettres maj entre 65 et 90
    # besoin de valider que les lettres sont bel et bien des lettres minuscules
    # besoin qu'elles soient entre 97 et 122

    # fonction ord(): utilisée en Python pour transformer
    # un caractère unicode en sa représentation en int 
    
    # fonction chr(): utilisée en Python pour prendre la valeur
    # unicode correspondante d'un nombre pour retourner le caractère

    # besoin de transformer premièrement les str en list
    mot_liste = list(mot)
    # pour chacun des caractères dans la liste de mot, 
    # transformer en int avec ord()
    mot_int_list = []
    for i in range(0, len(mot_liste)):
        mot_int = ord(mot_liste[i])
        mot_int_list.append(mot_int)

    # transformer chacun des ord dans mot_int_list en faisant -32
    majchr_int_list = []
    for i in range(0, len(mot_int_list)):
        majchr_int_list.append(mot_int_list[i] - 32)

    # transformer chacun des car en int
    majchr_chr_list = []
    for i in range(0, len(majchr_int_list)):
        majchr_chr_list.append(chr(majchr_int_list[i]))

    # les mettre ensemble avec la fonction join 
    result = "".join(majchr_chr_list)
    
    return result 


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
