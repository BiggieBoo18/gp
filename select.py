#coding: utf-8

import os
import numpy        as np
import numpy.random as npr
from population  import Population


class Select(object):
    """
    Select Class

    Select Algorithm
    * Elite Selection
    * Tournament Selection
    """
    @classmethod
    def Elite(self, ppl, n, mode="max"):
        """
        Elite selection

        [imagine] n=3
        ind1: fit=5
        ind2: fit=5
        ind3: fit=3 => n of Elite is [ind1: fit=5,
        ind4: fit=3                   ind2: fit=5,
        ind5: fit=2                   ind3: fit=3]
        
        [example]
        Select.Elite(Population.ppl, 10, "max") => [select the highest(lowest) fitness individuals for n size]

        :param Population.ppl: populaiton class in individuals
        :return: highest fitness elite
        :rtype:  list[Individual]
        """
        reverse = True
        if (mode!="max"):
            reverse = False
        individuals = ppl.getPpl()
        individuals.sort(reverse=reverse, key=lambda x:x.getFitness())
        elite = individuals[:n]

        return (list(elite))

    @classmethod
    def Tournament(self, ppl, n, torn_size=3, mode="max"):
        """
        Tournament selection

        [imagine]
        ind1: fit=5 ===|
        ind2: fit=2 ===|===> ind3: fit=9
        ind3: fit=9 ===|

        [example]
        Select.Tournament(Population.ppl, 10, 3, "max") => [select the high(low) fitness individuals for n size]

        :param   Population.ppl: populaiton class in individuals
        :return: high(low) fitness parents
        :rtype:  list[Individual]
        """
        parents     = []
        individuals = ppl.getPpl()
        candidate   = npr.choice(individuals, (n, torn_size))
        if (mode=="max"):
            mode    = max
        else:
            mode    = min

        for inds in candidate:
            parents.append(mode(inds, key=lambda x:x.getFitness()))
        return(list(parents))

if __name__ == "__main__":
    from individual  import Individual
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
    elite    = Select.Elite(population, 2, "max")
    parents  = Select.Tournament(population, 5, 3, "max")
    print(elite)
    print(parents)
