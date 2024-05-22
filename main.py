import string
alphabet_min=string.ascii_lowercase
alphabet_maj=string.ascii_uppercase
liste_caracteres_speciaux=[' ','!','?','#','@','&','(',')','-',';','_',',',';','.','/',':','=','+']
chiffres=['0','1','2','3','4','5','6','7','8','9']
message_a_coder=str(input('Entez la chaine de caractères à coder: '))
#encodage d'une chaîne de caratères rentrée par l'utilisateur
clé=int(input('Quel est la clé de codage, entrez un entier positif ou négatif: '))
longueur_message=len(message_a_coder)
message_codé=''
for i in range(longueur_message):
    # Premier cas le caractère est un caractère spécial, un espace ou un chiffre, dans ce cas on affiche
    # la même chose dans le message codé
    if message_a_coder[i] in liste_caracteres_speciaux or message_a_coder[i] in chiffres:
        message_codé+=message_a_coder[i]
    # le caractère est une minuscule
    elif message_a_coder[i] in alphabet_min:
        indice=alphabet_min.find(message_a_coder[i])
        indice_corrigé = (indice + clé) % 26
        if indice_corrigé<=25:
            message_codé+=alphabet_min[indice_corrigé]
        elif indice_corrigé>25:
            message_codé+=alphabet_min[indice_corrigé-26]
    # le caractère est une majuscule
    elif message_a_coder[i] in alphabet_maj:
        indice = alphabet_maj.find(message_a_coder[i])
        indice_corrigé = (indice + clé) % 26
        if indice_corrigé <= 25:
            message_codé += alphabet_maj[indice_corrigé]
        elif indice_corrigé > 25:
            message_codé += alphabet_maj[indice_corrigé - 26]
print('Le message encodé est : ' + message_codé)