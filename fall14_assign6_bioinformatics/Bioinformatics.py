'''
Created on Sep 17, 2013

@author: rcd
'''
# use these variables to make your code more readable
START_CODON = 'atg'
STOP_CODONS = [ 'taa', 'tag', 'tga' ]
# these next two lists are meant to be used together,
#   i.e., the index of a codon in the first list matches
#         its corresponding amino acid in the second list
# they are taken from this web site:
#   http://en.wikipedia.org/wiki/DNA_codon_table
# and are intended to help you with the problem, 
# so you do not have to hand code the translation yourself
CODONS = [
  'gct', 'gcc', 'gca', 'gcg',
  'tgt', 'tgc', 
  'gat', 'gac',
  'gaa', 'gag', 
  'ttt', 'ttc', 
  'ggt', 'ggc', 'gga', 'ggg',
  'cat', 'cac',
  'att', 'atc', 'ata',
  'aaa', 'aag',
  'ctt', 'ctc', 'cta', 'ctg', 'tta', 'ttg',
  'atg',
  'aat', 'aac',
  'cct', 'ccc', 'cca', 'ccg',
  'caa', 'cag',
  'cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg',
  'agt', 'agc', 'tct', 'tcc', 'tca', 'tcg', 
  'act', 'acc', 'aca', 'acg',
  'gtt', 'gtc', 'gta', 'gtg',
  'tgg',
  'tat', 'tac',
]

AMINO_ACIDS = [ 
  'A', 'A', 'A', 'A', 
  'C', 'C',
  'D', 'D', 
  'E', 'E', 
  'F', 'F',
  'G', 'G', 'G', 'G',
  'H', 'H',
  'I', 'I', 'I',
  'K', 'K', 
  'L', 'L', 'L', 'L', 'L', 'L',
  'M', 
  'N', 'N', 
  'P', 'P', 'P', 'P',
  'Q', 'Q',
  'R', 'R', 'R', 'R', 'R', 'R',
  'S', 'S',  'S', 'S', 'S', 'S',
  'T', 'T', 'T', 'T', 
  'V', 'V', 'V', 'V', 
  'W',
  'Y', 'Y', 
]


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
    reg = findRegion(dna)
    rev = findRegion(reversecomp(dna))
    if reg == "" and rev == "":
        print "This DNA does not code a protein forward or backward"
        return
    elif reg == "":
        print "This DNA does not code a protein forward"
        longest = rev
        y = "(In reverse order)"
    elif rev == "":
        print "This DNA does not code a protein in reverse"
        longest = reg
        y = "(In original order)"
    elif len(rev)>len(reg):
        longest = rev
        y = "(In reverse order)"
    else:
        longest = reg
        y = "(In original order)"
    print "The first longest possible protein strand is" + "\n" + longest + "\n" + y
    print ""
    
    longest = [(longest[i-2]+longest[i-1]+longest[i]) for i in range(2,len(longest),3)]
    protein = []
    for x in longest:
        protein.append(dictionary[x])
    end = "".join(protein)
    
    print "The protein of this first longest strand is" + "\n" + end
    return end

def createdictionary (c,a):
    return dict([(c[x],a[x]) for x in range(len(c))])

def reversecomp(dna):
    l = list(dna)
    l.reverse()
    for x in range(len(l)):
        if l[x] == "a":
            l[x] = 't'
        elif l[x] == "c":
            l[x] = "g"
        elif l[x] == "g":
            l[x] = "c"
        elif l[x] == "t":
            l[x] = "a"
    return "".join(l)

def findRegion(dna):
    if "atg" not in dna:
        return ""
    else:
        dna = dna[(3+dna.find("atg")):]
        l = [(dna[i-2]+dna[i-1]+dna[i]) for i in range(2,len(dna),3)]
    w = [len(l),len(l),len(l)]        
    for (k,t) in enumerate(STOP_CODONS):
        if t in l:
            w[k] = l.index(t)
    if min(w) == len(l):
        return ""
    else:
        final = [l[q] for q in range(min(w))]
        return "".join(final)
    

