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


sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
print(frequence(sentence))
