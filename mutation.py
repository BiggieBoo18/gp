import random
from   node   import Node
from   config import get_functions, get_registers, get_constants

class Mutation(object):
    @classmethod
    def mutation(self, child, mutate_rate, n_register, functions, constants):
        if (random.random()<mutate_rate):
            child_gene = child.getGene()
            r = random.random()
            if (r<0.3):                                    # swap
                new_node   = Node()
                new_node.createNode(functions=functions, constants=constants, registers=get_registers(n_register))
                child_gene = child.getGene()
                point = random.choice(range(len(child_gene)))
                child_gene[point] = new_node
            elif (r>0.3 and r<0.6 and len(child_gene)!=1): # remove
                point = random.choice(range(len(child_gene)))
                child_gene.pop(point)
            else:                                          # insert
                new_node   = Node()
                new_node.createNode(functions=functions, constants=constants, registers=get_registers(n_register))
                child_gene = child.getGene()
                point = random.choice(range(len(child_gene)))
                child_gene.insert(point, new_node)
        return(child)

if __name__ == "__main__":
    from config     import get_functions, get_registers, get_constants
    from population import Population
    from selection  import Selection
    from crossover  import Crossover
    inputs = [[0,0],[0,1],[1,0], [1,1]]

    ppl = Population()

    func       = get_functions()
    constants  = get_constants(bit=True)
    n_register = 10
    n_ind      = 5
    n_gene     = 5
    ppl.createPopulation(functions=func, constants=constants, n_ind=5, n_gene=5, n_register=n_register)

    eval_function = lambda x:x[0]^x[1] # xor
    ppl.excute_all(inputs, eval_function)
    
    elite_size = 3
    parents = Selection.elite(ppl, elite_size)

    tourn_size = 3
    for i in range(n_ind):
        parent = Selection.tournament(ppl, tourn_size)
        parents.append(parent)

    cross_rate  = 0.7
    child = Crossover.randomPoints(parents, cross_rate)

    mutate_rate = 0.7 # for debug (In generary, set up like 0.05)
    child.show()
    child = Mutation.mutation(child,  mutate_rate)
    child.show()
