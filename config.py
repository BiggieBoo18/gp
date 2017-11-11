import random
import itertools
from   function import Function

def get_registers(n_register=10):
    # A-Z, AB, CD, EF, GH, IJ, KL
    alphabet  = [chr(i) for i in range(65, 65+26)]
    c         = int(n_register/26)
    registers = [alphabet]
    cur       = alphabet
    for i in range(c):
        cur = registers[-1]
        registers.append(["".join([i, j]) for i, j in list(itertools.product(cur, alphabet))])
    registers = [reg for regs in registers for reg in regs][:n_register]
    registers = {reg:0 for reg in registers}
    return (registers)

def get_constants(lower=-10, upper=10, bit=False):
    if (bit):
        constant = {"c":lambda:random.choice([0, 1])}
    else:
        constant = {"c":lambda:random.uniform(lower, upper)}
    return (constant)

def get_functions():
    func = Function()
    """
    func.setFunction("+", 2, lambda x: x[0]+x[1])
    func.setFunction("-", 2, lambda x: x[0]-x[1])
    func.setFunction("*", 2, lambda x: x[0]*x[1])
    func.setFunction("/", 2, lambda x: x[0]/x[1] if (x[0]!=0 and x[1]!=0) else 0)
    """
    func.setFunction("and",  2, lambda x: x[0]&x[1])
    func.setFunction("or",   2, lambda x: x[0]|x[1])
    func.setFunction("not",  1, lambda x: ~x[0])
    return (func)

if __name__ == "__main__":
    registers = get_registers(30)
    print(registers)
    constant  = get_constants()
    print(constant, constant["c"]())
    func      = get_functions()
    print(func.show())
