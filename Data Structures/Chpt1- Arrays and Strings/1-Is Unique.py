"""
Implement and algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s):
    s = "".join(sorted(s))
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return print(False)
    return print(True)


is_unique("This returns False")
is_unique("NowIs True")
