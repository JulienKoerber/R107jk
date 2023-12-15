def saisir_personne():
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    return nom, prenom

def afficher_resultat(personnes):
    personnes_triees = sorted(personnes, key=lambda x: (x[0].upper(), x[1].title()))

    for nom, prenom in personnes_triees:
        nom_majuscules = nom.upper()
        prenom_majuscule = prenom.title()
        print(f"{prenom_majuscule} {nom_majuscules}")

if __name__ == "__main__":
    personnes = []

    for _ in range(2):
        personne = saisir_personne()
        personnes.append(personne)

    afficher_resultat(personnes)