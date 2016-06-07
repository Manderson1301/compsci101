'''
Created on Nov 25, 2014

@author: Miguel Anderson
'''
def get_data(food_file):
    ratings = [-5,-3,0,1,3,5]
    itlist = []
    rd = {} # first dictionary used to write from file
    rdict = {} # final dictionary based on rd
    f = open(food_file)
    c = 0                   #counter for odd/even lines to get either name or ratings
    lastperson = ""
    for line in f:
        c += 1
        if c % 2 == 1:
            if line.strip() not in rd.keys():
                rd[line.strip()] = []
                lastperson = line.strip()
        elif c % 2 == 0:
            line = line.strip().split(",")
            for k in line:
                k = k.split(" ")
                if k[0] not in itlist:
                    itlist.append(k[0])
                rd[lastperson].append(k)
    f.close()
    itlist.sort()
    for (y,t) in rd.iteritems():
        rdict[y] = [0] * len(itlist)
        for h in t:
            for (i,x) in enumerate(itlist):
                if h[0] == x:
                    rdict[y][i] = int(h[1])
    return itlist, rdict

#print get_data('foods.txt')