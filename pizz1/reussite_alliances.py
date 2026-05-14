from random import shuffle

### Affichage de la réussite ###

def carte_to_chaine(carte):
    """Prend en argument un dictionnaire représentant une carte.
    Retourne une chaîne de caractères permettant l'affichage de
    la carte correspondante."""
    
    # Affichage de la valeur
    if carte['valeur'] == 10:
        chaine = '10'
    else:
        chaine = ' ' + str(carte['valeur'])
        
    # Affichage de la couleur
    if carte['couleur'] == 'P': 
        chaine = chaine + chr(9824) # Code correspondant au pique
    elif carte['couleur'] == 'C': 
        chaine = chaine + chr(9825) # Code correspondant au coeur
    elif carte['couleur'] == 'K': 
        chaine = chaine + chr(9826) # Code correspondant au carreau
    elif carte['couleur'] == 'T':
        chaine = chaine + chr(9827) # Code correspondant au trèfle.
    return chaine

def afficher_reussite(liste_cartes):
    """Prend en argument une liste de cartes correspondant à
    l'état de la réussite à un moment donné.
    Affiche la réussite"""
    reussite = ''
    for i in range(len(liste_cartes)): # On parcourt la liste entière
        reussite = reussite + carte_to_chaine(liste_cartes[i]) + ' '
    print(reussite + '\n')

### Entrées / Sorties avec des fichiers ###

def init_pioche_fichier(fichier):
    """Prend en argument le nom d'un fichier contenant une liste de cartes.
    Renvoie la liste de cartes correspondante"""
    liste_cartes = []
    f = open(fichier) # On ouvre le fichier
    txt = f.read() # On copie son contenu dans une chaîne de caractères
    valeur = ""
    couleur = ""
    i = 0
    while i < len(txt): # On va parcourir le texte
        if txt[i] == "-": # Si on tombe sur un tiret ...
            couleur = txt[i+1] # ... on enregistre le caractère à sa droite (la couleur).
            if i + 2 < len(txt):
                i = i + 2
            else:
                i = i + 1
        elif txt[i] == " " or i == len(txt)-1: # Si on tombe sur un espace ou s'il s'agit du dernier caractère ...
            if 'A' <= valeur <= 'Z':
                liste_cartes.append({'valeur': valeur, 'couleur': couleur}) # ... on engeristre la valeur et la couleur dans un dictionnaire
            else:
                liste_cartes.append({'valeur': int(valeur), 'couleur': couleur})
            valeur = ""
            couleur = ""
            i = i + 1
        else:
            valeur = valeur + txt[i]
            i = i + 1
    f.close() # On ferme le fichier
    return liste_cartes

def ecrire_fichier_reussite(nom_fich, pioche):
    """Prend en argument un nom de fichier dans lequel il faut écrire
    la liste de cartes donnée en 2e argument.
    Ecrit la liste de cartes dans le fichier"""
    f = open(nom_fich, 'w')
    for carte in pioche:
        val = str(carte['valeur']) + '-' + str(carte['couleur']) + " " # On écrit la valeur de chaque carte
        f.write(val)
    f.close()

### Générer une pioche mélangée aléatoirement ###

def init_pioche_alea(nb_cartes=32):
    """Prend en argument le nombre de cartes (32 ou 52).
    Renvoie une liste contenant toutes les cartes du jeu puis les mélange"""
    if nb_cartes == 52:
        liste_cartes = [{'valeur': 2, 'couleur': 'C'}, {'valeur': 2, 'couleur': 'K'}, {'valeur': 2, 'couleur': 'P'}, {'valeur': 2, 'couleur': 'T'},
                        {'valeur': 3, 'couleur': 'C'}, {'valeur': 3, 'couleur': 'K'}, {'valeur': 3, 'couleur': 'P'}, {'valeur': 3, 'couleur': 'T'},
                        {'valeur': 4, 'couleur': 'C'}, {'valeur': 4, 'couleur': 'K'}, {'valeur': 4, 'couleur': 'P'}, {'valeur': 4, 'couleur': 'T'},
                        {'valeur': 5, 'couleur': 'C'}, {'valeur': 5, 'couleur': 'K'}, {'valeur': 5, 'couleur': 'P'}, {'valeur': 5, 'couleur': 'T'},
                        {'valeur': 6, 'couleur': 'C'}, {'valeur': 6, 'couleur': 'K'}, {'valeur': 6, 'couleur': 'P'}, {'valeur': 6, 'couleur': 'T'},
                        {'valeur': 7, 'couleur': 'C'}, {'valeur': 7, 'couleur': 'K'}, {'valeur': 7, 'couleur': 'P'}, {'valeur': 7, 'couleur': 'T'},
                        {'valeur': 8, 'couleur': 'C'}, {'valeur': 8, 'couleur': 'K'}, {'valeur': 8, 'couleur': 'P'}, {'valeur': 8, 'couleur': 'T'},
                        {'valeur': 9, 'couleur': 'C'}, {'valeur': 9, 'couleur': 'K'}, {'valeur': 9, 'couleur': 'P'}, {'valeur': 9, 'couleur': 'T'},
                        {'valeur': 10, 'couleur': 'C'}, {'valeur': 10, 'couleur': 'K'}, {'valeur': 10, 'couleur': 'P'}, {'valeur': 10, 'couleur': 'T'},
                        {'valeur': 'V', 'couleur': 'C'}, {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'V', 'couleur': 'T'},
                        {'valeur': 'D', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'P'}, {'valeur': 'D', 'couleur': 'T'},
                        {'valeur': 'R', 'couleur': 'C'}, {'valeur': 'R', 'couleur': 'K'}, {'valeur': 'R', 'couleur': 'P'}, {'valeur': 'R', 'couleur': 'T'},                        
                        {'valeur': 'A', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'T'}]
    elif nb_cartes == 32:
        liste_cartes = [{'valeur': 7, 'couleur': 'C'}, {'valeur': 7, 'couleur': 'K'}, {'valeur': 7, 'couleur': 'P'}, {'valeur': 7, 'couleur': 'T'},
                        {'valeur': 8, 'couleur': 'C'}, {'valeur': 8, 'couleur': 'K'}, {'valeur': 8, 'couleur': 'P'}, {'valeur': 8, 'couleur': 'T'},
                        {'valeur': 9, 'couleur': 'C'}, {'valeur': 9, 'couleur': 'K'}, {'valeur': 9, 'couleur': 'P'}, {'valeur': 9, 'couleur': 'T'},
                        {'valeur': 10, 'couleur': 'C'}, {'valeur': 10, 'couleur': 'K'}, {'valeur': 10, 'couleur': 'P'}, {'valeur': 10, 'couleur': 'T'},
                        {'valeur': 'V', 'couleur': 'C'}, {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'V', 'couleur': 'T'},
                        {'valeur': 'D', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'P'}, {'valeur': 'D', 'couleur': 'T'},
                        {'valeur': 'R', 'couleur': 'C'}, {'valeur': 'R', 'couleur': 'K'}, {'valeur': 'R', 'couleur': 'P'}, {'valeur': 'R', 'couleur': 'T'},                        
                        {'valeur': 'A', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'T'}]
    shuffle(liste_cartes) # On mélange le paquet
    return liste_cartes 

def verifier_pioche(liste_cartes, nb_cartes=32):
    """Prend en argument la liste des cartes constituant la pioche et le nombre de cartes
    Vérifie si cette pioche contient toutes les cartes d'un jeu sans doublon"""
    if len(liste_cartes) != nb_cartes:
        return False
    cartes_comptees = []
    for i in liste_cartes:
        if i in cartes_comptees:
            return False
        cartes_comptees.append(i)
    return True

### Programmer les règles de la réussite des alliances ###

def alliance(carte1, carte2):
    """Prend en argument 2 cartes.
    Renvoie True si les cartes ont la même valeur ou la même couleur et False
    si ce n'est pas le cas"""
    return carte1['valeur'] == carte2['valeur'] or carte1['couleur'] == carte2['couleur']

def saut_si_possible(liste_tas, num_tas):
    """Prend en argument la liste des cartes visibles sur le tas et un entier
    correspondant au numéro du tas.
    Vérifie s'il est possible de faire sauter le tas sur le tas précédent.
    Effectue le saut si c'est possible"""
    if len(liste_tas) >= 3 and 0 < num_tas < len(liste_tas) - 1 and alliance(liste_tas[num_tas-1], liste_tas[num_tas+1]): # On regarde s'il y a une alliance entre les 2 cartes aux extrémités
        liste_tas.pop(num_tas - 1) # On enlève la carte à gauche
        return True
    return False

def une_etape_reussite(liste_tas, pioche, affiche=False):
    """Prend en argument la liste des cartes visibles des tas de la réussite,
    la liste des cartes dans la pioche et un argument optionnel indiquant
    s'il faut afficher les états de la réussite
    Effectue une étape de la réussite, c'est-à-dire:
    - Piocher une carte
    - Faire le saut s'il est possible
    - Vérifier si cela a rendu possible d'autres sauts
    - Les effectuer si possible..."""
    
    # Etape 1 : Piocher une carte
    carte = pioche.pop(0)
    liste_tas.append(carte)
    if affiche == True:
        afficher_reussite(liste_tas)

    # Etape 2 : Faire sauter l'avant-dernière carte si possible
    changement = saut_si_possible(liste_tas, len(liste_tas) - 2)
    if changement == True and affiche == True:
        afficher_reussite(liste_tas)

    # Etape 3 : Vérifier, faire sauter si possible, recommencer
    while changement == True:
        changement = False
        i = 1
        while changement == False and i <= len(liste_tas) - 2:
            saut = saut_si_possible(liste_tas, i)
            if saut == True:
                changement = True
                if affiche == True:
                    afficher_reussite(liste_tas)
            i = i + 1

### Faire une partie ###

def reussite_mode_auto(pioche, affiche=False):
    """Prend en argument une liste de cartes correspondant au jeu déjà mélangé et
    un argument optionnel indiquant s'il faut afficher les états de la réussite.
    Joue l'ensemble de la réussite en affichant chaque étape si affiche vaut vrai.
    Renvoie la liste des cartes visibles sur les tas restants à la fin de la partie."""
    liste_pioche = list(pioche)
    if affiche == True:
        afficher_reussite(liste_pioche)
    liste_tas = []
    while len(liste_pioche) > 0:
        une_etape_reussite(liste_tas, liste_pioche, affiche)
    return liste_tas

def reglette(liste_tas):
    """Prend en argument la liste des cartes visibles sur les tas
    Affiche une "réglette" permettant de numéroter les cartes"""
    for i in range(len(liste_tas)):
        if i < 10:
            print("  " + str(i), end=" ")
        else:
            print(" " + str(i), end=" ")
    print("\n")

def reussite_mode_manuel(pioche, nb_tas_max=2):
    """Prend en argument une liste de cartes correspondant au jeu déjà mélangé et
    un argument optionnel indiquant ne nombre de tas maximum pour gagner la partie.
    Laisse le joueur jouer à la réussite en lui indiquant les actions possibles.
    Renvoie la liste des cartes visibles sur les tas restants à la fin de la partie."""
    liste_pioche = list(pioche)
    liste_tas = []
    impossible_piocher = False
    while impossible_piocher == False:
        print("Nombre de cartes dans la pioche :", len(liste_pioche), "\n")
        afficher_reussite(liste_tas)
        reglette(liste_tas)
        choix = input("Quelle action effectuer ? \n Piocher une carte (p) \n Faire un saut (s) \n Quitter (q) ")
        if choix == "p": # Si le joueur pioche...
            if len(liste_pioche) > 0:
                carte = liste_pioche.pop(0) #On enlève une carte de la pioche
                liste_tas.append(carte) # On la met sur un nouveau tas à droite des autres
            else:
                impossible_piocher = True
        elif choix == "s": # Si le joueur veut faire un saut...
            numero_carte = int(input("\nNuméro de la carte à faire sauter ")) # On lui demande quelle carte il veut faire sauter
            saut = saut_si_possible(liste_tas, numero_carte)
            if saut == False:
                print("Saut impossible")
        elif choix == "q": # Si le joueur quitte...
            while len(liste_pioche) > 0: # Toutes les cartes sont posées sur la réussite
                carte = liste_pioche.pop(0)
                liste_tas.append(carte)
                afficher_reussite(liste_tas)
                reglette(liste_tas)
            impossible_piocher = True
        else:
            print("Commande inconnue, veuillez réessayer.")
        print("")
    if len(liste_tas) <= nb_tas_max:
        print("Bravo, vous avez gagné !")
    else:
        print("Dommage, vous avez perdu")
    return liste_tas

def lance_reussite(mode, nb_cartes=32, affiche=False, nb_tas_max=2):
    """Prend en argument :
    - le mode de jeu (auto / manuel),
    - un argument optionnel indiquant s'il faut afficher les états de la réussite
    (seulement pour le mode auto)
    - et un argument optionnel indiquant ne nombre de tas maximum pour gagner
    la partie (seulement pour le mode manuel).
    Lance une partie selon les consignes données.
    Renvoie la liste des cartes visibles sur les tas restants à la fin de la partie."""
    pioche = init_pioche_alea(nb_cartes) # On mélange un jeu contenant le bon nombre de cartes
    if mode == 'auto':
        liste_tas_restants = reussite_mode_auto(pioche, afiche)
    elif mode == 'manuel':
        liste_tas_restants = reussite_mode_manuel(pioche, nb_tas_max)
    return liste_tas_restants
    
    
if __name__ == '__main__':

    """carte1 = {'valeur' : 7, 'couleur' : 'P'}
    print(carte_to_chaine(carte1))
    carte2 = {'valeur' : 10, 'couleur' : 'K'}
    print(carte_to_chaine(carte2))
    carte3 = {'valeur' : 'R', 'couleur' : 'C'}
    print(carte_to_chaine(carte3))

    afficher_reussite([{'valeur':7, 'couleur':'P'}, {'valeur':10, 'couleur':'K'}, {'valeur':'A', 'couleur':'T'}])

    #print(init_pioche_fichier("data_init.txt"))

    #ecrire_fichier_reussite("data_export.txt", [{'valeur': 'V', 'couleur': 'C'}, {'valeur': 8, 'couleur': 'P'}, {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'C'}, {'valeur': 10, 'couleur': 'P'}, {'valeur': 8, 'couleur': 'T'}, {'valeur': 8, 'couleur': 'K'}, {'valeur': 9, 'couleur': 'T'}, {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'P'}, {'valeur': 10, 'couleur': 'K'}, {'valeur': 9, 'couleur': 'P'}, {'valeur': 7, 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'T'}, {'valeur': 10, 'couleur': 'C'}, {'valeur': 9, 'couleur': 'K'}, {'valeur': 9, 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'C'}, {'valeur': 8, 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'K'}, {'valeur': 7, 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'T'}, {'valeur': 7, 'couleur': 'P'}, {'valeur': 'V', 'couleur': 'T'}, {'valeur': 7, 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'P'}, {'valeur': 10, 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'K'}, {'valeur': 'R', 'couleur': 'P'}])

    pioche = init_pioche_alea()
    #print(pioche)
    print(verifier_pioche(pioche, 32))

    print(alliance({'valeur': 7, 'couleur': 'P'}, {'valeur': 7, 'couleur': 'C'}))
    print(alliance({'valeur': 7, 'couleur': 'P'}, {'valeur': 8, 'couleur': 'C'}))

    print(saut_si_possible([{'valeur':7, 'couleur':'P'}, {'valeur':10, 'couleur':'K'}, {'valeur':9, 'couleur':'T'}], 1))"""

    lance_reussite('manuel')
