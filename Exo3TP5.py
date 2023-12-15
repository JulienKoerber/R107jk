def est_palindrome(chaine):
    # Retire les caractères non alphabétiques
    chaine_epuree = ''.join(caractere for caractere in chaine if caractere.isalpha())

    # Convertit la chaîne en minuscules pour la comparaison insensible à la casse
    chaine_epuree = chaine_epuree.lower()

    # Vérifie si la chaîne épurée est un palindrome
    return chaine_epuree == chaine_epuree[::-1]

# Lit une chaîne de caractères du clavier
chaine = input("Entrez une chaîne de caractères : ")

# Teste si la chaîne est un palindrome
if est_palindrome(chaine):
    print("La chaîne est un palindrome.")
else:
    print("La chaîne n'est pas un palindrome.")