#coding: utf-8

import random

class Function(object):
    def __init__(self):
        self.f    = {
            'x' : [0, None], # only one input x, can't yet input x, y, ...
            'c' : [0, None],
        }
        self.keys = None

    def createFunction(self, name, n_arg, f, check_zero=False):
        self.f[name] = [n_arg, f]
        self.keys    = list(self.f.keys())

    def getFunctionDict(self):
        return (self.f)
    
    def getRandomFunction(self, not_arg_zero=False):
        if (not_arg_zero):
            n_arg = 0
            while (n_arg==0):
                f_name = random.choice(self.keys)
                n_arg  = self.f[f_name][0]
                f      = self.f[f_name][1]
        else:
            f_name = random.choice(self.keys)
            n_arg  = self.f[f_name][0]
            f      = self.f[f_name][1]
        return (f_name, n_arg, f)

    def show(self):
        print("f:    ", self.f)
        print("keys: ", self.keys)

class Node(object):
    def __init__(self):
        self.node_id  = ""
        self.f_name   = None
        self.n_arg    = None
        self.f        = None
        self.parent   = None
        self.children = []

    def setNodeId(self, node_id):
        self.node_id = node_id
        
    def getNodeId(self):
        return (self.node_id)
        
    def setFunction(self, f_name, n_arg, f):
        self.f_name = f_name
        self.n_arg  = n_arg
        self.f      = f

    def getFunction(self):
        return (self.f_name, self.n_arg, self.f)

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return (self.parent)

    def addChildren(self, children):
        self.children.append(children)

    def getChildren(self):
        return (self.children)

    def excute(self, args):
        return (self.f(args))

    def show(self):
        print("node:     ", self)
        print("node_id:  ", self.node_id)
        print("f_name:   ", self.f_name)
        print("n_arg:    ", self.n_arg)
        print("f:        ", self.f)
        print("parent:   ", self.parent)
        print("children: ", self.children)

class Tree(object):
    def __init__(self):
        self.root      = None
        self.node_list = []

    def setRoot(self, root):
        self.root = root

    def getRoot(self):
        return (self.root)

    def addNodeList(self, node):
        self.node_list.append(node)
        
    def getNodeList(self):
        return (self.node_list)

    def getNodeListByFunction(self, f_name):
        node_list        = self.getNodeList()
        return_node_list = []
        for node in node_list:
            node_f_name, _, _ = node.getFunction()
            if (node_f_name==f_name):
                return_node_list.append(node)
        return (return_node_list)

    def build(self, inputs, Function, width=None, depth=None, number_of_node=10):
        # set root
        f_name, n_arg, f = Function.getRandomFunction()
        root             = Node()
        root.setNodeId("0")
        root.setFunction(f_name, n_arg, f)
        self.setRoot(root)
        self.addNodeList(root)

        # build tree
        if (n_arg==0):
            DONE  = True
        else:
            DONE  = False
        number_of_node = len(inputs)*number_of_node
        n_node    = random.randint(1, len(inputs)*number_of_node)
        node_list = self.getNodeList()
        i         = 0
        while (not(DONE)):
            cur_node     = node_list[i]
            children     = cur_node.getChildren()
            _, n_arg, _  = cur_node.getFunction()
            if (len(children)<n_arg):
                new_node = Node()
                f_name, n_arg, f = Function.getRandomFunction(not_arg_zero=True)
                new_node.setNodeId("{0}{1}".format(cur_node.getNodeId(), len(children)))
                new_node.setFunction(f_name, n_arg, f)
                new_node.setParent(cur_node)
                cur_node.addChildren(new_node)
                self.addNodeList(new_node)
            else:
                i += 1
                if (i==number_of_node):
                    DONE = True
        # set 'x' or 'c' to build tree
        node_list = self.getNodeList()
        for node in node_list:
            children = node.getChildren()
            if (len(children)==0):
                r = random.randint(0, 1)
                l = self.getNodeListByFunction('x')
                if (r==0 or len(l)<len(inputs)):
                    node.setFunction('x', 0, None)
                else:
                    node.setFunction('c', 0, None)

    def show(self):
        print("root: "     , self.root)
        print("node_list: ", self.node_list)
        for node in self.node_list:
            print("---------------")
            node.show()
            print("---------------")

if __name__ == "__main__":
    tree = Tree()
    tree.show()
    function = Function()
    function.createFunction('+', 2, lambda a:a[0]+a[1])
    function.createFunction('-', 2, lambda a:a[0]-a[1])
    function.createFunction('*', 2, lambda a:a[0]*a[1])
    function.createFunction('/', 2, lambda a:a[0]/a[1] if a[1]!=0 else 0)
    function.show()
    
    inputs    = [i for i in range(1)]
    tree.build(inputs, function)
    node_list = tree.getNodeList()
    x_nodes   = tree.getNodeListByFunction('x')
    tree.show()
