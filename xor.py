import random
import gc
import copy
from   config      import get_functions, get_constants
from   population  import Population
from   selection   import Selection
from   crossover   import Crossover
from   mutation    import Mutation
from   progressbar import ProgressBar

# config
gc.enable()
inputs = [[0,0], [0,1], [1,0], [1,1]]
revolution  = 10000
n_register  = 2
n_ind       = 50
n_gene      = 10
elite_size  = 3
tourn_size  = 3
cross_rate  = 0.7
mutate_rate = 0.5
path        = "./result/result.txt"

# init
ppl       = Population()
func      = get_functions()
constants = get_constants(lower=-10, upper=10, bit=True)
ppl.createPopulation(functions=func, constants=constants, n_ind=n_ind, n_gene=n_gene, n_register=n_register)
eval_function = lambda x:x[0]^x[1] # xor
ppl.excute_all(inputs, eval_function)

# revolution
p = ProgressBar(0, revolution)
for i in range(revolution):
    #print("revolution: ", i)
    p.update(i+1)
    elite = Selection.elite(ppl, elite_size)
    new_p = copy.deepcopy(elite)
    for j in range(n_ind-elite_size):
        parent = Selection.tournament(ppl, tourn_size)
        elite.append(parent)
        child = Crossover.randomPoints(elite, cross_rate)
        child = Mutation.mutation(child,  mutate_rate, n_register)
        new_p.append(child)
    ppl.setPopulation(new_p)
    ppl.excute_all(inputs, eval_function)
    if ((i%100)==0):
        ppl.result()
ppl.result()
ppl.write_result(path)
p.finish()
