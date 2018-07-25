# Author: Eric Oropezaelwood
#
"""
Given a string, find and return the first instance of a non-repeating character in it. If one does not exist, return '_'
"""

def firstNotRepeatingCharacter(s):
    for i, letter in enumerate(s):
        if s.count(letter) == 1:
            return letter
    return '_'