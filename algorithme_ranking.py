import numpy as np
import random as rd
from numpy.random import permutation
import networkx as nx
from networkx.algorithms import bipartite

def ranking(d_L,d_R):
    #input :  two sequences5 of nonnegative integers
    #d_U de taille N = degrés des sommet de U c'est à dire le nombre de demi arrete que comporte chaque somment de U
    #d_V de taille T = degrés des sommets de V
    N=len(d_L)
    T=len(d_R)
    L = [rd.random() for i in range(N)]
    M=[]
    eps=[]
    H=d_L[:]
    ##### Pour le tracé #####
    U=["L"+str(i) for i in range(len(d_L))]
    V=["R"+str(i) for i in range(len(d_R))]
    G = nx.Graph()
    G.add_nodes_from(U, bipartite=0)
    G.add_nodes_from(V,bipartite=1)
    ########################
    for t in range(T): #attention aux indices
        #on considère que les aretes d'un meme sommet sont interchangeables
        for i in range(d_R[t]):
            nb_aretes_dispo=np.sum(H)
            if nb_aretes_dispo>0:
                res=0
                curseur = 0
                for j in range (len(H)): #On détermine à quel sommet on rattache l'arête i du sommet t
                    a = H[j]*(1-np.exp(L[j]-1))
                    if a>res:
                        res = a
                        curseur = j
                eps.append(("L"+str(curseur),"R"+str(t)))#on rajoute la nouvelle arete a la liste des aretes
                H[curseur]-=1 #on rend la demi-arete de L indisponible
                if (curseur,t) not in M:
                    M.append((curseur,t))
    G.add_edges_from(eps)
    #nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, U), width = 2)
    return (eps,M)


### TEST ###
#d_U=[2,3,1,3]
#d_V=[2,1,2]

#d_U=[2,1,2,1]
#d_V=[2,4,3]

#U=["L"+str(i) for i in range(len(d_U))]
#V=["R"+str(i) for i in range(len(d_V))]


#test = ranking([rd.randint(1, 3) for x in range(2)],[rd.randint(1, 3) for x in range(3)])
#test = ranking(d_U,d_V)
#print(test)

#"""
#G = nx.Graph()
#G.add_nodes_from(U, bipartite=0)
#G.add_nodes_from(V,bipartite=1)
#G.add_edges_from(test[0])
#bipartite.is_bipartite(G)
#nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, U), width = 2)
#"""