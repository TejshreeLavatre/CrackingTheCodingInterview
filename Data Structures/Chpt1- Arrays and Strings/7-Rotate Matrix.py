"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method
to rotate the image by 90 degrees. Can you do this in place?
"""


def rotate(matrix):
    l = len(matrix)
    if l == 0 or l != len(matrix[0]):
        return print(False)
    for layer in range(l//2):
        first, last = layer, l - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
    return print(matrix)


rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

"""
     0   1   2   3

0    1   2   3   4
1    5   6   7   8
2    9   10  11  12
3    13  14  15  16  



     0   1   2   3

0    13   9    5   1
1    14   10   6   2
2    15   11   7   3
3    16   12   8   4  


"""