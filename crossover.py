import random
import copy

class Crossover(object):
    @classmethod
    def onePoint(self, parents, cross_rate):
        parent1 = copy.deepcopy(random.choice(parents))
        parent2 = random.choice(parents)
        if (random.random()<cross_rate):
            if (len(parent1.getGene())<len(parent2.getGene())): # always len(parent1_gene) > len(parent2_gene)
                tmp     = parent1
                parent1 = copy.deepcopy(parent2)
                parent2 = tmp
            parent1_gene = parent1.getGene()
            parent2_gene = parent2.getGene()
            parent2_gene_length = len(parent2_gene)
            idx = range(parent2_gene_length)
            point = random.choice(idx)
            # crossover
            parent1_gene[point:parent2_gene_length] = parent2_gene[point:parent2_gene_length]
        return (parent1)

    @classmethod
    def twoPoints(self, parents, cross_rate):
        parent1 = copy.deepcopy(random.choice(parents))
        parent2 = random.choice(parents)
        if (random.random()<cross_rate):
            if (len(parent1.getGene())<len(parent2.getGene())): # always len(parent1_gene)>len(parent2_gene)
                tmp     = parent1
                parent1 = copy.deepcopy(parent2)
                parent2 = tmp
            parent1_gene = parent1.getGene()
            parent2_gene = parent2.getGene()
            parent2_gene_length = len(parent2_gene)
            idx = range(parent2_gene_length)
            if (parent2_gene_length<2):
                point1 = 0
                point2 = 1
            else:
                k = 2
                point1, point2 = random.sample(idx, k)
            if (point1>point2): # always point1<point2
                tmp    = point1
                point1 = point2
                point2 = tmp
            #crossover
            parent1_gene[point1:point2] = parent2_gene[point1:point2]
        return(parent1)

    @classmethod
    def randomPoints(self, parents, cross_rate):
        parent1 = copy.deepcopy(random.choice(parents))
        parent2 = random.choice(parents)
        if (random.random()<cross_rate):
            if (len(parent1.getGene())<len(parent2.getGene())): # always len(parent1_gene)>len(parent2_gene)
                tmp     = parent1
                parent1 = copy.deepcopy(parent2)
                parent2 = tmp
            parent1_gene = parent1.getGene()
            parent2_gene = parent2.getGene()
            parent2_gene_length = len(parent2_gene)
            idx = range(parent2_gene_length)
            k    = random.choice(idx)+1
            points = random.sample(idx, k)
            for point in points:
                #crossover
                parent1_gene[point] = parent2_gene[point]
        return(parent1)

if __name__ == "__main__":
    from config     import get_functions, get_registers, get_constants
    from population import Population
    from selection  import Selection
    inputs = [[0,0],[0,1],[1,0], [1,1]]

    ppl = Population()

    func       = get_functions()
    registers  = get_registers()
    constants  = get_constants(bit=True)
    n_register = 10
    ppl.createPopulation(functions=func, constants=constants, n_ind=5, n_gene=5, n_register=n_register)

    eval_function = lambda x:x[0]^x[1] # xor
    ppl.excute_all(inputs, eval_function)
    
    elite_size = 3
    parents = Selection.elite(ppl, elite_size)

    tourn_size = 3
    n_ind = 5
    for i in range(n_ind):
        parent = Selection.tournament(ppl, tourn_size)
        parents.append(parent)
        parent.show()

    cross_rate = 0.7
    print("..crossover onePoint")
    child = Crossover.onePoint(parents, cross_rate)
    child.show()
    print("..Done!")

    print("..crossover twoPoints")
    child = Crossover.twoPoints(parents, cross_rate)
    child.show()
    print("..Done!")

    print("..crossover randomPoints")
    child = Crossover.randomPoints(parents, cross_rate)
    child.show()
    print("..Done!")
