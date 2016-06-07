'''
Created on Sep 25, 2014

@author: Miguel Anderson
'''
import InputGUI as Input
import string

 
    
def write_words(file, words):
    """
    output given words to the file (and also to the console)
     - words is a list of lists,
       where each sublist represents a line to write
     - file is a file open for writing
    write each sublist to the file
    with words on a line separated by whitespace
    and each sublist of words on a line
    """
    # TODO: modify this function to write output to file in addition to printing it

    for line in words:
        for w in line:
            print w + " ",
            file.write(w + " ",)
        file.write("\n")
        print


def transform(words, func):
    '''
    apply func each word in words and return the result
     - words is a list of lists,
       where each sublist represents a line from the original file
     - the result is a list of lists, 
       where in each sublist each word has been 
       transformed by applying func to the word
    '''
    # TODO: change each word in the list of lists, using func to accomplish the change
    # FOR EXAMPLE:

    newWords = words[:]                 # copy list
    x = -1
    for line in words:
        x += 1
        for w in range(0,len(line)):
            newWords[x][w] = func(words[x][w])
    return newWords

def get_words (file):
    '''
    returns all words in file as a list of lists, 
    where each nested list is one line from file, 
    words in line as elements of nested list
    '''
    returnlist = [ ]
    for line in file.readlines():
        returnlist += [line.split()]
    return returnlist

def unpigify (word):
    '''Decode from Pig-latin into English.
       Note, when transforming the string word, 
             do not change its capitalization or punctuation.
       Note, since some words may represent multiple different English words, 
             choose the final English word you think is more common.
    '''
    v = "aeiouAEIOU"
    qs = "qQ"
    if word[-3] == "w":
        return word[0:-4]
    elif word[-4] in qs:
        return word[-4:-2] + word[0:-4]
    else:
        x = word.find("-")
        return word[x+1:-2]+word[0:x]


def rot13encode (words):
    '''ROT-13 substitution cipher (both encodes and decodes).
       Note, since this transformation is symmetrical, 
       it can serve as encoder and decoder for the same message.
    '''
    # TODO: complete this function so that it returns a new version of the string word, 
    #       with each letter rotated by 13 places.
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    b = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    neww=""
    for ch in range(0,len(words)):
        if words[ch] in string.letters:
            neww+=b[a.find(words[ch])]
        else:
            neww+=words[ch]
    return neww


def check(words):
    totalnumberofwords=0
    pigcounter = 0
    rotcounter = 0
    x = -1
    v = "aeiouAEIOU"
    runs=0
    for line in words:
        for w in range(0,len(line)):
            totalnumberofwords+=1
    while pigcounter<(totalnumberofwords/10) and rotcounter <(totalnumberofwords/10) and runs <=(totalnumberofwords/2): #onetenth of words check for half the words
        for line in words:
            x += 1
            for w in range(0,len(line)):
                runs +=1
                if words[x][w][-2:] == "ay":
                    pigcounter += 1
                else:
                    for letter in words[x][w]:
                        vowelnoncount=0
                        if letter not in v:
                            vowelnoncount += 1
                    if vowelnoncount == len(words[x][w]):
                        rotcounter+=1
    if pigcounter<(totalnumberofwords/10) and rotcounter< (totalnumberofwords/10):
        return None
    elif pigcounter >= (totalnumberofwords/10):
        return unpigify
    elif rotcounter >= (totalnumberofwords/10):
        return rot13encode
    
    
def Untransform_file ():
    """
    do the work for this program: 
      - prompt user for file
      - prompt user for transform function
      - apply transform to each word
      - write transformed data to a file specified by user
    """
    file = Input.choose_file_to_open()
    if file == None:
        return
    words = get_words(file)
    file.close()
    
    func = check(words)
    if func == None:
        print None
        return
    twords = transform(words, func)
    
    file = Input.choose_file_to_save()
    if file == None:
        return
    write_words(file, twords)
    file.close();

# the main function
Untransform_file()