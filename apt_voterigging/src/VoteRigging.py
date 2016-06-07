'''
Created on Oct 28, 2014

@author: Miguel Anderson
'''
def minimumVotes(votes):
    if len(votes) == 1:
        return 0
    myguy = votes[0]
    votes = votes[1:]
    counter = 0
    while myguy<=max(votes):
        votes[votes.index(max(votes))] += -1
        myguy += 1
        counter+=1 
        
        
        
        
        
        
        
    return counter