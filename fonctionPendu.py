#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:01:14 2020

Fonction utilisé pour le pendu
ELiott RAJAUD
27/11/20
TODO:
"""

from random import randint

def choixMot():
    ''' Role : prendre un mot aléatoire de Mot.txt
        Entrée : Aucune car prend les variable du dessus
        Sortie : le mot choisit'''
    fichierMot = open("Mot.txt",'r')
    liste=[]
    for ligne in fichierMot:
        ligne=ligne.strip()
        liste.append(ligne)
    fichierMot.close()
    val=randint(0,len(liste)-1)
    return liste[val]

def lettreCorrect(mot,lettreTrouve,motAChercher):
    ''' Role : Verifier qu'une lettre est bien dans le mot à chercher
        Entrée: le mot qui a été selectionné, les lettres trouver par l'utilisateur,
        et le mot a chercher constitué d'underscore et des lettres trouve
        Sortie : l'affichage du mot a chercher avec les underscores remplacé par les lettres trouvé'''
    for val in mot:
        if val in lettreTrouve:    
            motAChercher += val 
        else:
            motAChercher += "_ "
    return motAChercher


def affichagePendu(chance,mot):
    ''' Role : Afficher le pendu au fur et à mesure du nombre de chance restante
        Entrée : le nombre de chance restante, le mot a afficher en cas de défaite
        Sortie : il n'y en a pas, l'affichage se fait directement dans la fonction'''
    if chance==0:
        print("Vous avez perdu, le mot était : ", mot)
        print("\n =========Y= ")
    if chance<=1:
        print(" |/       |  ")
    if chance<=2:
        print(" |        0  ")
    if chance<=3:
        print(" |       /|\ ")
    if chance<=4:
        print(" |       /|\  ")
    if chance<=5:                    
        print(" |           ")
    if chance<=6:
        print("/|            ")
    if chance<=7:
        print("==============\n")
        
def dejaUtiliser(lettreJouer):
    ''' Role : Savoir si une lettre a déja été utilisé
        Entrée : La liste des lettres joué et la proposition
        Sortie : True si la lettre a déja été joué'''
    proposition = input("Saisir lettre ")
    while proposition in lettreJouer:
        proposition = input("Lettre déja utilisé, ressaisir lettre ")
    lettreJouer.append(proposition)
    return proposition
        
def bestScore(score):
    '''' Role : Connaitre le meilleur score (le nombre de chance restante) et à quelle partie ce score
         à été obtenu.
         Entrée : Une liste de nombre de chance restante pour chaque partie joué
         Sortie : Le meileur nombre de chance restante et son numéro de partie associé'''
    best = 0
    partie = 1
    for i in range(len(score)):
        if score[i] > best:
            best = score[i]
            partie = i + 1
    return best,partie

def AffichagePenduImage():
    return