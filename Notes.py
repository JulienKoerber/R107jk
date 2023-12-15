def saisir_notes_et_coefficients():
    notes = []
    coefficients = []

    for i in range(1, 6):
        note = float(input(f"Veuillez entrer la note du module {i} : "))
        coefficient = int(input(f"Veuillez entrer le coefficient correspondant à la note du module {i} : "))

        notes.append(note)
        coefficients.append(coefficient)

    return notes, coefficients

def calcul_moyenne_ponderee(notes, coefficients):
    somme_produits = sum(note * coefficient for note, coefficient in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)

    moyenne_ponderee = somme_produits / somme_coefficients

    return moyenne_ponderee

if __name__ == "__main__":
    notes, coefficients = saisir_notes_et_coefficients()
    moyenne_ponderee = calcul_moyenne_ponderee(notes, coefficients)

    print(f"La moyenne pondérée est : {moyenne_ponderee}")