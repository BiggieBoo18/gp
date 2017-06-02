#coding: utf-8

import argparse
from readDataset import readDataset
from individual  import Individual
from population  import Population
from select      import Select
from crossover   import Crossover
from mutation    import Mutation
import six
if (six.PY2):
    from ga4py2  import GA
if (six.PY3):
    from ga4py3  import GA
from copy        import deepcopy
import tree

class Sin(GA):
    def evaluate(self, ind, args):
        fitness = sum(ind)
        return (fitness)

    def revolution(self, args):
        #config
        if   (args.crossmode=="one"):
            cross_func = Crossover.onePoint
        elif (args.crossmode=="two"):
            cross_func = Crossover.twoPoints
        else:
            cross_func = Crossover.randomPoints

        function = tree.Function()
        function.createFunction('+', 2, lambda a:a[0]+a[1])
        function.createFunction('-', 2, lambda a:a[0]-a[1])
        function.createFunction('*', 2, lambda a:a[0]*a[1])
        function.createFunction('/', 2, lambda a:a[0]/a[1] if a[1]!=0 else 0)
        inputs   = [i for i in range(10)]

        # Create individuals & population
        ppl = Population()
        for i in range(args.individuals):
            individual = Individual()
            individual.createGene(inputs, function, args.gene)
            ppl.addInd(individual)

        # Evolution
        for i in range(args.revolution):
            # Evaluation population in individuals
            ppl.calcFitness(self.evaluate)
            if ((i%10)==0):
                ppl.show()

            # Select parents
            if (args.elite):
                parents = Select.Elite(ppl, args.esize, args.mode)
                parents.extend(Select.Tournament(ppl, args.individuals-args.esize, args.tornsize, args.mode))
            else:
                parents = Select.Tournament(ppl, args.individuals, args.tornsize, args.mode)

            # Clossover
            children = cross_func(parents, args.individuals, args.gene, args.crossrate)

            # Mutation
            children = Mutation.mutation(children, args.mutaterate, dataset)
            # Swap children
            ppl.setPpl(children)
            
        # show result
        ppl.calcFitness(self.evaluate)
        ppl.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ind",      "--individuals", type=int, default=50,                     help="Number of individuals")
    parser.add_argument("-gene",     "--gene",        type=int, default=10,                     help="Length of gene")
    parser.add_argument("-revo" ,    "--revolution",  type=int, default=100,                    help="Number of revolution")
    parser.add_argument("-elite",    "--elite",                 default=False,                  help="Use elite selection", action="store_true")
    parser.add_argument("-esize",    "--esize",       type=int, default=2,                      help="Size of elite")
    parser.add_argument("-tornsize", "--tornsize",    type=int, default=3,                      help="Size of tournament")
    parser.add_argument("-mode",     "--mode",        type=str, default="max",                  help="Max or min")
    parser.add_argument("-crate",    "--crossrate",   type=float , default=0.7,                 help="probability of crossover")
    parser.add_argument("-cmode",    "--crossmode",   type=str, default="one",                  help="one or two or random")
    parser.add_argument("-mrate",    "--mutaterate",  type=float,  default=0.05,                 help="probability of mutation")
    args   = parser.parse_args()
    print("[argments list]")
    print(args)
    sin = Sin()
    sin.revolution(args)
