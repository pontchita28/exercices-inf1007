#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    # TODO: demander les valeurs ici
    # demander les valeurs à l'utilisateur 
    # peuvent être n'importe quelles valeurs 
    # sort la liste
        # sorted retourne une autre liste et ne
        # modifie pas la liste originale
    if values is None:
        values = []
        while len(values) < 10:
            valeurs = input("Veuillez entrer quelque chose: ")
            values.append(valeurs)

        print(values)

        # mettre la liste en ordre 
        # utilisation de sort 
        ord_values = sorted(values)
            
        return ord_values


def anagrams(words: list = None) -> bool:
    # TODO: demander les mots ici

    # anagrammes: si on veut réarannger les mots 
    # pour former un autre 

    # pour les avoir: mettre les mots dans une liste
    # et sort les deux listes
    # si elles sont les mêmes vraies 
    # sinon, faux

    if words is None:
        mot1 = input("Veuillez entrer le premier mot: ")
        mot2 = input("Veuillez entrer le deuxième mot: ")

        # transformation des mots en listes 
        mot1_liste = list(mot1)
        mot2_liste = list(mot2)

        # mettre les lettres du mots en ordre 
        mot1_ord = sorted(mot1_liste)
        mot2_ord = sorted(mot2_liste)

        if mot1_ord == mot2_ord:
            return True
        else:
            return False



def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
