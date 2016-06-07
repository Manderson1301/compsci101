'''
Created on Oct 21, 2014

@author: Miguel Anderson
'''
def namesForYear(courses, year):
    answer = set()
    for i in range(len(courses)):
        courses[i] = (courses[i]).split(":")
    for i in range(len(courses)):
        for j in range(len(courses[i])):
            if year == courses[i][j]:
                answer |= set([courses[i][j-1]])
    answer = sorted((":".join(answer)).split(":"))
    
    return " ".join(answer)