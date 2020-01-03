# The Problem - https://www.hackerrank.com/challenges/encryption/problem

import math


def encryption(s):
    length = len(s)
    res = math.sqrt(length)
    row = math.floor(res)
    col = math.ceil(res)
    if row * col < length:
        row += 1
    matrix = [0] * row
    i, j = 0, 0
    while j < row and i < length:
        st = list(s[i : (i + col)])
        matrix[j] = st
        i += col
        j += 1
    encoded_msg = ""
    for i in range(col):
        for j in range(row):
            try:
                tmp = matrix[j][i]
                encoded_msg += tmp
            except IndexError:
                pass
        encoded_msg += " "
    return encoded_msg


s = input()
res = encryption(s)
print(res)
