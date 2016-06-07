'''
Created on Nov 19, 2014

@author: Miguel Anderson
'''
def maximumFacts(sus):
    a = [x.split(",") for x in sus]
    x = set()
    max = 0
    for (j,jj) in enumerate(a):
        for (k,kk) in enumerate(a):
            if k!=j:
                if kk == jj and len(kk)>max:
                    max = len(kk)
                elif len(set(kk)&set(jj)) > max:
                    max = len(set(kk)&set(jj))
                    x = set(kk)&set(jj)

    return max
                