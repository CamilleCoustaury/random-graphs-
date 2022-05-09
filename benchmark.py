#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:14:36 2022

@author: camille
"""

#from time import time
import time
from random import seed

import tqdm as tqdm

from algorithme_ranking import ranking
from graph_generator import gready

import matplotlib.pyplot as plt


def benchmark(sizes=([3,3], [5,3], [10,10], [100,100], [1000,1000]), runs=100, method=ranking):
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
    with tqdm.tqdm(total=len(sizes) * runs, desc="Progress (" + method.__name__[:6] + ")") as bar:
        for s in sizes:
            tot = 0.0
            for _ in range(runs):
                d_L=[rd.randint(1, 10) for x in range(s[0])]
                d_R=[rd.randint(1, 10) for x in range(s[1])]
                t0 = time.time()
                method(d_L, d_R)
                tot += (time.time() - t0)
                bar.update(1)
            print("size %d time: %0.5f" % (s[0], tot / float(runs)))
            results.append(tot / float(runs))
    return {'sizes': sizes, 'avg time': results}


def main():
    """
    A sample main program.

    :return: nothing
    """
    algorithms = [ranking,gready]  

    results = {}

    for algorithm in algorithms:
        #sizes = (*range(10, 11, 1), *range(1000, 10001, 1000))
        sizes = ([3,3], [5,5], [10,10],[20,20],[30,30],[40,40],[50,50],[100,100],[200,200])
        runs = 10
        results[algorithm] = benchmark(sizes=sizes, runs=runs, method=algorithm)
        print(algorithm)
        plt.plot(results[algorithm]['sizes'], results[algorithm]['avg time'], label=str(algorithm.__name__))
        
    #plt.show()
    plt.legend()
    plt.title("Matching algorithms execution time (s)")
    plt.xlabel("Size")
    plt.ylabel("Time (s)")
    plt.savefig("matching.png")
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()
