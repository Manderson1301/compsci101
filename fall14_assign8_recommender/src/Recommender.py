'''
Created on Nov 25, 2014

@author: Miguel Anderson
'''
import BookReader
import MovieReader
import FoodReader

def average(items,ratings):
    endtup = []
    for (i,T) in enumerate(items):
        n = 0
        su = 0
        for D in ratings.values():
            if D[i] != 0:
                su += D[i]
                n += 1
        if n == 0: # make average zero if no ratings
            av = 0
        else:
            av = su/n
        endtup.append((T,av))
    return sorted(endtup, key = lambda x: x[1], reverse=True)
    
def similarities(name, ratings):
    endtup = []
    for (i,D) in ratings.iteritems():
        dot = 0
        if i != name:
            for (n,k) in enumerate(D):
                dot += ratings[name][n]*k #add the multiplication of the score by the weight (0s will give 0)
            endtup.append((i,dot))
    return sorted(endtup, key = lambda x: x[1], reverse=True)

def recommended(slist,items,ratings,n):
    slist = slist[:n]
    endtup = []
    speeps = {}
    for L in ratings.keys():
        if L in slist:
            speeps[L] = ratings[L]
    for y in range(len(items)):
        we = 0
        for g in slist:
            we += ratings[g[0]][y]*g[1]     # add score multiplied by weight g[1]
        endtup.append((items[y],we))
    return sorted(endtup, key = lambda x: x[1], reverse=True)

def allav(category): #category has to be 'foods', 'movies', or 'books'
    print "The average ratings for each item reviewed is (in decreasing order):"
    if category == 'foods':
        (items,ratings) = FoodReader.get_data('foods.txt')
    elif category == 'movies':
        (items,ratings) = MovieReader.get_data('movieratings.txt')
    elif category == 'books':
        (items,ratings) = BookReader.get_data('books.txt', 'bookratings.txt')
    print average(items,ratings)
    print ""

def closeusers(name,category):
    print name + "'s closest matches are these (in decreasing order):"
    if category == 'foods':
        (items,ratings) = FoodReader.get_data('foods.txt')
    elif category == 'movies':
        (items,ratings) = MovieReader.get_data('movieratings.txt')
    elif category == 'books':
        (items,ratings) = BookReader.get_data('books.txt', 'bookratings.txt')
    print similarities(name,ratings)
    print ""
    
def top(name,category,m,nraters): 
    #'m' are how many recommendations someone wants
    #'nraters' are how many raters one wants to use to compile the list
    print name + " is most recommended these " + str(m) + " item(s) reviewed based on the " + str(nraters) + " closest rater(s):"
    if category == 'foods':
        (items,ratings) = FoodReader.get_data('foods.txt')
    elif category == 'movies':
        (items,ratings) = MovieReader.get_data('movieratings.txt')
    elif category == 'books':
        (items,ratings) = BookReader.get_data('books.txt', 'bookratings.txt')
    print recommended(similarities(name,ratings),items,ratings,nraters)[:m]
    print ""
    
category = 'books' # set category, make sure to change name accordingly
name = 'Megan'
allav(category)
closeusers(name,category)
for u in range(1,21):
    top(name,category,5,u) # the last integer parameter is what is referred to as "n" in the assignment