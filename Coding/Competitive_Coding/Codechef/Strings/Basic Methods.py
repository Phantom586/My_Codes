# # These are some Basic methods of Strings in Python3
#
# # Method - 1 : find("string", beg, end)
# It returns “-1 ” if string is not found in given range.
# It returns first occurrence of string if found.
# Desc - Finds the first occurrence of the given String.

str = "My name is Phantom Boy. I'm an Awesome Boy"
# print(str.find("Phantom"))

# # Method - 2 : rfind("string", beg, end)
# Desc - Finds the last occurrence of the given String.
# print(str.rfind("Boy"))

# # Method - 3 : startswith("string", beg, end)
# Desc - Returns True if the function begins with the mentioned String(prefix)
# print(str.startswith("My"))

# # Method - 4 : endswith("string", beg, end)
# Desc - returns True if the function ends with the mentioned string(suffix)
# print(str.endswith("Me"))

# # Method - 5 : islower()
# Desc - returns True if all the letters in string are lower cased
# print(str.islower())

# # Method - 6 : isupper()
# Desc - returns True if all the letters in string are upper cased
# print(str.isupper())

# # Method - 7 : lower()
# Desc - returns new string with all the letters lower cased.
# print(str.lower())

# # Method - 8 : upper("string")
# Desc - returns new string with all the letters upper cased.
# print(str.upper())

# # Method - 9 : swapcase()
# Desc - swaps the cases of the string i.e., upper case is converted to lower case and vice-versa
# print(str.swapcase())

# # Method - 10 : title()
# Desc - Converts the first letter of every word to Uppercase.
# print(str.title())

# # Method - 11 : count("string", beg=0, end=len(str))
# Desc - counts th occurrence of the given substring in whole string.
# print(str.count("Boy"))
# print(str.count("Boy", 0, 26))

# # Method - 12 : center(width, fillchar=' ')
# Desc - surrounds the string with a character repeated both sides of the string multiple times.
# str1 = "hello"
# print(str1.center(len(str), "B"))

# # Method - 13 : ljust(width, fillchar=' ')
# Desc - returns the original string shifted to the left that has a character at its right.
# print(str1.ljust(5, '-')), currently not working somehow

# # Method - 14 : isalpha()
# Desc - returns True when all the characters in the string are alphabets.
# print(str.isalpha())

# # Method - 15 : isalnum()
# Desc - returns True when all the characters in the string are combination of numbers and alphabets.
# print(str.isalnum())

# # Method - 16 : isspace()
# Desc - returns True when all the characters in the string are spaces.
# print(str.isspace())

# # Method - 17 : join()
# Desc - joins a sequence of string mentioned in its arguments with the string
# s1 = ['my ', 'name ', 'is harsh']
# print(''.join(s1))

# # Method - 18 : strip(sep=' ')
# Desc - used to delete all the leading and trailing characters mentioned in the args.
# str1 = "BBHello Guys!BBB"
# print(str1.strip('B'))

# # Method - 19 : lstrip(sep=' ')
# Desc -  used to delete all the leading characters mentioned in the args.
# str1 = "BBHello Guys!BBB"
# print(str1.lstrip('B'))

# # Method - 20 : rstrip(sep=' ')
# Desc -  used to delete all the trailing characters mentioned in the args.
# str1 = "BBHello Guys!BBB"
# print(str1.rstrip('B'))

# # Method - 21 : min("string")
# Desc - returns minimum value alphabet from the string
# str1 = "hello"
# print(min(str1))

# # Method - 22 : max("string")
# Desc - returns maximum value alphabet from the string
# str1 = "hello"
# print(max(str1))
