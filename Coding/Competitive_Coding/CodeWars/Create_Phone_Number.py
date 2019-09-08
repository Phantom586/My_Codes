# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parenthesis!
from unittest import TestCase


# def create_phone_number(n):
#     a = [str(i) for i in n[:3]]
#     b = [str(i) for i in n[3:6]]
#     c = [str(i) for i in n[6:]]
#     print(f'({"".join(a)}) {"".join(b)}-{"".join(c)}')


# Improved Version
def create_phone_number(n):
    st = ''.join(map(str, n))
    print(f'({"".join(st[:3])}) {"".join(st[3:6])}-{"".join(st[6:])}')


# (123) 456-7890
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# (111) 111-1111
create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# (123) 456-7890
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# (023) 056-0890
create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
# (000) 000-0000
create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
