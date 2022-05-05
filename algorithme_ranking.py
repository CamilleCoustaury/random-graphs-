import numpy as np
import random as rd
from numpy.random import permutation

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
    for t in range(T): #attention aux indices
        #on considère que les aretes d'un meme sommet sont interchangeables
        for i in range(d_R[t]):
            nb_aretes_dispo=np.sum(H)
            if nb_aretes_dispo>0:
                res=0
                curseur = 0
                for j in range (len(H)): #On détermine à quel sommet on rattache l'arête i du sommet t
                    a = H[j]*(1-L[j])
                    if a>res:
                        res = a
                        curseur = j
                eps.append((curseur,t))#on rajoute la nouvelle arete a la liste des aretes
                H[curseur]-=1 #on rend la demi-arete de L indisponible
                if (curseur,t) not in M:
                    M.append((curseur,t))
    return (eps,M)


### TEST ###
#d_U=[2,3,1,3]
#d_V=[2,1,2]

d_U=[2,1,2,1]
d_V=[2,4,3]

test = ranking(d_U,d_V)
print(test)
