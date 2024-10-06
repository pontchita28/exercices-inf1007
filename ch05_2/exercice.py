#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	# calculer le total de l'achat 
	sous_total = 0
	i = 0
	for b in range(i, len(data)):
		sous_total = round((sous_total + data[b][INDEX_QUANTITY] * data[b][INDEX_PRICE]),2)

	# calcul des taxes 
	taxes = float(round((sous_total * 0.15),2))

	# calcul du total 
	total = float(round((sous_total + taxes),2))

	# affichage de la facture 
	facture = f"{name}\nSOUS TOTAL     {sous_total} $\nTAXES           {taxes} $\nTOTAL          {total} $"

	return facture


def format_number(number, num_decimal_digits):
	return ""



def get_triangle(num_rows):
		

	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
