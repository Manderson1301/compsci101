'''
Created on Feb 15, 2011, modified on Sep 18, 2014

You need to complete this file.



@author: ola, rcd, rodger
@author: Miguel Anderson
'''


# This import is added to help you with file I/O
import InputGUI as Input


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


def transform_file ():
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
    
    func = Input.choose_transform()
    if func == None:
        return
    twords = transform(words, func)
    
    file = Input.choose_file_to_save()
    if file == None:
        return
    write_words(file, twords)
    file.close();


# the main function
transform_file()
