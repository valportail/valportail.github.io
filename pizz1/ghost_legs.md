<header>

PORTAIL Valentin - Prép'ISIMA 1 - 2021/2022

![Logo de l'UCA](images/logo_uca.png) ![Logo de l'ISIMA - Clermont Auvergne INP](images/logo_isima.png)

[Lien vers la page Web](https://perso.isima.fr/~vaportail/ghost_legs.html)

![Image d'un amidakuji dans une garderie](images/ghost_leg.jpg)

</header>

-------------------------------------

## Introduction du problème

Cet exercice s'inspire d'un jeu de loterie asiatique, l'_Amidakuji_.
Il se joue sur une grille composé de plusieurs lignes verticales,
appelées colonnes dans le reste de ce rapport,
connectées entre elles par plusieurs lignes horizontales.
Il est impossible de mettre deux lignes horizontales l'une en face de l'autre.

La grille ci-dessous est reprise de l'énoncé de Codingame :
```
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3
```

Pour jouer, on commence par choisir une valeur de départ en haut de la grille,
puis on suit la ligne verticale correspondante de haut en bas.
Si on croise une ligne horizontale, il faut la suivre.
On arrive donc sur une autre ligne verticale que l'on suit et ainsi de suite.

A la fin, on tombe sur une des trois valeurs d'arrivée en bas de la grille.

Par exemple, si on choisit la ligne A, on tombe sur la valeur 2,
si on choisit la ligne B, on tombe sur la ligne 1
et si on choisit la ligne C, on tombe sur la ligne 3.

Chaque valeur de départ est toujours liée
à une unique valeur d'arrivée en bas de la grille.

L'objectif de l'exercice est de trouver les différentes paires de valeurs,
puis de donner la liste de toutes ces paires.

Le programme prend en entrée la grille de jeu écrite en caractères ASCII,
sa hauteur et sa largeur.
Ces deux dernières valeurs doivent être comprises entre 3 et 100.

Chaque paire doit être donnée sous la forme d'une chaîne de caractères de type
"DA", où D est la valeur de départ et A la valeur d'arrivée.
Les paires seront séparées par des retours à la ligne.

## Méthode de résolution

### Description synoptique

L'idée de ma méthode de résolution est de parcourir la grille
pour chaque valeur de départ, noter la valeur d'arrivée,
puis afficher le couple de valeurs.

Pour parcourir la grille, il faut que l'algorithme puisse "descendre" la grille
en empruntant les lignes horizontales lorsqu'il y en a.

### Détail algorithmique

> **Remarque 1 :** Afin d'être fidèle aux éléments déjà donnés par Codingame,
le nom des fonctions et des variables seront en anglais.
Les commentaires du programme seront, en revanche, en français.

Le programme commence par demander à l'utilisateur
la largeur de la grille, notée _W_ (_width_ en anglais),
sa hauteur, notée _H_ (_height_ en anglais),
puis lui demande la grille complète sous forme de caractères ASCII.

Pour cela, on demande à l'utilisateur autant de fois que la hauteur de la grille
une ligne qui est stockée dans une chaîne de caractères appelée _line_.

Cette partie a déjà été préprogrammée par Codingame,
mais elle a été légèrement modifiée.
En effet, la grille, écrite en caractères ASCII, est, de plus,
stockée dans un tableau à deux dimensions appelé _diam_.

Ce tableau a une taille de 101 par 101 pour pouvoir couvrir tous les cas possibles.
On parcourt chaque ligne et on insère chaque caractère dans la tableau au bon emplacement.

> **Remarque 2 :** Pour la suite de l'algorithme, on remarque que chaque ligne verticale dans la grille
est séparée de trois caractères.

Une fonction appelée _next\_line_ permet de parcourir la grille.
Elle prend en argument une ligne de la grille nommée _line_,
la largeur de la ligne _width_ et le numéro de la colonne _column_
qui va de 0 à _width_.
Elle renvoie le numéro de la colonne où l'on doit se trouver sur la colonne suivante :

- Si elle détecte un "-" directement à gauche de la position actuelle et
si l'on ne sort pas de la grille (donc si _column_ - 3 est supérieur ou égal à 0),
elle se déplace de trois caractères à gauche et renvoie la nouvelle position.

- Sinon, si elle détecte un "-" directement à droite de la position actuelle et
si l'on ne sort pas de la grille (donc si _column_ + 3 est inférieur à _width_),
elle se déplace de trois caractères à droite et renvoie la nouvelle position.

- Sinon, elle renvoie la position actuelle.

Le programme parcourt ensuite la grille pour chaque colonne, c'est-à-dire,
pour un entier _c_ compris entre 0 et _W_ avec un pas de 3 (cf. Remarque 2).

Pour chaque colonne, il stocke la valeur initiale, qui se trouve
à la ligne 0 et à la colonne _c_, dans une variable _start_.
Pour éviter de modifier la variable _c_, il copie son contenu
dans une variable _col_.

Il parcourt ensuite la grille pour chaque ligne, sauf la dernière,
donc pour une variable _l_ allant de 0 à _H_-1 avec un pas de 1,
en se servant de la fonction _next\_line_ pour trouver
le nouvel indice de colonne qu'il stocke dans la variable _col_.

A la fin, il stocke la valeur d'arrivée, qui se trouve
à la ligne _H_ - 1 et à la colonne _col_, dans une variable _end_.
Il affiche ensuite la paire composée de _start_ et de _end_.

## Code commenté de la résolution

Voici le programme proposé, écrit en langage C :
``` c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int next_line(char line[], int width, int column) {
    if (column - 1 >= 0 && line[column-1] == '-') {
    // S'il y a un chemin à gauche et si on ne sort pas de la grille
        return column - 3; // On va 3 caractères à gauche
    } else if (column + 1 < width && line[column+1] == '-') {
    // S'il y a un chemin à droite et si on ne sort pas de la grille
        return column + 3; // On va 3 caractères à droite
    } else {
        return column; // On reste au même endroit
    }
}

int main()
{
    /* Saisie de la grille par Codingame */

    int W;
    int H;
    scanf("%d%d", &W, &H); fgetc(stdin);

    char diag[101][101]; // On crée un tableau à 2 dimensions

    for (int i = 0; i < H; ++i) {
        char line[1025];
        scanf("%[^\n]", line); fgetc(stdin);
        // On enregistre la ligne saisie par l'utilisateur
        for (int j = 0; j < W; ++j) {
            diag[i][j] = line[j]; // On stocke les valeurs dans le tableau
        }
    }

    /* Afficher la grille (pour tester, non pris en compte dans l'évaluation) */

    for (int i = 0; i < H; i++) {
        fprintf(stderr, "%s\n", diag[i]);
    }

    /* Parcourir la grille, colonne après colonne */

    for (int c = 0; c < W; c+=3) { // Pour chaque colonne
        int col = c;
        char start = diag[0][col]; // On stocke la valeur de départ
        for (int l = 0; l < H-1; ++l) { // Pour chaque ligne sauf la dernière
            col = next_line(diag[l], W, col); // On parcourt la grille
        }
        char end = diag[H-1][col]; // On stocke la valeur d'arrivée
        printf("%c%c\n", start, end); // On affiche la paire de valeurs
    }

    return 0;
}
```

## Description d'une autre solution

Cette solution a été proposée sur Codingame par l'utilisateur
"VE_FORBRYDERNE" :
``` c
#include <stdio.h>

char g[102][102];
int w, h;
int i, r, c;
char x;

int main(void) {
    /* Read first line */
    scanf("%d%d\n", &w, &h);

    /* Read rest of input */
    for (i = 0; i < h; i++)
        fgets(g[i], 102, stdin);

    for (i = 0; i < w; i += 3) {
        r = 1;
        c = i;
        x = g[0][i];
        while (r < h-1) {
            /* Move left */
            if (c && g[r][c-1] == '-') c -= 3;

            /* Move right */
            else if (g[r][c+1] == '-') c += 3;

            r += 1;
        }
        printf("%c%c\n", x, g[r][c]);
    }
}
```

Cette solution m'a séduit car elle est plutôt compacte :
elle occupe en effet 31 lignes contre 57 pour la mienne.
Elle reste cependant lisible et plutôt facilement compréhensible.

Dans cette solution, il n'y a pas de fonction et le changement de colonne
se fait directement dans la boucle _while_.
La variable _r_ correspond à la ligne et la variable _c_ à la colonne.

On peut cependant regretter la présence d'une boucle _while_ au lieu
d'une boucle _for_, ce qui aurait pu permettre de réduire davantage
la taille du code,
ainsi que l'absence d'accolades autour de certaines boucles
ne contenant qu'une seule instruction (ce qui n'est pas une erreur,
le programme s'exécutant quand même).

## Bilan des apprentissages

Lors de cet exercice, j'ai pu apprendre à :

- manier les **tableaux** et les **chaînes de caractères**,
que je n'avais pas encore vus en C.
- chercher des **informations supplémentaires** en cas de difficultés.
- **décomposer** un problème complexe en plusieurs **problèmes simples**.
- **comparer** ma solution à celles **d'autres personnes** afin d'en tirer
des améliorations potentielles.
