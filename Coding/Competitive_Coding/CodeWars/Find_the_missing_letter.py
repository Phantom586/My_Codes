# Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter,
# in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will,
# always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'


def find_missing_letter(chars):
    for i in range(1, len(chars)):
        # print(chars[i-1], chars[i])
        if (ord(chars[i]) - ord(chars[i - 1])) != 1:
            print(chr(ord(chars[i])+1), i)


find_missing_letter(['a','b','c','d','f'])
# find_missing_letter(['O','Q','R','S'])