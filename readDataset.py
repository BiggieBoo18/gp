#coding: utf-8

def readDataset(dpath):
    """
    Read dataset
    
    example.
    --------------
    [binary.txt]
    0
    1
    EOF
    --------------
    dataset = readDataset("binary.txt") # [0, 1]
    
    :param dpath: to dataset path
    :type dpath:  str
    :return:      return dataset for individual
    :rtype:       list
    """
    dataset = None

    fd      = open(dpath)
    dataset = [int(d.strip()) for d in fd.readlines()]
    
    return (dataset)

if __name__ == "__main__":
    dpath = "./dataset/binary.txt"
    dataset = readDataset(dpath)
    print(dataset)
