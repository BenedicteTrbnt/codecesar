# modifié pour donner la possibilité de saisir du texte ou de sélectionner un fichier à encoder/décoder

import string

# Définition de l'alphabet en minuscules et majuscules, caractères spéciaux et chiffres
alphabet_min = string.ascii_lowercase
alphabet_maj = string.ascii_uppercase
liste_caracteres_speciaux = [' ', '!', '?', '#', '@', '&', '(', ')', '-', ';', '_', ',', ';', '.', '/', ':', '=', '+']
chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Fonction pour lire un fichier texte
def lire_fichier(chemin_fichier):
    try:
        with open(chemin_fichier, 'r') as fichier:
            return fichier.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {chemin_fichier} n'a pas été trouvé.")
        exit()

# Demander à l'utilisateur s'il souhaite saisir le texte ou importer un fichier
print("Voulez-vous saisir le texte ou importer un fichier .txt ?")
print("1: Saisir le texte")
print("2: Importer un fichier .txt")
option = input("Entrez votre choix (1 ou 2): ").strip()

# Si l'utilisateur choisit de saisir le texte manuellement
if option == '1':
    message_a_decoder = input('Entrez la chaîne de caractères à coder: ')
# Si l'utilisateur choisit d'importer un fichier
elif option == '2':
    chemin_fichier = input('Entrez le chemin du fichier: ')
    message_a_decoder = lire_fichier(chemin_fichier)
else:
    print("Option non valide.")
    exit()

# Demander la clé de codage
cle = int(input('Quelle est la clé de codage ? Entrez un entier positif ou négatif: '))
longueur_message = len(message_a_decoder)
message_code = ''

# Codage du message saisi ou lu depuis le fichier
for i in range(longueur_message):
    # Premier cas : le caractère est un caractère spécial, un espace ou un chiffre
    if message_a_decoder[i] in liste_caracteres_speciaux or message_a_decoder[i] in chiffres:
        message_code += message_a_decoder[i]
    # Le caractère est une minuscule
    elif message_a_decoder[i] in alphabet_min:
        indice = alphabet_min.find(message_a_decoder[i])
        indice_corrige = (indice + cle) % 26
        message_code += alphabet_min[indice_corrige]
    # Le caractère est une majuscule
    elif message_a_decoder[i] in alphabet_maj:
        indice = alphabet_maj.find(message_a_decoder[i])
        indice_corrige = (indice + cle) % 26
        message_code += alphabet_maj[indice_corrige]

# Afficher le message codé
print('Le message codé est : ' + message_code)

# Demander à nouveau la clé de décodage
cle = int(input('Quelle est la clé de décodage ? Entrez un entier positif ou négatif: '))
message_decode = ''
longueur_message_code = len(message_code)  # Assurer que nous utilisons la longueur du message codé

# Décodage du message codé
for i in range(longueur_message_code):
    # Premier cas : le caractère est un caractère spécial, un espace ou un chiffre
    if message_code[i] in liste_caracteres_speciaux or message_code[i] in chiffres:
        message_decode += message_code[i]
    # Le caractère est une minuscule
    elif message_code[i] in alphabet_min:
        indice = alphabet_min.find(message_code[i])
        indice_corrige = (indice - cle) % 26
        message_decode += alphabet_min[indice_corrige]
    # Le caractère est une majuscule
    elif message_code[i] in alphabet_maj:
        indice = alphabet_maj.find(message_code[i])
        indice_corrige = (indice - cle) % 26
        message_decode += alphabet_maj[indice_corrige]

# Afficher le message décodé
print('Le message décodé est : ' + message_decode)
