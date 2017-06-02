#coding: utf-8

import os
import numpy        as np
import numpy.random as npr
import tree

class Individual(object):
    """
    Individual Class

    example: individual = [0, 1, 0, ... , 0]
    """
    def __init__(self):
        self.gene = None
        self.fit  = None

    def createGene(self, inputs, function, gene):
        """
        Create gene with dataset

        :param list     inputs:   inputs
        :param Function function: functions
        :param int gene:          Size of gene
        :returns:                 gene
        :rtype:                   list[int]
        """
        t = tree.Tree()
        t.build(inputs, function, number_of_node=gene)
        self.gene = t

    def setGene(self, gene):
        """
        Set gene

        :param gene: gene
        """
        self.gene = gene
        
    def getGene(self):
        """
        :returns: gene
        :rtype:   list[int]
        """
        return (self.gene)

    def setFitness(self, fit):
        """
        Set fitness

        :param fit: fitness
        """
        self.fit = fit

    def getFitness(self):
        """
        Get fitness

        :returns: fitness
        :rtype:   int
        """
        return (self.fit)
    
    def show(self):
        """
        This individual show infomation
        """
        print(self)
        print("\tgene    is ", self.gene)
        print("\tfitness is ", self.fit)

if __name__ == "__main__":
    individual = Individual()
    function = tree.Function()
    function.createFunction('+', 2, lambda a:a[0]+a[1])
    function.createFunction('-', 2, lambda a:a[0]-a[1])
    function.createFunction('*', 2, lambda a:a[0]*a[1])
    function.createFunction('/', 2, lambda a:a[0]/a[1] if a[1]!=0 else 0)
    inputs   = [i for i in range(10)]

    individual.createGene(inputs, function, 10)
    individual.show()
