import string
alphabet_min=string.ascii_lowercase
alphabet_maj=string.ascii_uppercase
message_a_coder=str(input('Entez la chaine de caractères à coder: '))
#encodage d'une chaîne de caratères rentrée par l'utilisateur
clé=int(input('Quel est la clé de codage, entrez un entier positif ou négatif: '))
longueur_message=len(message_a_coder)
message_codé=''
for i in range(longueur_message):
    a=message_a_coder[i]
    if message_a_coder[i]==' ':
        message_codé+=' '
    elif message_a_coder[i] in alphabet_min:
        indice=alphabet_min.find(message_a_coder[i])
        indice_corrigé = (indice + clé) % 26
    #pour un espace l'indice dans l'aphabet est -1, donc on créé une boucle if lorsque indice==-1
    # on ajoute un espace à la chaine de caratères message_codé
        #if indice==-1:
            #message_codé+=' '
        if indice_corrigé<=25:
            message_codé+=alphabet_min[indice_corrigé]
        elif indice_corrigé>25:
            message_codé+=alphabet_min[indice_corrigé-26]
    elif message_a_coder[i] in alphabet_maj:
        indice = alphabet_maj.find(message_a_coder[i])
        indice_corrigé = (indice + clé) % 26
        #if indice == -1:
            #message_codé += ' '
        if indice_corrigé <= 25:
            message_codé += alphabet_maj[indice_corrigé]
        elif indice_corrigé > 25:
            message_codé += alphabet_maj[indice_corrigé - 26]
print(message_codé)