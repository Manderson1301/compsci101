'''
Created on Nov 25, 2014

@author: Miguel Anderson
'''
def get_data(books, ratings):
    B = open(books)
    itlist = [line.strip() for line in B]
    B.close()
    R = open(ratings)
    rdict = {} 
    c = 0                   #counter for odd/even lines to get either name or ratings
    lastperson = ""
    for line in R:
        c += 1
        if c % 2 == 1:
            if line.strip() not in rdict.keys():
                rdict[line.strip()] = []
                lastperson = line.strip()
        elif c % 2 == 0:
            rdict[lastperson] = [int(r) for r in line.strip().split(" ")]
    R.close()

    return itlist, rdict

#print get_data('books.txt','bookratings.txt')