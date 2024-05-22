import string
alphabet=string.ascii_lowercase
message_a_décoder=str(input('Entez la chaine de caractères à décoder: '))
clé=int(input('Quel est la clé de décodage, entrez un entier positif ou négatif: '))
#décodage d'une chaîne de caratères rentrée par l'utilisateur
longueur_message=len(message_a_décoder)
message_décodé=''
for i in range(longueur_message):
    indice=alphabet.find(message_a_décoder[i])
    if indice+clé<=25:
        message_décodé+=alphabet[indice-clé]
    elif indice+clé>25:
        message_décodé+=alphabet[indice-clé-26]
print(message_décodé)