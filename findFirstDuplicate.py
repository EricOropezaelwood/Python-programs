# Find the first duplicate in a given array
# Author: Eric Oropezaelwood

"""Given an array a that contains only numbers in the range from 1 to a.length, find 
the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, return the number for 
which the second occurrence has a smaller index than the second occurrence of the 
other number does. If there are no such elements, return -1.
"""

def firstDuplicate(a):

    dupOne = {}
    dupTwo = {}
    
    for idx, c in enumerate(a):
        if c not in dupOne:
            dupOne[c] = idx
        # not the first
        else:
            if c not in dupTwo:
                # add idx of first duplicate
                dupTwo[c] = idx
            else:
                pass
    # look at the second entries
    if len(dupTwo) == 0:
        return -1
    else:
        # minimum
        answer = min(dupTwo.keys(), key=(lambda k: dupTwo[k]))
        return answer