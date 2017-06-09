import random
from   function import Function

def get_registers(k=10):
    # A-Z, AB, CD, EF, GH, IJ, KL
    registers = {"".join(chr(i)):0 for i in range(65, 65+26)}
    for i in range(66, 66+12, 2):
        registers["".join([chr(i-1), chr(i)])] = 0
    registers = {k:v for k, v in list(registers.items())[:10]}
    if (not('A' in registers)):
        registers['A'] = 0
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
    registers = get_registers()
    print(registers)
    constant  = get_constants()
    print(constant, constant["c"]())
    func      = get_functions()
    print(func.show())
