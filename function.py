class Function(object):
    def __init__(self):
        self.f = {"c" : [0, None],
                  "x" : [0, None]}

    def setFunction(self, f_name, n_args, f):
        self.f[f_name] = [n_args, f]

    def getFunction(self, not_zero=False):
        return (self.f)

    def getKeys(self, not_zero=False):
        keys = list(self.f.keys())
        if (not_zero):
            keys = []
            for key, val in self.f.items():
                args = val[0]
                if (args!=0):
                    keys.append(key)
        return (keys)

    def show(self):
        print(self.f)

if __name__ == "__main__":
    func = Function()
    func.show()
    func.setFunction("+", 2, lambda x: x[0]+x[1])
    func.setFunction("-", 2, lambda x: x[0]-x[1])
    func.setFunction("*", 2, lambda x: x[0]*x[1])
    func.setFunction("/", 2, lambda x: x[0]/x[1] if (x[0]!=0 and x[1]!=0) else 0)
    func.show()
    print(func.getKeys())
    print(func.getKeys(not_zero=True))
