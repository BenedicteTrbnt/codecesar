import string
alphabet=string.ascii_lowercase
#print(alphabet)
#print(alphabet.find('z'))
message_a_coder=str(input('Entez la chaine de caractères à coder: '))
#encodage d'une chaîne de caratères rentrée par l'utilisateur
clé=int(input('Quel est la clé de codage, entrez un entier positif ou négatif: '))
#encodage d'une chaîne de caratères rentrée par l'utilisateur
message_a_coder=str(input('Entez la chaine de caractères à décoder: '))
longueur_message=len(message_a_coder)
#print(longueur_message)
#print(message_a_coder)
message_codé=''
for i in range(longueur_message):
    indice=alphabet.find(message_a_coder[i])
    if indice+clé<=25:
        message_codé+=alphabet[indice+clé]
    elif indice+clé>25:
        message_codé+=alphabet[indice+clé-26]
print(message_codé)