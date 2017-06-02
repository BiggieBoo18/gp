#coding: utf-8

import os
import copy
import numpy        as np
import numpy.random as npr
from individual  import Individual
from population  import Population

class Mutation(object):
    """
    Mutation Class
    """
    @classmethod
    def mutation(self, children, mrate, dataset):
        """
        Mutation children par child

        [imagine]
        child [0, 1, 0] => mutation => mutated child [0, 1, 1]
        
        [example]
        Mutation.mutation(children) => [mutated children for individuals size]

        :param list[Individual] children: crossover children
        :param float mrate: probability of mutation
        :param list[] dataset: prepared dataset
        :returns: mutated children
        :rtype:   list[Individual]
        """
        for child in children:
            if (mrate>npr.random()):
                gene     = child.getGene()
                n_random = npr.choice(list(range(len(gene))))
                idx      = npr.choice(list(range(len(gene))), n_random, replace=False)
                for i in idx:
                    swap_gene = npr.choice(dataset) # duplicate
                    gene[i] = swap_gene
        return (children)

if __name__ == "__main__":
    from readDataset import readDataset
    from individual  import Individual
    from select      import Select
    from crossover   import Crossover
    dataset = readDataset("./dataset/binary.txt")
    population = Population()
    for i in range(5):
        ind = Individual()
        ind.createGene(dataset, 10)
        population.addInd(ind)

    def evaluate(ind):
        fitness = sum(ind)
        return (fitness)

    population.calcFitness(evaluate)
    population.show()
    parents  = Select.Tournament(population, 5, 3, "max")
    for ind in parents:
        ind.show()
    print("Onepoint")
    children = Crossover.onePoint(parents, 5, 10, 0.7)
    for ind in children:
        ind.show()
    print("Twopoints")
    children = Crossover.twoPoints(parents, 5, 10, 0.7)
    for ind in children:
        ind.show()
    print("Randompoints")
    children = Crossover.randomPoints(parents, 5, 10, 0.7)
    for ind in children:
        ind.show()
    Mutation.mutation(children, 0.7, dataset)
