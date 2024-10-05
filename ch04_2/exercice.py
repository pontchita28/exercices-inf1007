#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	# noms composés qui sont séparés sur la base d'un trait
	# d'union
	# besoin d'utiliser la fonction split
	# prendre le premier qui se trouve au premier index (0)

	# faire une nouvelle chaîne de char 
	# bonjour premier prénom 

	# utilisation de la fonction split 
	name_list = name.split("-")

	# besoin de le mettre sous la forme majuscule en 
	# premier puis le reste minusucle
		# comme avec Title
	# besoin de prendre le premier index 
	first_index_val = (name_list[0]).title()

	# mettre la phrase "Bonjour, PremierPrénom"
	phrase = "Bonjour, " + first_index_val

	return phrase



def get_random_sentence(animals, adjectives, fruits):
	# chacune des entrées sont des tuples 
	# choisir un des index aléatoirement 
	rand_animal = random.choice(animals)
	rand_adj = random.choice(adjectives)
	rand_fruits = random.choice(fruits)

	phrase = f"Aujourd'hui, j'ai vu un {rand_animal} s'emparer d'un panier {rand_adj} plein de {rand_fruits}"

	return phrase



def encrypt(text, shift):
	# faire avec le code ASCII
	# pour avoir la valeur du code ASCII d'une lettre, utilisation de ord()

	# mettre le texte sous forme de liste
	text_list = (list(text.upper()))

	# prendre chacune des lettres et vérifier leur code ASCII
	# mettre la valeur des codes ASCII dans une nouvelle liste
	# avec le shift ajouté

	nouv_text_list = []
	for i in range(0, len(text_list)):
		if (text_list[i]).isalpha():
			valeur_ascii = ord(text_list[i])
			nouv_ascii = valeur_ascii + shift
			
			if 65 < nouv_ascii < 90:
				# transformation en charactère
				nouv_char = chr(nouv_ascii)
				# mettre le nouv_char dans la liste
				nouv_text_list.append(nouv_char)
			else:
				# pour toutes les lettres maj, on reste dans une boucle de 26 lettres 
				enlever = nouv_ascii - 26
				# char qui sont à enlever du ascii original
				other_ascii = enlever 
				# transformation en charactère
				nouv_char = chr(other_ascii)
				# mettre le nouv_char dans la liste
				nouv_text_list.append(nouv_char)
		else:
			nouv_text_list.append(text_list[i])



	# prendre les valeurs de chacun et les mettre dans une nouvelle liste
	# join la liste
	# retourner le str 

	# mettre la liste sous forme de str
	nouv_text = "".join(nouv_text_list)

	return nouv_text

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
