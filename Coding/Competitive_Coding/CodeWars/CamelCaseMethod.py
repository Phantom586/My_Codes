# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings.
# All words must have their first letter capitalized without spaces.

# For instance:

# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord


# def camel_case(string):
#     str = ''
#     for i in string.split():
#         a = list(i)
#         a[0] = a[0].upper()
#         str += ''.join(a)
#     print(str)


# Improved Solution
def camel_case(string):
    print(string.title().replace(" ", ""))


camel_case("camel case method")
camel_case(" camel case word")