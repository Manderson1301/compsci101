'''
Created on Oct 3, 2014

@author: Miguel Anderson
'''
def whichOrder(available, orders):
    """
    return zero-based index of first
    sandwich in order, list of strings
    that can be made from ingredients
    in available, list of strings
    """
       
    for x in range(len(orders)):
        counter = 0
        for i in range(len(orders[x].split())):
            if orders[x].split()[i] in available:
                counter +=1
        if counter == len(orders[x].split()):
            return x
    return -1