# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
#  alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)


# def alphabet_position(text):
#     d = {}
#     st = "abcdefghijklmnopqrstuvwxyz"
#     for i in range(1, len(st)+1):
#         d[st[i-1]] = i
#     a = ""
#     for i in text.lower():
#         if i in st:
#             a += str(d[i]) + " "
#     print(a.strip())


# Improved Solution
def alphabet_position(text):
    print(' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()))


# "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
alphabet_position("The sunset sets at twelve o' clock. ")
# "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
alphabet_position("The narwhal bacons at midnight.")
