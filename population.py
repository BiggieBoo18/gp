#coding: utf-8

from individual import Individual

class Population(object):
    """
    Population Class

    example: population = [ind_1, ind_2, ind_3, ... , ind_n]
    """
    def __init__(self):
        self.ppl = []

    def addInd(self, ind):
        """
        Add individual in populaiton

        :param Individual.ind: individual class
        """
        self.ppl.append(ind)

    def setPpl(self, inds):
        """
        Set individuals as populaiton
        :param inds: individuals
        """
        self.ppl = inds

    def getPpl(self):
        """
        Get Population

        :returns: population
        :rtype:   list[Individual]
        """
        return (self.ppl)

    def calcFitness(self, func, args=None):
        """
        calculation fitness par individual

        :param func: calculation function
        """
        for ind in self.ppl:
            individual = ind.getGene()
            ind.setFitness(func(individual, args))

    def show(self):
        """
        This population show infomation        
        """
        print("Population Class")
        print("\tpopulation is ", self.ppl)
        ppl = sorted(self.ppl, key=lambda x:x.fit, reverse=True)
        for ind in ppl:
            ind.show()

if __name__ == "__main__":
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
