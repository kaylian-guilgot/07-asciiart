"""Programme qui encode une chaine de caractères par une liste de tuples"""
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)

#### Fonctions secondaires

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    c = [s[0]]
    o = [1]
    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            o[-1]+=1
        else:
            c.append(s[k])
            o.append(1)

    return list(zip(c, o))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée
    en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # cas de base
    if not s:
        return []
    # recherche nombre de caractères identiques au premier
    i = 1
    while i < len(s) and s[0] == s[i]:
        i+=1
    return [(s[0], i)] + artcode_r(s[i:])

#### Fonction principale

def main():
    """Appel aux fonctions secondaires pour vérifier leur bon fonctionnement"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
