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
    # besoin de créer un dict pour classer les valeurs en clé
    # avec leur répétion 

    new_dict = {}
    for i in range(0, len(items)):
        if items[i] not in new_dict:
            new_dict[items[i]] = 1
        else:
            new_dict[items[i]] += 1 

    for ele in new_dict:
        if new_dict[ele] > 1:
            return True
        else:
            return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    # besoin de retourner un dict avec l'étudiant
    # ayant la meilleur moyenne dans un dict


    
    # les notes sont organisées sous forme de liste

    grade_dict = {}
    
    
    
    for ele in grades:
        somme = 0
        for i in range(0, len(grades[ele])):
            somme += grades[ele][i]
        moyenne = somme / len(grades[ele])

        grade_dict[ele] = moyenne

    new_list = []
    # faire une liste avec toutes les notes 
    for ele in grade_dict:
        new_list.append(grade_dict[ele])

    sorted_new_list = sorted(new_list, reverse= True)

    best_student = {}
    for ele in grade_dict:
        if grade_dict[ele] == sorted_new_list[0]:
            best_student[ele] = sorted_new_list[0]

    return best_student


grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
best_student = best_grades(grades)
print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    # afficher toutes les lettres utilisées dans le programme plus de 5 fois
    letter_list = []
    
    for i in range(0, len(sentence)):
        if (sentence[i]).isalpha():
            letter_list.append(sentence[i])

    # make a dict to have the count of the values
    letter_dict = {}
    for i in range(0, len(letter_list)):
        if letter_list[i] not in letter_dict:
            letter_dict[letter_list[i]] = 1
        else:
            letter_dict[letter_list[i]] += 1 


    # mettre les valeurs dans une liste
    valeurs_list = []
    for ele in letter_dict:
        valeurs_list.append((letter_dict[ele], ele))


    # maintenant on va sort les tuples dans la liste
    valeurs_list_sort = sorted(valeurs_list, reverse= True)

    valeurs_liste_plus_5 = []
    # liste des valeurs plus grande que 5 
    for i in range(0, len(valeurs_list_sort)):
        for j in range(0, len(valeurs_list_sort[i])):
            if valeurs_list_sort[i][0] > 5:
                valeurs_liste_plus_5.append(valeurs_list_sort[i])

    # recréer un dict à partir des valeurs trouvées 
    dict_plus_5 = {}
    for i in range(0, len(valeurs_liste_plus_5)):
        for j in range(0, len(valeurs_liste_plus_5[i])):
            dict_plus_5[valeurs_liste_plus_5[i][1]] = valeurs_liste_plus_5[i][0]
    
    return dict_plus_5


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    # structure de données la plus appropriée est un dict 
    # clé pour le nom de recette
    # ingredients mis dans une liste qui sera attaché à la cl

    # clé du dict 
    nom_recette = input("Veuillez entrer le nom de la recette: ")

    # liste des ingrédients
    # Nombre ingrédients
    nombre = int(input("Veuillez entrer le nombre d'ingrédients: "))

    ingredient_list = []
    while len(ingredient_list) < nombre:
        ingredient = input("Veuillez entrer un ingrédient: ")
        ingredient_list.append(ingredient)

    
    # dictionnaire de recette
    dict_recipe = {}
    dict_recipe[nom_recette] = ingredient_list

    return dict_recipe


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom_recette = input("Veuillez entrer le nom de la recette que vous recherchez? ")
    if nom_recette in ingredients:
        return ingredients[nom_recette]


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
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()
    print(recipes)

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
