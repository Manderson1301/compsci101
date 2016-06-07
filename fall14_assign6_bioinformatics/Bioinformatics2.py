'''
Created on Nov 1, 2014

@author: Miguel Anderson
'''
from Bioinformatics import CODONS
from Bioinformatics import AMINO_ACIDS
from Bioinformatics import createdictionary
from Bioinformatics import STOP_CODONS
from Bioinformatics import findRegion
from Bioinformatics import reversecomp



def translateDNAtoProtein (dna):
    """
    given a string composed only of lowercase letters 'gcta', 
    return a string of uppercase letters that represents the 
    longest protein found first within that string or its 
    reverse complement, or the empty string if no protein can
    be found
    """
    dictionary = createdictionary(CODONS,AMINO_ACIDS)
    print "The DNA strand is " + "\n" + dna
    print ""
    print "The reverse compliment is " + reversecomp(dna)
    print ""
    b = "forward"
    reg = findLongestRegion(dna,b)
    b = "reversed"
    rev = findLongestRegion(reversecomp(dna),b)
    if reg == None and rev == None:
        print "This DNA does not code a protein forward or backward"
        return
    elif reg == None:
        longest = rev
        y = "(In reverse order)"
    elif rev == None:
        longest = reg
        y = "(In original order)"
    elif len(rev)>len(reg):
        longest = rev
        y = "(In reverse order)"
    else:
        longest = reg
        y = "(In original order)"
    print "The longest possible protein strand is" + "\n" + longest + "\n" + y
    print ""
    
    longest = [(longest[i-2]+longest[i-1]+longest[i]) for i in range(2,len(longest),3)]
    protein = []
    for x in longest:
        protein.append(dictionary[x])
    end = "".join(protein)
    
    print "The protein of this longest strand is" + "\n" + end
    return end

def findLongestRegion (dna,b):
    all = [findRegion(dna)]
    while all[-1] != "":
        dna = dna[(3+dna.find("atg")):]
        all.append(findRegion(dna))
    all.pop(-1)
    if all == []:
        print "There are no possible "+ b + " protein codings"
        print ""
        return 
    print "The possible protein codings " + b + " are"
    print all
    print ""
    return max(all, key=len)
