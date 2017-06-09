import random

class Selection(object):
    @classmethod
    def elite(self, population, elite_size):
        p     = population.getPopulation()
        elite = p[:elite_size] # sorted
        return (elite)

    @classmethod
    def tournament(self, population, tourn_size, mode="min"):
        p         = population.getPopulation()
        candidate = []

        f = min
        if (mode!="max"):
            f = max
        for i in range(tourn_size):
            candidate.append(random.choice(p))
        parent = f(candidate, key=lambda x:x.getFitness())
        return (parent)

if __name__ == "__main__":
    from function   import Function
    from config     import get_functions, get_registers, get_constants
    from population import Population
    inputs = [[0,0],[0,1],[1,0], [1,1]]

    ppl = Population()

    func       = get_functions()
    registers  = get_registers()
    constants  = get_constants(bit=True)
    n_register = 10
    ppl.createPopulation(functions=func, constants=constants, n_ind=5, n_gene=5, n_register=n_register)

    eval_function = lambda x:x[0]^x[1] # xor
    ppl.excute_all(inputs, eval_function)
    
    print("..select elite")
    elite_size = 3
    elite = Selection.elite(ppl, elite_size)
    print("elite: ", elite)
    print("..Done!")

    print("..select tournament")
    tourn_size = 3
    parents    = Selection.tournament(ppl, tourn_size)
    print("parents: ", parents)
    print("..Done!")
