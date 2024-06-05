import string
alphabet_min=string.ascii_lowercase
alphabet_maj=string.ascii_uppercase
liste_caracteres_speciaux=[' ','!','?','#','@','&','(',')','-',';','_',',',';','.','/',':','=','+']
chiffres=['0','1','2','3','4','5','6','7','8','9']

def unifier(b):
    from unicodedata import normalize
    return(normalize('NFD',b).encode('ASCII', 'ignore').decode('utf8'))

def codage_cesar(message_a_coder, clé) :

    message_a_coder=unifier(message_a_coder)
    longueur_message = len(message_a_coder)
    message_codé = ''
    for i in range(longueur_message):
        # Premier cas le caractère est un caractère spécial, un espace ou un chiffre, dans ce cas on affiche
        # la même chose dans le message codé
        if message_a_coder[i] in liste_caracteres_speciaux or message_a_coder[i] in chiffres:
            message_codé += message_a_coder[i]
        # le caractère est une minuscule
        elif message_a_coder[i] in alphabet_min:
            indice = alphabet_min.find(message_a_coder[i])
            indice_corrigé = (indice + clé) % 26
            if indice_corrigé <= 25:
                message_codé += alphabet_min[indice_corrigé]
            elif indice_corrigé > 25:
                message_codé += alphabet_min[indice_corrigé - 26]
        # le caractère est une majuscule
        elif message_a_coder[i] in alphabet_maj:
            indice = alphabet_maj.find(message_a_coder[i])
            indice_corrigé = (indice + clé) % 26
            if indice_corrigé <= 25:
                message_codé += alphabet_maj[indice_corrigé]
            elif indice_corrigé > 25:
                message_codé += alphabet_maj[indice_corrigé - 26]
    return message_codé

def decodage_cesar(message_a_coder, clé) : #fonction de décodage
    return codage_cesar(message_a_coder, -clé)

def traitement(): #fonction pour choisir l'action et ouvrir un fichier personnalisé
    action_tr = input("voulez vous coder (c), décoder (d) ou trouver la clé (b)").lower()
    fichier = input("entrez le chemin de fichier : ")

    try:
        with open(fichier, 'r', encoding='utf-8') as fichier:
            message_a_coder = fichier.read()
        if action_tr == 'c':
            clé = int(input("entrez la clé : "))
            resultat = codage_cesar(message_a_coder, clé)
        elif action_tr == 'd':
            clé = int(input("entrez la clé : "))
            resultat = decodage_cesar(message_a_coder, clé)
        elif action_tr == 'b':
            resultat = brute_force(message_a_coder)
        else:
            print("Action non reconnue.")
            return
        print(f"Résultat:\n{resultat}")
    except FileNotFoundError:
        print("Fichier non trouvé. Veuillez vérifier le nom du fichier et réessayer.")

def brute_force(message_a_coder): #fonction pour déviner la clé de codage
    for clé in range(26):
        texte_decodage = decodage_cesar(message_a_coder, clé)
        print(f"Essai avec la clé {clé}: {texte_decodage}")
        entree_utilisateur = input("Est-ce que ce texte a du sens? (o/n): ").lower()
        if entree_utilisateur == 'o':
            print(f"Le texte a été décrypté avec la clé {clé}: {texte_decodage}")
            return texte_decodage, clé
    print("Aucune clé valide trouvée.")
    return None, None

def main() : #fonction principale de programme
    print("ce programme permet de crypter, décrypter ou deviner la clé de cryptage d'un texte ou d'un fichier donné")
    while True:
        choix = input("choisissez une option: console (c), fichier (f) ou quitter (q): ").lower()
        if choix == 'c':
            message_a_coder = input("Entrez le texte: ")
            if not message_a_coder:
                print("Le texte ne peut pas être vide.")
                continue
            action = input("Voulez-vous encrypter (e), décrypter (d) ou trouver la clé (b) ? ").lower()
            if action == 'e':
                try:
                    clé = int(input("Entrez la clé: "))
                except ValueError:
                    print("la clé doit être un entier.")
                    continue
                print("Texte encrypté: ", codage_cesar(message_a_coder, clé))
            elif action == 'd':
                try:
                    clé = int(input("Entrez la clé: "))
                except ValueError:
                    print("la clé doit être un entier.")
                    continue
                print("Texte décrypté: ", decodage_cesar(message_a_coder, clé))
            elif action == 'b':
                brute_force(message_a_coder)
            else:
                print("Action non reconnue.")
        elif choix == 'f':
            traitement()

        elif choix == 'q':
            break
        else:
            print("Choix non reconnu. Veuillez essayer à nouveau.")
if __name__ == "__main__":
    main()
