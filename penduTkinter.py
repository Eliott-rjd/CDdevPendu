#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programme du pendu version graphique
Eliott RAJAUD
11/12/20
TODO : Faire un meilleur affichage, plus jolie
"""

from tkinter import Tk,Label, Button,Entry,StringVar,Canvas,PhotoImage
from fonctionPendu import choixMot, lettreCorrect,lettreUse

motAChercher = ""
mot=choixMot()

lettreTrouve = [mot[0]]
lettreJouer = [mot[0]]
lienImage = ['bonhomme1.gif','bonhomme2.gif','bonhomme3.gif','bonhomme4.gif','bonhomme5.gif','bonhomme6.gif','bonhomme7.gif','bonhomme8.gif']
listeImage=[]


MonPendu = Tk()
MonPendu.title('Pendu version graphique')
MonPendu.geometry('1000x500+500+200')
buttonQuit = Button(MonPendu , text='Quitter' , fg = 'red' , command = MonPendu.destroy)

#while chance !=0:
trouver=Label(MonPendu, text = lettreCorrect(mot,lettreTrouve,motAChercher))
Tentative=Label(MonPendu, text='')

lettre=StringVar()
saisie = Entry(MonPendu, textvariable=lettre, bg='cyan')
saisie.focus_set()

canevas = Canvas(MonPendu, width='500', height='500')
for i in range(len(lienImage)):
    listeImage.append(PhotoImage(file=lienImage[i]))
image = listeImage[0]
item = canevas.create_image(0,0, anchor='nw', image=image)

proposition = Button(MonPendu, text ='Proposer ma lettre', fg = 'black', command = lambda:lettreUse(lettreJouer,lettre,listeImage,canevas,item,mot,lettreTrouve,motAChercher,trouver))        



trouver.grid(row=1, sticky = "w",padx=20)
saisie.grid(row=2, sticky = "e",padx=20)
Tentative.grid(row=3, sticky = "e")
buttonQuit.grid(row=4, sticky = "e")
proposition.grid(row=2, column = 2)
canevas.grid(row=1, column=3,rowspan=4, padx=40,pady=5, sticky='nesw'  )
    
MonPendu.mainloop()
