#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:14:36 2022

@author: camille
"""

#from time import time
import time
from random import seed
import random as rd

import tqdm as tqdm

from algorithme_ranking import ranking
from algorithme_gready import gready

import matplotlib.pyplot as plt


###### ETUDE DE TEMPS D'EXECUTION ######
def benchmark1(sizes=[3,5,10,100,1000],capacity=3, runs=100, method=ranking):
    """
    For each size in the 'sizes' list, compute the average time over a given number of runs to find the matching
    for a bipartit graph of that size,
    :param sizes: list of problem sizes to consider (default is ([3,3], [5,3], [10,10], [100,100], [1000,1000]))
    :param method: the name of the algorithm to use (default is ranking)
    :param runs: the number of repetition to perform for computing average (default is 100)
    :param capacity: max capacity of a node in the graph
    :return: nothing
    """
    print(method.__name__)
    seed(0)
    results = []
    with tqdm.tqdm(total=len(sizes) * runs, desc="Progress (" + method.__name__[:6] + ")") as bar:
        for s in sizes:
            tot = 0.0
            for _ in range(runs):
                d_L=[rd.randint(1, capacity) for x in range(s)]
                d_R=[rd.randint(1, capacity) for x in range(s)]
                t0 = time.time()
                method(d_L, d_R)
                tot += (time.time() - t0)
                bar.update(1)
            print("size : %d,time: %0.5f | " % (s, tot / float(runs)),end="\r")
            results.append(tot / float(runs))
    return {'sizes': sizes, 'avg time': results}


def benchmark2(size=[100,100],capacity=[i for i in range(1,20)], runs=100, method=ranking):
    """
    For each size in the 'sizes' list, compute the average time over a given number of runs to find the matching
    for a bipartit graph of that size,
    :param sizes: list of problem sizes to consider (default is ([3,3], [5,3], [10,10], [100,100], [1000,1000]))
    :param method: the name of the algorithm to use (default is ranking)
    :param runs: the number of repetition to perform for computing average (default is 100)
    :return: nothing
    """
    print(method.__name__)
    seed(0)
    results = []
    with tqdm.tqdm(total=len(capacity) * runs, desc="Progress (" + method.__name__[:6] + ")") as bar:
        for c in capacity:
            tot = 0.0
            for _ in range(runs):
                d_L=[rd.randint(1, c) for x in range(size[0])]
                d_R=[rd.randint(1, c) for x in range(size[1])]
                t0 = time.time()
                method(d_L, d_R)
                tot += (time.time() - t0)
                bar.update(1)
            print("capacity : %d, time: %0.5f | " % (c, tot / float(runs)), end="\r\r")
            results.append(tot / float(runs))
    return {'capacity': capacity, 'avg time': results}


def main1():
    """
    A sample main program.

    :return: nothing
    """
    algorithms = [ranking,gready]

    results = {}

    for algorithm in algorithms:
        sizes = [3,5,10,20,30,40,50,100,200,300,500]
        capacity=2
        runs = 10
        results[algorithm] = benchmark1(sizes=sizes,capacity=capacity, runs=runs, method=algorithm)
        print(algorithm)
        plt.plot(results[algorithm]['sizes'], results[algorithm]['avg time'], label=str(algorithm.__name__))

    plt.legend()
    plt.title("Matching algorithms execution time (capacity = %d )" %(capacity))
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.savefig("matching.png")
    plt.show()
    plt.close()

def main2():
    """
    A sample main program.

    :return: nothing
    """
    algorithms = [ranking,gready]

    results = {}

    for algorithm in algorithms:
        size = [100,100]
        capacity=[i for i in range(1,10)]
        runs = 10
        results[algorithm] = benchmark2(size=size,capacity=capacity, runs=runs, method=algorithm)
        print(algorithm)
        plt.plot(results[algorithm]['capacity'], results[algorithm]['avg time'], label=str(algorithm.__name__))

    #plt.show()
    plt.legend()
    plt.title("Matching algorithms execution time (size = %d )" %(size[0]))
    plt.xlabel("capacity")
    plt.ylabel("Time (s)")
    plt.savefig("matching.png")
    plt.show()
    plt.close()
    
###############################################################################################

############# ETUDE COMPETITIVE RATIO ###############################
#PLOT COMPETITIVE RATIO EN FONCTION DE LA taille de graphes #########

def benchmark3(sizes=[3,5,10,100,200],capacity=3, runs=100, method=ranking):
    """
    For each size in the 'sizes' list, compute the average time over a given number of runs to find the matching
    for a bipartit graph of that size,
    :param sizes: list of problem sizes to consider (default is ([3,3], [5,3], [10,10], [100,100], [1000,1000]))
    :param method: the name of the algorithm to use (default is ranking)
    :param runs: the number of repetition to perform for computing average (default is 100)
    :param capacity: max capacity of a node in the graph
    :return: nothing
    """
    print(method.__name__)
    seed(0)
    results = []
    with tqdm.tqdm(total=len(sizes) * runs, desc="Progress (" + method.__name__[:6] + ")") as bar:
        for s in sizes:
            card_M = 0.0
            for _ in range(runs):
                #d_L=[rd.randint(0, capacity) for x in range(s)]
                d_L=[capacity for x in range(s)]# pour les d-graphes
                #d_R=[rd.randint(0, capacity) for x in range(s)]
                d_R=[capacity for x in range(s)]# pour les d-graphes
                test = method(d_L, d_R)
                if len(test[0])>0:
                    card_M += len(test[1])/(2*s)
                #card_M += len(test[1])
                bar.update(1)
            print("size : %d competitive ratio: %0.5f" % (s, card_M))
            results.append(card_M/float(runs))
    return {'sizes': sizes, 'competitive_ratio': results}


def main3():
    """
    A sample main program.

    :return: nothing
    """
    algorithms = [ranking,gready]

    results = {}

    for algorithm in algorithms:
        sizes = [5,10,15,20,25,30,35,40,50,60,70,80,90,100]
        capacity=2
        runs = 10
        results[algorithm] = benchmark3(sizes=sizes,capacity=capacity, runs=runs, method=algorithm)
        print(algorithm)
        plt.plot(results[algorithm]['sizes'], results[algorithm]['competitive_ratio'], label=str(algorithm.__name__))

    #plt.show()
    plt.legend()
    plt.title("Matching algorithms competitive ratio (capacity = %d )" %(capacity))
    plt.xlabel("Size")
    plt.ylabel("Competitive ratio ")
    plt.savefig("matching.png")
    plt.show()
    plt.close()
##########################################################################################

#PLOT COMPETITIVE RATIO EN FONCTION DE LA CAPACITE

def benchmark4(size=[100,100],capacity=[i for i in range(1,20)], runs=100, method=ranking):
    """
    For each size in the 'sizes' list, compute the average time over a given number of runs to find the matching
    for a bipartit graph of that size,
    :param sizes: list of problem sizes to consider (default is ([3,3], [5,3], [10,10], [100,100], [1000,1000]))
    :param method: the name of the algorithm to use (default is ranking)
    :param runs: the number of repetition to perform for computing average (default is 100)
    :return: nothing
    """
    print(method.__name__)
    seed(0)
    results = []
    with tqdm.tqdm(total=len(capacity) * runs, desc="Progress (" + method.__name__[:6] + ")") as bar:
        for c in capacity:
            tot = 0.0
            for _ in range(runs):
                #d_L=[rd.randint(0, c) for x in range(size[0])]
                d_L=[c for x in range(size[0])]# pour les d-graphes
                #d_R=[rd.randint(0, c) for x in range(size[1])]
                d_R=[c for x in range(size[1])]# pour les d-graphes
                test = method(d_L, d_R)
                tot += len(test[1])/(size[0]+size[1])
                bar.update(1)
            print("capacity : %d, competitive ratio: %0.5f | " % (c, tot / float(runs)), end="\r\r")
            results.append(tot / float(runs))
    return {'capacity': capacity, 'competitive_ratio': results}



def main4():
    """
    A sample main program.

    :return: nothing
    """
    algorithms = [ranking,gready]

    results = {}

    for algorithm in algorithms:
        size = [100,100]
        capacity=[i for i in range(1,20)]
        runs = 10
        results[algorithm] = benchmark4(size=size,capacity=capacity, runs=runs, method=algorithm)
        print(algorithm)
        plt.plot(results[algorithm]['capacity'], results[algorithm]['competitive_ratio'], label=str(algorithm.__name__))

    #plt.show()
    plt.legend()
    plt.title("Matching algorithms competitive ratio (size = %d )" %(size[0]))
    plt.xlabel("capacity")
    plt.ylabel("competitive ratio")
    plt.savefig("matching.png")
    plt.show()
    plt.close()


###############################################################################################
#PLOT COMPETITIVE RATIO EN FONCTION DE LA taille de graphes pour diff??rentes capacit??s pour un algo donn??

def benchmark5(sizes=[3,5,10,100,200],capacity= 3, runs=100, method=ranking):
    """
    For each size in the 'sizes' list, compute the average time over a given number of runs to find the matching
    for a bipartit graph of that size,
    :param sizes: list of problem sizes to consider (default is ([3,3], [5,3], [10,10], [100,100], [1000,1000]))
    :param method: the name of the algorithm to use (default is ranking)
    :param runs: the number of repetition to perform for computing average (default is 100)
    :param capacity: max capacity of a node in the graph
    :return: nothing
    """
    print(method.__name__)
    seed(0)
    results = []
    with tqdm.tqdm(total=len(sizes) * runs, desc="Progress (" + method.__name__[:6] + ")") as bar:
        for s in sizes:
            card_M = 0.0
            for _ in range(runs):
                d_L=[capacity for x in range(s)]# pour les d-graphes
                d_R=[capacity for x in range(s)]# pour les d-graphes
                test = method(d_L, d_R)
                if len(test[0])>0:
                    card_M += len(test[1])/(2*s)
                bar.update(1)
            print("size : %d competitive ratio: %0.5f" % (s, card_M))
            results.append(card_M/float(runs))
    return {'sizes': sizes, 'competitive_ratio': results}


def main5():
    """
    A sample main program.

    :return: nothing
    """
    algorithms = [ranking,gready]

    results = {}

    for algorithm in algorithms:
        sizes = [10,20,30,50,100, 150, 200, 250, 300]
        #sizes = [500, 600, 700, 800, 1000]
        capacites = [2,3, 4, 6, 8]
        for i in range (len(capacites)):
            capacity=capacites[i]
            runs = 10
            results[algorithm] = benchmark5(sizes=sizes,capacity=capacity, runs=runs, method=algorithm)
            print(algorithm)
            plt.plot(results[algorithm]['sizes'], results[algorithm]['competitive_ratio'], label= "d = " + str(capacites[i]))
        #plt.show()
        plt.legend()
        plt.title("Competitive ratio en fonction de la taille - (Algorithme = " + str(algorithm.__name__) + ")")
        plt.xlabel("Size")
        plt.ylabel("Competitive ratio")
        plt.savefig(str(algorithm.__name__))
        plt.show()
        plt.close()


 ##############################################################################

if __name__ == "__main__":
    #main1()
    #main2()
    #main3()
    #main4()
    main5()