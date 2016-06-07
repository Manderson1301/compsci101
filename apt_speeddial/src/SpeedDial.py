'''
Created on Nov 4, 2014

@author: Miguel Anderson
'''
def assignNumbers(numbers,howMany,slots):
    for (i,x) in enumerate(numbers):
        numbers[i] = len(str(x))
        
    total = sum([(howMany[i]*numbers[i]) for i in range(len(numbers))])
    
    saved = [(howMany[i]*numbers[i] - (2*howMany[i])) for i in range(len(numbers))]
    
    saved_presses = sum(sorted(saved)[-slots:])
    
    return total - saved_presses