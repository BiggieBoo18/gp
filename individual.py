import copy
import random
from   config import get_registers
from   node   import Node

class Individual(object):
    """
    Individual class
    """
    def __init__(self, functions, constants, n_register=10):
        self.gene       = None                      # gene with list
        self.fitness    = None                      # fitness with int
        self.functions  = functions                 # set up functions
        self.constants  = constants                 # set up constants
        self.registers  = get_registers(n_register) # registers with list

    def createGene(self, n_gene):
        """
        create gene
        
        :param int n_gene: number of gene
        """
        self.gene = []
        for i in range(n_gene):
            node = Node()
            node.createNode(self.functions, self.registers, self.constants, f_name=None)
            self.gene.append(node)

    def getGene(self):
        return (self.gene)

    def setFitness(self, fitness):
        self.fitness = fitness

    def getFitness(self):
        return (self.fitness)

    def calcFitness(self, inputs, eval_function): # <!> logistic only now
        n_data = len(inputs)
        mse    = 0
        for x in inputs: # input == ex.[[0,0], [0,1], [1,0], [0,0]]
            ind = copy.copy(self)
            ind.excute(x)
            output = ind.registers['A'] # <!> output is 'A' register, othreway mean each register..
            y      = eval_function(x)
            mse   += (output-y)**2
        mse = mse/float(n_data)
        fit = mse
        self.setFitness(fit)
        
    def getRegisters(self):
        return (self.registers)
    
    def excute(self, x):
        functions = self.functions.getFunction()
        x_len     = len(x)
        x_cur     = 0
        for node in self.gene:
            data = node.getData()
            operator = data[0]
            ops_keys = data[1]
            save_to  = data[2] # save to register key
            constant = data[3]
            ops = []
            ops_append = ops.append
            for op_key in ops_keys: # ops_keys is register_keys or constants as 'c' or inputs as 'x'
                if (op_key in self.registers):
                    ops_append(self.registers[op_key])
                elif (op_key in self.constants):
                    ops_append(constant)
                elif (op_key=='x'):
                    ops_append(x[x_cur])
                    x_cur += 1
                    if (x_cur==x_len):
                        x_cur = 0
            f_data   = functions[operator]
            function = f_data[1]             # function with lambda
            result   = function(ops)         # excute
            self.registers[save_to] = result # save result to register

    def show(self):
        print("self:      ", self)
        print("gene:      ", self.gene)
        print("fitness:   ", self.fitness)
        print("function:  ", self.functions)
        print("constants: ", self.constants)
        print("registers: ", self.registers)

if __name__ == "__main__":
    from function import Function
    from config   import get_functions, get_registers, get_constants
    inputs = [[0,0],[0,1],[1,0], [1,1]]
    print("..set up functions")
    func = get_functions()

    print("..create Individual")
    registers = get_registers()
    constants = get_constants(lower=-10, upper=10)
    ind = Individual(func, constants)
    ind.show()
    ind.createGene(5)
    ind.show()
    print("..Done!")

    print("..excute Individual")
    ind.excute(inputs[0])
    ind.show()
    print("..Done!")

    print("..calc fitness")
    eval_function = lambda x:x[0]^x[1] # xor
    ind.calcFitness(inputs, eval_function)
    ind.show()
    print("..Done!")    
