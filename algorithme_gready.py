#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:26:54 2022

@author: camille
"""
######## IMPORTATIONS #########
import numpy as np
import random as rd
from numpy.random import permutation
import networkx as nx
from networkx.algorithms import bipartite

##############################################################################
    

def gready(d_U,d_V,affichage=False):
    #input :  two sequences5 of nonnegative integers
    #d_U de taille N = degrés des sommet de U c'est à dire le nombre de demi arrete que comporte chaque somment de U
    #d_V de taille T = degrés des sommets de V
    N=len(d_U)
    T=len(d_V)
    M=[]
    eps=[]
    #H0=half edges de U
    H=d_U[:]
    ##### Pour le tracé #####
    U=["L"+str(i) for i in range(len(d_U))]
    V=["R"+str(i) for i in range(len(d_V))]
    G = nx.Graph()
    G.add_nodes_from(U, bipartite=0)
    G.add_nodes_from(V,bipartite=1)
    ########################
    for t in range(T): #attention aux indices
        #Pt=permutation(np.arrange(d_V[t]))
        #on considère que les aretes d'un meme sommet sont interchangeables   
        for i in range(d_V[t]):
            nb_aretes_dispo=np.sum(H)
            #sert à selectionner une demi-arete uniformément dans les demi-aretes encore dispo de U
            if nb_aretes_dispo>0:
                curseur = rd.randrange(1,nb_aretes_dispo+1)
                res=0
                i=0
                while res<curseur:
                    res+=H[i]
                    i+=1
                i-=1 #c'est le sommet de la demi arrete encore dispo de U qu'on selectionne 
                eps.append(("L"+str(i),"R"+str(t)))#on rajoute la nouvelle arete a la liste des aretes 
                H[i]-=1 #on rend la demi-arete de U indisponible
                if "L"+str(i) not in M :
                    if "R"+str(t) not in M:
                        M.append("L"+str(i))
                        M.append("R"+str(t))
                G.add_edges_from(eps)
                if affichage:
                    nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, U), width = 2)
    return (eps,M)
                
            
             
                
        
        
        

### TEST ###
#d_U=[2,3,1,3]
#d_V=[2,1,2]

#d_U=[2,1,2,1]
#d_V=[2,4,3]

#test = gready(d_U,d_V)
#print(test)

