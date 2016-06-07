'''
Created on Nov 14, 2014

@author: Miguel Anderson
'''
import random

def load_lines(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    lines = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        lines.append(line)
    return lines
    
    
def get_words(filename, wordlength = 5):
    """
    returns a list of words having a specified length from
    the file whose name is filename.
    default length is 5 (if parameter not specified)
    """
    lines = load_lines(filename)
    wlist = [w for w in lines if len(w) == wordlength]
    return wlist

def get_file(filename): # doesn't account or ask for word length
    lines = load_lines(filename)
    wlist = [w for w in lines]
    return wlist

def pickcategory(): #prompts user to pick category
    print "Your choices for hangman categories are:"
    print "(1) US Presidents"
    print "(2) Sports"
    print "(3) Types of Pies"
    print "(4) dictionary words"
    print "Type the number of which category of words would you like to play with: ",
    cat = int(raw_input())
    while (cat != 1) & (cat !=2) & (cat != 3) & (cat != 4):
        print "Please select a number between 1 and 4:",
        cat = int(raw_input())
    if cat == 4:
        return catword("lowerwords.txt",2,22)  # the numbers following are the lengths of the words in the each file
    elif cat == 1:
        return catword("uspresidents.txt",10,25)
    elif cat == 2:
        return catword("sports.txt",4,10)
    elif cat == 3:
        return catword("pie.txt",7,18)

def catword(file,low,high):
    print "The category you picked has words ranging from length " + str(low) + " and length " + str(high)
    print "How long would you like your word to be?",
    n = int(raw_input())
    while n not in range(low,high+1):
        print "Please pick a length within length " + str(low) + " and length " + str(high) + ":",
        n = int(raw_input())
    words = get_words(file,n)
    print "There %d words whose length is %d in this database" % (len(words),n)
    return [random.choice(words),words]

def numofguesses(): #asks for guesses
    print "How many guesses do you want?",
    x = int(raw_input())
    return x

def getgoodguess(inputthing,alreadywrong,alreadyright): #checks to see whether inputted value is a letter and whether it was guessed already
    while inputthing not in "abcdefghijklmnopqrstuvwxyz" or inputthing in alreadywrong or inputthing in alreadyright:
        if inputthing not in "abcdefghijklmnopqrstuvwxyz":
            print "please pick a single letter a as guess:",
            inputthing = str(raw_input())
        if inputthing in alreadyright or inputthing in alreadywrong:
            print "You already guessed that. Please guess a new letter:",
            inputthing = str(raw_input())
    return inputthing

def cheat(guessed,justguessed,sofarright,parameters):
    # guessed are letters incorrectly guessed
    # just guessed is the letter just guessed
    # sofarright is the list of what the user has so far
    # parameters is a list with the secret word first and a list of all possible words (by length) second
    
    for i in guessed:
        for (k,x) in enumerate(parameters[1]):
            if i in x:
                parameters[1].pop(k)     #pop ones that have the missed letters
    for (e,r) in enumerate(sofarright):
        if (r != "_") & (r != " "):
            for (u,h) in enumerate(parameters[1]):
                if h[e] != r:
                    parameters[1].pop(u)     #pop ones without the letter just guessed
    d = {}
    d[-1] = [p for p in parameters[1] if justguessed not in p]
    for i in range(len(parameters[0])):
        d[i] = []
        for w in parameters[1]:
            if w[i] == justguessed:
                d[i].append(w)
    maxa = 0
    for y in d.values():
        if len(y) > maxa:
            maxa = len(y)
            bank = y   # pick biggest back
    parameters[0] = random.choice(bank)
    parameters[1] = bank
    return parameters
    
    
def game():
    slist = pickcategory()
    secret = slist[0]
    guessnum = numofguesses()
    trynum = 0
    guessed = set()
    secretlist = ["_"] * len(secret) # create empty guessing spots
    for i in range(len(secret)): #fill in spaces so that they don't get in the way
        if secret[i]==" ":
            secretlist[i] = " "
    print "Remember if you think you know the word type it all out"
    while "".join(secretlist)[:] != secret and trynum<=guessnum:
        print secret
        print " "
        print " "
        print " ".join(secretlist)
        print "Misses left: " + str(guessnum-trynum)
        print "Incorrect guesses: " + str(", ".join(guessed))
        print "Guess letter:",
        k = str(raw_input())
        if k.lower() == secret.lower(): #in the case where the word is guessed in its entirety
            print "WOW"
            print "You got the whole thing right!!"
            print "You even had " + str(guessnum - trynum) + " guesses left!"
            return
        else:
            k = getgoodguess(k, guessed, secretlist) #check if valid guess
            if k not in secret.lower(): # if incorrect guess
                print "Nope, no " + k
                trynum += 1
                guessed |= set(k)
                if guessnum - trynum == 0:
                    print " "
                    print "Well that's awkward, you just got hanged"
                    print "The word was actually " + secret
                    return
            else: # if correct guess
                slist = cheat(guessed,k,secretlist,slist)
                secret = slist[0]
                if k not in secret.lower(): # if incorrect guess
                    print "Nope, no " + k
                    trynum += 1
                    guessed |= set(k)
                    if guessnum - trynum == 0:
                        print " "
                        print "Well that's awkward, you just got hanged"
                        print "The word was actually " + secret
                        return
                else:
                    for i in range(len(secret)):
                        if k == secret[i].lower():
                            secretlist[i] = secret[i] #replace guessing spot with correct guess
    if "".join(secretlist)[:] == secret: #if all letters guessed correctly, but individually
        print " "
        print " "
        print "The secret word was " + "".join(secretlist)
        print "You guessed it correctly with only " + str(trynum) + " incorrect guesses"
        print "YOSHAAA!!!!!"
        return
        
        
if __name__ == "__main__":
    game()
    

