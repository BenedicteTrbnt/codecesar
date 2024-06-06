Ce code permet de coder et décoder des messages à l'aide de la méthode du code cesar, de plus il possède un version brute force si l'utilisateur à perdu à clé de déchiffrage.

Premièrement utilisateur choisi si il veut entrer le message à coder/décoder dans la console (c), ou si il veut importer un fichier .txt (f) ou quitter le programme.
Ensuite l'utilisateur choisi si il veut encrypter (e), décoder (d) le message ou si il veut utiliser la méthode brute force pour retrouver la clé (b).
Lors de l'utilisation de la méthode brute force l'utilisateur devra intéragir avec le code (oui/non) afin de vérifier si le message codé aurait du sens.

Le code est composé : - d'une focntion unifier qui permet d'unifier le texte avant son traitement (accents)
                      - d'une fonction codage_cesar qui permet de retourner le message coder à l'aide d'une clé
                      - d'une fonction decodage_cesar qui retourne le message décoder, elle utilise la fonction codage_cesar
                      - d'une fonction traitement qui permet de lire et recupérer le texte contenu dans le fichier donné par l'utilisateur
                      - d'une fonction brute force qui teste toutes les clés possibles pour trouver la bonne clé à l'aide de l'utilisateur
                      
                      
