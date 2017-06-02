#coding: utf-8
from abc import ABCMeta, abstractmethod

class GA(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def evaluate(self, ind, args):
        pass

    @abstractmethod
    def revolution(self, args):
        """
        Genetic Algorithm

        0. Define evaluation function
           example: def evaluate(ind): return(sum(ind))

        1. Prepare dataset
           example: dataset = [0, 1]

        2. Create individuals
           Individual.createInd(dataset, n, rand=True)

        3. Create population
           Population.addInd(ind)

        4. Evolution
            4-1. Evaluation population in individuals
                 * 

            4-2. Select parent1 parent2
                 * Tournament select

            4-3. Crossover parent1 parent2
                 * One point crossover
                 * Two point crossover
                 * Random point crossover

            4-4. Mutation child
        """
        pass
