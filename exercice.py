#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    a = False
    if len(string)%2 == 0:
        a = True

    return a


def remove_third_char(string: str) -> str:
    x=range(len(string))
    nouvelle_chaine = ''
    for i in x:
        if i != 2:
            nouvelle_chaine += string[i]
    return nouvelle_chaine


def replace_char(string: str, old_char: str, new_char: str) -> str:
    nouvelle_chaine = ''
    x= range(len(string))
    for i in x:
        if ord(string[i])== ord(old_char):
            nouvelle_chaine+= new_char
        else:
            nouvelle_chaine+= string[i]
    return nouvelle_chaine


def get_number_of_char(string: str, char: str) -> int:
    c=0
    x=range(len(string))
    for i in x:
        if ord(string[i]) == ord(char):
            c+=1
    return c


def get_number_of_words(sentence: str, word: str) -> int:
    c = 0
    for i in range(len(sentence)-len(word)+1):
        a = False
        for j in range(len(word)):
            if ord(sentence[i+j]) != ord(word[j]):
                a = True
                break
        if a == False:
            c += 1

    return c


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
