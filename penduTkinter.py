#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programme du pendu version graphique
Eliott RAJAUD
11/12/20
TODO : Pendu en tkinter
"""

from tkinter import Tk,Label, Button,Frame,Entry,StringVar,Canvas,PhotoImage
from fonctionPendu import choixMot, lettreCorrect, dejaUtiliser,bestScore

mot=choixMot
motAChercher = ""
chance = 8  
mot=choixMot()
lettreTrouve = mot[0]
lettreJouer = [mot[0]]
ListeImage = ['bonhomme1.gif','bonhomme2.gif','bonhomme3.gif','bonhomme4.gif','bonhomme5.gif','bonhomme6.gif','bonhomme7.gif','bonhomme8.gif']

MonPendu = Tk()
MonPendu.title('Pendu version graphique')
MonPendu.geometry('1000x500+500+200')


LettreTrouver=Label(MonPendu, text = '_ _ _ _ _ ')
LettreTrouver.pack()

lettre=StringVar()
saisie = Entry(MonPendu, textvariable=lettre, bg='cyan')
saisie.focus_set()
saisie.pack()


Proposition = Button(MonPendu, text ='Proposer ma lettre', fg = 'black', command = lettreCorrect(mot,lettreTrouve,motAChercher))
Proposition.pack()


ButtonQuit = Button(MonPendu , text='Quitter' , fg = 'red' , command = MonPendu.destroy)
ButtonQuit.pack()

Image = PhotoImage(file='bonhomme1.gif')
canevas = Canvas(MonPendu, width='500', height='500')
item = canevas.create_image(0,0, anchor='nw', image=Image)
print("Image de fond (item",item,")")   #A SUPPRIMMER TEST
canevas.pack()


MonPendu.mainloop()
