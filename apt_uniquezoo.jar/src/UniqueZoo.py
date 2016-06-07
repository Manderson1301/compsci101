'''
Created on Oct 9, 2014

@author: Miguel Anderson
'''
def numberUnique(zoos):
    list = range(len(zoos))
    counter = 0
    for i in range(len(zoos)):
        list[i] = set(zoos[i].split())
        answer = list[:]
    for k in range(len(zoos)):
        for l in range(len(zoos)):
            if k!=l:
                answer[k] = answer[k] - list[l]
    for k in range(len(answer)):
        if answer[k]!=set():
            counter+=1
    return counter
