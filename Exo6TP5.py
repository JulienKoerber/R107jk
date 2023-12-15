def taille_chaine(chaine):
    taille = 0
    while chaine[taille] != '\0' and taille < 100:
        taille += 1
    return taille

def pourcentage_voyelles(chaine):
    taille = taille_chaine(chaine)
    if taille > 0:
        nb_voyelles = sum(1 for char in chaine[:taille] if char.lower() in "aeiou")
        pourcentage = (nb_voyelles / taille) * 100
        return pourcentage
    else:
        return 0

def recherche_sous_chaine(chaine, sous_chaine):
    taille_chaine_principale = taille_chaine(chaine)
    taille_sous_chaine = taille_chaine(sous_chaine)
    position = -1

    for i in range(taille_chaine_principale - taille_sous_chaine + 1):
        if chaine[i:i + taille_sous_chaine] == sous_chaine:
            position = i
            break

    return position

def nombre_occurrences(chaine, sous_chaine):
    taille_chaine_principale = taille_chaine(chaine)
    taille_sous_chaine = taille_chaine(sous_chaine)
    nb_occurrences = 0

    for i in range(taille_chaine_principale - taille_sous_chaine + 1):
        if chaine[i:i + taille_sous_chaine] == sous_chaine:
            nb_occurrences += 1

    return nb_occurrences

# Exemple d'utilisation
chaine_T = "Bienvenue dans le wagon\0"
sous_chaine_wagon = "wagon"

# 1. Taille de la chaîne T
taille_T = taille_chaine(chaine_T)
print(f"1. Taille de la chaîne T : {taille_T}")

# 2. Pourcentage de voyelles dans la chaîne T
pourcentage_voyelles_T = pourcentage_voyelles(chaine_T)
print(f"2. Pourcentage de voyelles dans la chaîne T : {pourcentage_voyelles_T}%")

# 3. Recherche de la sous-chaîne 'wagon' dans T
position_occurrence = recherche_sous_chaine(chaine_T, sous_chaine_wagon)
if position_occurrence != -1:
    print(f"3. 'wagon' est une sous-chaîne de T, début de l'occurrence : {position_occurrence}")
else:
    print("3. 'wagon' n'est pas une sous-chaîne de T.")

# 4. Nombre d'occurrences de la chaîne 'wagon' dans T
nb_occurrences_wagon = nombre_occurrences(chaine_T, sous_chaine_wagon)
print(f"4. Nombre d'occurrences de 'wagon' dans T : {nb_occurrences_wagon}")