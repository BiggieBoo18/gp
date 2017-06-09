import random
from   individual import Individual
from   config     import get_registers

class Population(object):
    def __init__(self):
        self.p = None

    def createPopulation(self, functions, constants, n_ind, n_gene, n_register):
        self.p = []
        for i in range(n_ind):
            ind = Individual(functions, constants, n_register)
            ind.createGene(random.randint(1,n_gene))
            self.p.append(ind)

    def setPopulation(self, p):
        self.p = p
        
    def getPopulation(self):
        return (self.p)

    def excute_all(self, inputs, eval_function, mode="min"):
        for ind in self.p:
            ind.calcFitness(inputs, eval_function)
        reverse = True
        if (mode!="max"):
            reverse = False
        self.p = sorted(self.p, key=lambda x:x.getFitness(), reverse=reverse)

    def show(self):
        print("p: ", self.p)

    def result(self):
        for ind in self.p:
            print("fitness:   ", ind.getFitness())
            print("registers: ", ind.getRegisters())
            for i, node in enumerate(ind.getGene()):
                print("gene{0}:     ".format(i), node.getData())

if __name__ == "__main__":
    from config   import get_functions, get_registers, get_constants
    print("..set up functions")
    inputs = [[0,0],[0,1],[1,0], [1,1]]
    func = get_functions()
    print("..Done!")

    print("..create Population")
    ppl = Population()
    ppl.show()
    print("..Done!")

    print("..create Population")
    constants  = get_constants(bit=True)
    n_register = 10
    ppl.createPopulation(functions=func, constants=constants, n_ind=5, n_gene=5, n_register=n_register)
    ppl.show()
    print("..Done!")

    print("..excute all")
    eval_function = lambda x:x[0]^x[1] # xor
    ppl.excute_all(inputs, eval_function)
    ppl.show()
    print("..Done!")

    p = ppl.getPopulation()
    for ind in p:
        ind.show()
