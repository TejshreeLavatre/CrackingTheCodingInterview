"""
 Assume you have a method isSubstring which checks if one word is a substring of another.
 Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
 [e.g., "water bottle" is a rotation of "erbottlewat")
"""


def isSubstring(s1, s2):
    if len(s1) != len(s2):
        return print(False)
    new_s = s1 + s2
    return print(s2 in new_s)


isSubstring("waterbottle","erbottlewat")
