'''
Created on Oct 21, 2014

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
    print "Your choices for hangman categories are US Presidents, Sports, Types of Pies, or dictionary words."
    print "Which category of words would you like to play with: ",
    cat = str(raw_input())
    while (cat.lower() != "US Presidents".lower()) & (cat.lower() !="Sports".lower()) & (cat.lower() != "dictionary words".lower()) & (cat.lower() != "Types of Pie".lower()):
        print "Please select either US Presidents, Sports, Types of Pies, or dictionary words:",
        cat = str(raw_input())
    if cat.lower() == "dictionary words".lower():
        return catword()
    elif cat.lower() == "US Presidents".lower():
        return random.choice(get_file("uspresidents.txt"))
    elif cat.lower() == "Sports".lower():
        return random.choice(get_file("sports.txt"))
    elif cat.lower() == "Types of Pie".lower() or cat.lower() == "Types of Pies".lower():
        return random.choice(get_file("pie.txt"))

def catword(): #only called if dictionary word is chosen
    print "How long would you like your word to be?",
    n = int(raw_input())
    words = get_words("lowerwords.txt",n)
    print "There %d words whose length is %d in this database" % (len(words),n)
    return random.choice(words)

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
    
def game():
    secret = pickcategory()
    guessnum = numofguesses()
    trynum = 0
    guessed = set()
    secretlist = ["_"] * len(secret) # create empty guessing spots
    for i in range(len(secret)): #fill in spaces so that they don't get in the way
        if secret[i]==" ":
            secretlist[i] = " "
    print "Remember if you think you know the word type it all out"
    while "".join(secretlist)[:] != secret and trynum<=guessnum:
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
                for i in range(len(secret)):
                    if k == secret[i].lower():
                        secretlist[i] = secret[i] #replace guessing spot with correct guess
    if "".join(secretlist)[:] == secret: #if all leters guessed correctly, but individually
        print " "
        print " "
        print "The secret word was" + "".join(secretlist)
        print "You guessed it correctly with only " + str(trynum) + " incorrect guesses"
        print "YOSHAAA!!!!!"
        return
        
        
if __name__ == "__main__":
    game()
    

