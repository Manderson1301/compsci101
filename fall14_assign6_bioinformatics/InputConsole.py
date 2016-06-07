'''
Get input interactively from the user.

There is NO need to modify this file.

Created on Sep 16, 2013

@author: rcd
'''
import Bioinformatics as StudentWork

dna = raw_input("Enter DNA string to test: ").strip()

StudentWork.translateDNAtoProtein(dna)
    
