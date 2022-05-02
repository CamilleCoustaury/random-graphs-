#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:26:54 2022

@author: camille
"""

import numpy as np
import random as rd


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
    

def gready(d_U,d_v):
    #input :  two sequences5 of nonnegative integers
    #d_u de taille N 
    #d_v de taille T
    T=len(du_v)
    M0=[]
    eps0=[]
    #H0=half edges de U
    #p=permutation de 1:kt
    for i in range(kt):
        
        
        
        

### TEST ###

test = graph_generator(4,5,8)