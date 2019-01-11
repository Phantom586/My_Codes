# importing the Textwrap Library.
import textwrap

def wrap(string, max_width):
    # Using the wrap method to obtain a list of characters of a specific length.
    str = textwrap.wrap(string, max_width)
    # Printing the elements of the list.
    for i in str:
        print(i)
    return ''

if __name__ == '__main__':
    # Using Unpacking to Input a String and a Width.
    string, max_width = input(), int(input())
    # Calling the wrap function and retrieving the return value in the result variable.
    result = wrap(string, max_width)
    print(result)