"""
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, pie -> false
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return print(False)
    if len(s2) > len(s1):
        return one_away(s2, s1)
    i, j, different = 0, 0, False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if different:
                return print(False)
            different = True
            if len(s1) == len(s2):
                j += 1
        else:
            j += 1
        i += 1
    return print(True)


one_away("pale", "pie")
one_away("pale", "pales")
one_away("pale", "bale")
one_away("pale", "bake")
