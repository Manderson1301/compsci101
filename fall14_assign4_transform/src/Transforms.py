'''
All possible transform functions.

You need to complete this file.

Those whose name starts with transform_ will appear in the menu option.
You can write as many helper functions as you want to support these primary functions.

Created on Sep 18, 2014



@author: Miguel Anderson
'''
import string


def transform_identity (word):
    '''Identity transform (no change).
       Note, this simply serves as an example transform.
    '''
    return word


def transform_uppercase (word):
    '''Transform to UPPERCASE (no decode).
       Note, this simply serves as an example transform.
    '''
    return word.upper()


def transform_pigify (word):
    '''Encode into Pig-latin from English.
       Note, when transforming the string word, 
             do not change its capitalization or punctuation.
       Note, this transformation is not unique, 
             some different words may be transformed into the same pig-latin word.
    '''
    # TODO: complete this function so that it returns a new version of the string word,
    #       assuming word is in English, use the rules of pig-latin to encode the word
    v = "aeiouAEIOU"
    qs = "qQ"
    if word[0] in v:
        return word + "-way"
    elif word[0] in qs:
        return word[2:] + "-quay"
    else:
        for y in range(1,len(word)):
            if word[y] in v:
                return word[y:len(word)]+"-"+word[0:y]+"ay"
        return word + "-way"


def transform_unpigify (word):
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


def transform_rot13 (words):
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

