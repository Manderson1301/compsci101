'''
Created on Nov 28, 2014

@author: Miguel Anderson
'''
def edit(entry):
    for (i,m) in enumerate(entry):
        entry[i] = sorted(m.split(" "))
    check = 0
    for (f,g) in enumerate(entry):
        if check == 1:
            break
        else:
            for (j,h) in enumerate(entry):
                if f != j and len(set(h)&set(g))>=2:
                    check = 1
                    break
    if check == 1:
        for (f,g) in enumerate(entry):
            for (j,h) in enumerate(entry):
                if f != j and len(set(h)&set(g))>=2:
                    if f>j:
                        entry.pop(f)
                        entry.pop(j)
                    else:
                        entry.pop(j)
                        entry.pop(f)
                    entry.append(list(set(h)|set(g)))
                    break
        for (r,q) in enumerate(entry):
            entry[r] = " ".join(q)
        entry = edit(entry)
    else:
        for (r,q) in enumerate(entry):
            entry[r] = " ".join(q)
    return sorted(entry)  
