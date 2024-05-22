import string
alphabet=string.ascii_lowercase
ALPHABET=string.ascii_uppercase
message_a_coder=str(input('Entez la chaine de caractères à coder: '))
print(message_a_coder)
#encodage d'une chaîne de caratères rentrée par l'utilisateur
clé=int(input('Quel est la clé de codage, entrez un entier positif ou négatif: '))
longueur_message=len(message_a_coder)
message_codé=''
for i in range(longueur_message):
    indice=alphabet.find(message_a_coder[i])
    indice_corrigé = (indice + clé) % 26
    #pour un espace l'indice dans l'aphabet est -1, donc on créé une boucle if lorsque indice==-1
    # on ajoute un espace à la chaine de caratères message_codé
    if indice==-1:
        message_codé+=' '
    elif indice_corrigé<=25:
        message_codé+=alphabet[indice_corrigé]
    elif indice_corrigé>25:
        message_codé+=alphabet[indice_corrigé-26]
print(message_codé)