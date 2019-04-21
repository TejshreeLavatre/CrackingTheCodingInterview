"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3, If the "compressed" string would not become
smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""


def compress_string(s):
    compressed = []
    consecutive_count = 0
    i = 0
    while i < len(s):
        char = s[i]
        while i < len(s) and s[i] == char:
            consecutive_count += 1
            i += 1
        compressed.append(char)
        compressed.append(str(consecutive_count))
        consecutive_count = 0
    new_s = "".join(compressed)
    return print(new_s) if len(s) > len(new_s) else print(s)


compress_string("aABBbbccccCC")
compress_string("aabcccccaaa")
