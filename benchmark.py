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
from graph_generator import gready

import matplotlib.pyplot as plt


def benchmark1(sizes=([3,3], [5,3], [10,10], [100,100], [1000,1000]),capacity=3, runs=100, method=ranking):
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
                d_L=[rd.randint(1, capacity) for x in range(s[0])]
                d_R=[rd.randint(1, capacity) for x in range(s[1])]
                t0 = time.time()
                method(d_L, d_R)
                tot += (time.time() - t0)
                bar.update(1)
            print("size %d time: %0.5f" % (s[0], tot / float(runs)))
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
            print("capacity %d time: %0.5f" % (capacity[0], tot / float(runs)))
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
        #sizes = (*range(10, 11, 1), *range(1000, 10001, 1000))
        sizes = ([3,3], [5,5], [10,10],[20,20],[30,30],[40,40],[50,50],[100,100],[200,200])
        capacity=3
        runs = 10
        results[algorithm] = benchmark1(sizes=sizes,capacity=capacity, runs=runs, method=algorithm)
        print(algorithm)
        plt.plot(results[algorithm]['sizes'], results[algorithm]['avg time'], label=str(algorithm.__name__))

    #plt.show()
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
        #sizes = (*range(10, 11, 1), *range(1000, 10001, 1000))
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

if __name__ == "__main__":
    main1()
    #main2()


def benchmark3(sizes=([3,3], [5,3], [10,10], [100,100], [1000,1000]),capacity=3, runs=100, method=ranking):
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
                d_L=[rd.randint(1, capacity) for x in range(s[0])]
                d_R=[rd.randint(1, capacity) for x in range(s[1])]
                test = method(d_L, d_R)
                card_M = len(test[1])
                bar.update(1)
            print("size %d time: %0.5f" % (s[0], card_M)) #C'est quoi ce charabia?
            results.append(card_M)
    return {'sizes': sizes, 'competitive_ratio': results}


def main3():
    """
    A sample main program.

    :return: nothing
    """
    algorithms = [ranking,gready]

    results = {}

    for algorithm in algorithms:
        #sizes = (*range(10, 11, 1), *range(1000, 10001, 1000))
        sizes = ([3,3], [5,5], [10,10],[20,20],[30,30],[40,40],[50,50],[100,100],[200,200],[500,500])
        capacity=3
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