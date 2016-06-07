'''
Created on Oct 21, 2014

@author: Miguel Anderson
'''

def one(a,b,c):
    return len(a & b & c)

def two(a,b,c):
    return 2 * len(((a & b) | (a & c)) - (a & b & c))

def three(a,b,c):
    return 3 * len(a - (b | c))

def score(listA,listB,listC):
    setA = set(listA)
    setB = set(listB)
    setC = set(listC)
    x = one(setA,setB,setC)
    scorelist = [x,x,x]

    scorelist[0] += two(setA,setB,setC)
    scorelist[1] += two(setB,setA,setC)
    scorelist[2] += two(setC,setB,setA)
    scorelist[0] += three(setA,setB,setC)
    scorelist[1] += three(setB,setA,setC)
    scorelist[2] += three(setC,setB,setA)
    
    for i in range(len(scorelist)):
        scorelist[i] = str(scorelist[i])
    
    return "/".join(scorelist)
    

        