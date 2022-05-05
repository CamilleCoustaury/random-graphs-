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

##############################################################################

#cette fonction permet de générer un graph bipartite de base 

def graph_generator(l,r,n):
    #l = number of left edges on the bipartite graph (labelled from 0 to l-1)
    #r = number of right edges on the bipartite graph (labelled from 0 to r-1)
    #n = number of vertices 
    vertices = []
    for i in range(n):
        vertices.append([rd.randint(0,l-1),rd.randint(0,r-1)])
    return l,r,np.array(vertices)



def utility(L):
    #L = selected vertices for the alocation in the graph
    return len(L)

#this functions tells if a vertice is available or not to be added in the allocation
#une arrête n'est pas dispo si son sommet de gauche est déjà utilisé par une autre arrete de l'allocation
def available(allocation,new_vertice):
    res = True
    if (newvertice[0] in allocation[:,0]):
        res = False
    return res

def new_node(l,k,nb_vertices):
    #nb_vertices = nombre d'arretes entrant dans le noeuds de droite
    #l = nombre de noeuds de gauche
    #k = numéro du noeud de droite 
    vertices = []
    for i in range(k):
        vertices.append([rd.randint(0,l-1),k])
    return np.array([k,vertices])
        

def step_gready(allocation,new_node): 
    vertices = new_node[1] #on récupère la liste d'arrêtes 
    while len(vertices!=0):
        to_add=rd.choice(new_node[1])# on choisit une arrete au hasard 
        if available(to_add): # si elle est dispo on la choisit
            return to_add
        else:
            vertices.remove(to_add) #sinon on la retire de la liste et on en choisi une autre
    return 
    

def gready(d_U,d_V):
    #input :  two sequences5 of nonnegative integers
    #d_U de taille N = degrés des sommet de U c'est à dire le nombre de demi arrete que comporte chaque somment de U
    #d_V de taille T = degrés des sommets de V
    N=len(d_U)
    T=len(d_V)
    M=[]
    eps=[]
    #H0=half edges de U
    H=d_U[:]
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
                eps.append((i,t))#on rajoute la nouvelle arete a la liste des aretes 
                H[i]-=1 #on rend la demi-arete de U indisponible
                if (i,t) not in M:
                    M.append((i,t))
    return (eps,M)
                
            
             
                
        
        
        

### TEST ###
#d_U=[2,3,1,3]
#d_V=[2,1,2]

d_U=[2,1,2,1]
d_V=[2,4,3]

test = gready(d_U,d_V)
print(test)

