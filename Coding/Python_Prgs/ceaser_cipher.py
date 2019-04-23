import math
import os
import random
import re
import sys


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result

    return wrapper


# Complete the caesarCipher function below.
@my_timer
def caesarCipher(s, k):
    str = list(s)
    s1 = []
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            s1.append(chr(97 + (ord(i) - 97 + k) % 26))
        elif ord(i) >= 65 and ord(i) <= 90:
            s1.append(chr(65 + (ord(i) - 65 + k) % 26))
        else:
            s1.append(i)
    return (''.join(s1))


if __name__ == '__main__':

    print(__name__)

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result + '\n')