""" Imports et définition des variables globales"""


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    lst = [s[0]]
    cmp = [1]
    k = 1
    n = len(s)
    while k<n:
        if s[k] == s[k-1]:
            cmp[-1] +=1
        else :
            lst.append(s[k])
            cmp.append(1)
        k+=1
    return list(zip(lst,cmp))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    # cas de base
    if not s:
        return []
    # recherche nombre de caractères identiques au premier
    cmp = 1
    while cmp < len(s) and s[0] == s[cmp]:
        cmp +=1
    # appel récursif
    return [(s[0],cmp)] + artcode_r(s[cmp:])



#### Fonction principale


def main():
    """
    >>>main()
    [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]
    [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
