import random
from   function import  Function
class Node(object):
    def __init__(self):
        self.data = [] # data in node

    def createNode(self, function, registers, f_name=None):
        """
        create a node

        :param Function function: set up functions
        :param list registers:    registers is save location for calculation result
        :param str f_name:        function name
        """
        f = function.getFunction()
        register_keys = list(registers.keys())
        if (f_name==None):
            f_names = function.getKeys(not_zero=True)
            f_name  = random.choice(f_names)
        if (register_keys==None):
            operands = [random.choice(['x', 'c', 'A']) for i in range(f[f_name][0])]
            register = 'A'
        else:
            operands = [random.choice(['x', 'c'] + register_keys) for i in range(f[f_name][0])]
            register = random.choice(register_keys)
        self.data = [f_name, operands, register]
        
    def getData(self):
        return (self.data)

    def show(self):
        print("data: ", self.data)

if __name__ == "__main__":
    from config import get_registers
    print("..set up functions")
    func = Function()
    func.setFunction("+", 2, lambda x: x[0]+x[1])
    func.setFunction("-", 2, lambda x: x[0]-x[1])
    func.setFunction("*", 2, lambda x: x[0]*x[1])
    func.setFunction("/", 2, lambda x: x[0]/x[1] if (x[0]!=0 and x[1]!=0) else 0)
    func.show()
    print("..Done!")

    print("..create Node class")
    node = Node()
    node.show()
    print("..Done!")

    print("..create Node")
    registers = get_registers()
    node.createNode(func, registers, f_name=None)
    node.show()
    print("..Done!")
