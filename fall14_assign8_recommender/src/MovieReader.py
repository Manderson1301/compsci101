'''
Created on Nov 25, 2014

@author: Miguel Anderson
'''
def get_data(movieratings):
    MR = open(movieratings)
    itlist = []
    rdict = {}
    for line in MR:
        k = line.strip().split(" ")
        if (k[1]).replace("_"," ") not in itlist:
            itlist.append((k[1]).replace("_"," "))
    itlist.sort()
    MR.close()
    MR = open(movieratings)
    for line in MR:
        k = line.strip().split(" ")
        if k[0] not in rdict.keys():
            rdict[k[0]] = [0]*len(itlist)
        for (i,x) in enumerate(itlist):
            if x == (k[1]).replace("_"," "):
                rdict[k[0]][i] = int(k[2])
    MR.close()
    return itlist, rdict

#print get_data('movieratings.txt')