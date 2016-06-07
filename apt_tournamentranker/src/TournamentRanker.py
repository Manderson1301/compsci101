'''
Created on Dec 2, 2014

@author: Miguel Anderson
'''
def rankTeams(names,lostTo):
    d = {}
    J = []
    a = []
    for t in names:
        d[t] = lostTo.count(t)
    J = [x for x in d.items()]
    if len(d.keys())==len(set(d.values())):
        J = sorted(J, key = lambda x: x[1], reverse=True)
        for u in J:
            a.append(u[0])
    else:      
        n = lostTo.index("")
        a.append(names[n]) 
        for Y in range(max(d.values())):
            compare = []
            for (q,w) in d.iteritems():
                if w == max(d.values()) - Y - 1:
                    compare.append(q)
            if len(compare) == 1:
                a.append(compare[0])
            else:
                f = []
                for r in compare:
                    f.append((r,d[lostTo[names.index(r)]]))
                f = sorted(f, key = lambda x: x[1], reverse=True)
                for G in range(max(d.values())):
                    compareagain = []
                    for (b,p) in f:
                        if p == max(d.values()) - G:
                            compareagain.append(b)
                    if len(compareagain) == 1:
                        a.append(compareagain[0])
                    else:
                        z = []
                        for pp in compareagain:
                            z.append((pp,a.index(lostTo[names.index(pp)])))
                        z = sorted(z, key = lambda x: x[1])
                        for dd in z:
                            a.append(dd[0])
    return a