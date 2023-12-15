def decomposer_somme(somme):
    billet100 = somme // 100
    reste = somme % 100

    billet50 = reste // 50
    reste = reste % 50

    billet10 = reste // 10
    reste = reste % 10

    piece2 = reste // 2
    piece1 = reste % 2

    return billet100, billet50, billet10, piece2, piece1

if __name__ == "__main__":
    try:
        somme = int(input("Veuillez entrer une somme d'argent en euros : "))
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier.")
    else:
        if somme < 0:
            print("Erreur : Veuillez entrer une somme positive.")
        else:
            billet100, billet50, billet10, piece2, piece1 = decomposer_somme(somme)

            print(f"Nombre de billets de 100 euros : {billet100}")
            print(f"Nombre de billets de 50 euros : {billet50}")
            print(f"Nombre de billets de 10 euros : {billet10}")
            print(f"Nombre de pièces de 2 euros : {piece2}")
            print(f"Nombre de pièces de 1 euro : {piece1}")