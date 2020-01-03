
def find_prefix(pattern, m, prefArray):
    length = 0
    prefArray[0] = 0
    for i in range(1, m):
        if pattern[i] == pattern[length]:
            length += 1
            prefArray[i] = length
        else:
            if length is not 0:
                length = prefArray[length - 1]
                i -= 1
            else:
                prefArray[i] = 0


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    find_prefix(pattern, m, prefArray)
    i, j = 0, 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            print(f"There is a pattern at location {i - j}")
            j = prefArray[j - 1]
        elif i < n and pattern[j] is not text[i]:
            if j is not 0:
                j = prefArray[j - 1]
            else:
                i += 1


text = input()
pattern = input()
prefArray = [0] * len(pattern)
kmp(text, pattern)
