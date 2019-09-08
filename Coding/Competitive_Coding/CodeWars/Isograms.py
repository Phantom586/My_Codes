# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case


# def is_isogram(string):
#     st = string.lower()
#     check = list(set(st))
#     c = 0
#     for i in check:
#         st = st.replace(i, '', 1)
#         if i in st:
#             c += 1
#     if c != 0:
#         print(False)
#     else:
#         print(True)


# Improved Version
def is_isogram(str):
    print(len(str) == len(set(str.lower())))



# True
is_isogram("Dermatoglyphics")
# True
is_isogram("isogram")
#  False, "same chars may not be same case"
is_isogram("moOse")
# False
is_isogram("isIsogram")
# False,  "same chars may not be adjacent"
is_isogram("aba")
#  True, "an empty string is a valid isogram"
is_isogram("")