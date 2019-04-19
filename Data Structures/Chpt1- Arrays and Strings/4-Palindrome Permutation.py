"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

from collections import defaultdict


def palindrome_permutation(s):
    odd_count = 0
    d = defaultdict(int)
    for i in s:
        d[i] += 1
        if d[i] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1
    return print(odd_count <= 1)


palindrome_permutation("tactcoa")
