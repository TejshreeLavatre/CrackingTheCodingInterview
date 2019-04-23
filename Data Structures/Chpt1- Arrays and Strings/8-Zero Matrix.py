"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""


def zero(matrix):
    m_row = len(matrix)
    n_col = len(matrix[0])
    is_col = False
    for i in range(m_row):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, n_col):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, m_row):
        for j in range(1, n_col):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(n_col):
            matrix[0][j] = 0
    if is_col:
        for i in range(m_row):
            matrix[i][0] = 0
    return print(matrix)


zero([[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12]])
