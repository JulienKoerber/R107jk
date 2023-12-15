def calculer_salaire(nombre_heures, salaire_horaire):
    salaire_total = 0

    # Calcul du salaire pour les 160 premières heures
    if nombre_heures <= 160:
        salaire_total = nombre_heures * salaire_horaire
    else:
        salaire_total = 160 * salaire_horaire  # salaire pour les 160 premières heures

        # Calcul du salaire pour les heures entre 161 et 200 avec une majoration de 25%
        if nombre_heures <= 200:
            heures_supplementaires = nombre_heures - 160
            salaire_total += heures_supplementaires * salaire_horaire * 1.25
        else:
            # Calcul du salaire pour les 40 heures supplémentaires au-delà de 200 avec une majoration de 50%
            salaire_total += 40 * salaire_horaire * 1.25
            heures_supplementaires = nombre_heures - 200
            salaire_total += heures_supplementaires * salaire_horaire * 1.5

    return salaire_total

# Exemple d'utilisation du programme
heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_total = calculer_salaire(heures_travaillees, salaire_horaire)
print(f"Le salaire total est : {salaire_total}")