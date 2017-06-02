#coding: utf-8

import os
import copy
import numpy        as np
import numpy.random as npr
from individual  import Individual
from population  import Population

class Crossover(object):
    """
    Crossover Class

    Crossover Algorithm
    * One point
    * Two points
    * Random points
    """
    @classmethod
    def onePoint(self, parents, n, crate):
        """
        One point crossover

        [imagine]
        parent1: [0, 1, 1]
                            => crossover => child: [1(p1), 0(p2), 0(p2)]
        parent2: [1, 1, 0]
        
        [example]
        Crossover.Onepoint(list.parents, 5) => [crossover the parents for individuals size]

        :param list[Individual] parents: Selected parents
        :param int n: Size of individuals
        :param int crate:     Probability of crossover
        :returns: Children
        :rtype:   list[Individual]
        """
        children = []
        for i in range(n):
            child = Individual()
            parent1, parent2 = npr.choice(parents, 2, replace=False)
            gene1 = parent1.getGene().getNodeList()
            gene2 = parent2.getGene().getNodeList()
            if (len(gene1)<len(gene2)):
                gene1 = copy.deepcopy(parent2.getGene().getNodeList())
                gene2 = copy.deepcopy(parent1.getGene().getNodeList())
            else:
                gene1 = copy.deepcopy(parent1.getGene().getNodeList())
                gene2 = copy.deepcopy(parent2.getGene().getNodeList())
            idx       = [i for i in range(len(gene2))]
            if (len(gene1)!=1 and len(gene2)!=1):
                point = npr.choice(idx, 1)[0]
                if (crate>npr.random()):
                    node_parent = gene1[point].getParent()
                    gene1[point] = gene2[point]
                    gene1[point].setParent(node_parent)
            child.setGene(gene1)
            children.append(child)
        return (children)

    @classmethod
    def twoPoints(self, parents, n, crate):
        """
        Two points crossover

        [imagine]
        parent1: [0, 1, 1, 1]
                               => crossover => child: [0(p1), 1(p2), 0(p2), 1(p1)]
        parent2: [1, 1, 0, 1]

        [example]
        Crossover.Twopoints(list.parents) => [crossover the parents for individuals size]

        :param list[Individual] parents: Selected parents
        :param int n: Size of individuals
        :param int crate:     Probability of crossover
        :returns: Children
        :rtype:   list[Individual]
        """
        children = []
        for i in range(n):
            child  = Individual()
            parent1, parent2 = npr.choice(parents, 2, replace=False)
            gene1 = parent1.getGene().getNodeList()
            gene2 = parent2.getGene().getNodeList()
            if (len(gene1)<len(gene2)):
                gene1 = copy.deepcopy(parent2.getGene().getNodeList())
                gene2 = copy.deepcopy(parent1.getGene().getNodeList())
            else:
                gene1 = copy.deepcopy(parent1.getGene().getNodeList())
                gene2 = copy.deepcopy(parent2.getGene().getNodeList())
            idx      = [i for i in range(len(gene2))]
            points = npr.choice(idx, 2)
            points.sort()

            if (crate>npr.random()):
                print("before:")
                print(gene1[points[0]].show())
                print(gene1[points[1]].show())
                node_parent   = gene1[points[0]].getParent()
                node_children = gene1[points[1]].getChildren()
                gene1[points[0]:points[1]+1] = gene2[points[0]:points[1]+1]
                gene1[points[0]].setParent(node_parent)
                gene1[points[1]].setChildren(node_children)
                print("after:")
                print(gene1[points[0]].show())
                print(gene1[points[1]].show())
            exit()
            child.setGene(gene1)
            children.append(child)
        return (children)

    @classmethod
    def randomPoints(self, parents, n, crate):
        """
        Random points crossover

        [imagine]
        parent1: [0, 1, 1, 1]
                               => crossover => child: [1(p2), 1(p1), 1(p1), 1(p2)]
        parent2: [1, 1, 0, 1]

        [example]
        Crossover.Twopoints(list.parents) => [crossover the parents for individuals size]

        :param list[Individual] parents: Selected parents
        :param int n: Size of individuals
        :param int crate:     Probability of crossover
        :returns: Children
        :rtype:   list[Individual]
        """
        children = []
        idx      = [i for i in range(gene_size)]
        n_random = npr.randint(1, gene_size+1)
        for i in range(n):
            child  = Individual()
            parent1, parent2 = npr.choice(parents, 2, replace=False)
            gene1  = copy.copy(parent1.getGene())
            gene2  = parent2.getGene()
            points = npr.choice(idx, n_random, replace=False)

            if (crate>npr.random()):
                for j in points:
                    gene1[j] = gene2[j]
            child.setGene(gene1)
            children.append(child)
        return (children)

if __name__ == "__main__":
    from individual  import Individual
    from select      import Select
    import tree
    population = Population()
    function = tree.Function()
    function.createFunction('+', 2, lambda a:a[0]+a[1])
    function.createFunction('-', 2, lambda a:a[0]-a[1])
    function.createFunction('*', 2, lambda a:a[0]*a[1])
    function.createFunction('/', 2, lambda a:a[0]/a[1] if a[1]!=0 else 0)
    inputs   = [i for i in range(10)]

    for i in range(5):
        ind = Individual()
        ind.createGene(inputs, function, 10)
        ind.setFitness(0)
        population.addInd(ind)

    population.show()
    parents  = Select.Tournament(population, 5, 3, "max")
    for ind in parents:
        ind.show()
    print("Onepoint")
    children = Crossover.onePoint(parents, 5, 0.7)
    for ind in children:
        ind.show()
    print("Twopoints")
    children = Crossover.twoPoints(parents, 5, 0.7)
    for ind in children:
        ind.show()
    print("Randompoints")
    children = Crossover.randomPoints(parents, 5, 0.7)
    for ind in children:
        ind.show()
