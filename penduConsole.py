#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 07:41:34 2020

https://github.com/Eliott-rjd/CS-DevPendu.git

Programme du pendu version console
Eliott RAJAUD
27/11/20
TODO : Pendu en tkinter

"""


from fonctionPendu import choixMot, lettreCorrect,affichagePendu, dejaUtiliser,bestScore

def main():  
#permet de lancer le programme sur la console et de ne pas le fonctionner en import 
#grâce au 'if' à la fin du programme
    score=[]
    jouer = input("Voulez-vous jouer ? ")
    while jouer.upper() == "OUI": 
        motAChercher = ""
        chance = 7
        
        mot=choixMot()
        lettreTrouve = mot[0]
        lettreJouer = [mot[0]]
        
        affichage=lettreCorrect(mot,lettreTrouve,motAChercher)
        print(affichage)
        
        
        while chance != 0:
            proposition = dejaUtiliser(lettreJouer)
            if proposition in mot:
                lettreTrouve += proposition
                affichage = lettreCorrect(mot,lettreTrouve,motAChercher)
                print(affichage)
               
                if "_" not in affichage:
                    print('Gagner')
                    score.append(chance)
                    break
            else:
                chance -= 1
                print(affichage)
            affichagePendu(chance,mot)
        
        jouer = input("Voulez-vous jouer ? ")
         
    best,partie = bestScore(score)
    print("Votre meilleur score est",best,"chance(s) restante(s), obtenu à la partie",partie)

if __name__ == '__main__':
    main()