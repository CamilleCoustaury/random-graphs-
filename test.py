#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:46:40 2022

@author: camille
"""

from random import seed
import random as rd
#import numpy as np

import networkx as nx
from networkx.algorithms import bipartite

from algorithme_ranking import ranking
from graph_generator import gready
import os

#clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#clearConsole()

def main(left=2,right=3):
    """
    A sample main program to test our algorithms.

    @return: None
    """
    # initialize the random generator seed to always use the same set of points
    #seed(0)
    # creates graph
    d_L=[rd.randint(1, 3) for x in range(left)]
    d_R=[rd.randint(1, 3) for x in range(right)]
    
    test = gready(d_L,d_R)
    #test = ranking(d_L,d_R)
    print (test)
    

if __name__ == "__main__":
    main()
