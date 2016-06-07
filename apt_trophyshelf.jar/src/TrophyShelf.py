'''
Created on Oct 14, 2014

@author: Miguel Anderson
'''
def countVisible(trophies):
    """
    return two-element int list
    based on trophies, an int list
    """
    
    t = trophies
    tprime = t[::-1]
    x = []
    y = []
    m = 0
    counterx = 0
    countery = 0
    for i in range(len(t)):
        if t[i]>m:
            x.append([t[i]])
            m=t[i]
            counterx += 1
    m=0
    for i in range(len(tprime)):
        if tprime[i]>m:
            y.append([tprime[i]])
            m=tprime[i]
            countery += 1
    return [counterx,countery]