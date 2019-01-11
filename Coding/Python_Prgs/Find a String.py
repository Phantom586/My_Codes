def count_substring(string, sub_string):
    # Calculating the length of the substring.
    l = len(sub_string)
    # Initializing the counter variable to zero.
    c = 0
    # For loop to Iterate the String and make a Substring from its ith position to (i+l)position and then matching it with the substring.
    for i in range(len(string)):
        # Creating the Substring.
        sub = string[i:(i + l)]
        # Matching it with the Provided Substring
        if sub == sub_string:
            # If it matched increasing the counter to 1.
            c += 1
    return c


if __name__ == '__main__':
    # Inputting a String and Removing its WhiteSpaces.
    string = input().strip()
    # Inputting a Substring that is to be searched(removing all the WhiteSpaces).
    sub_string = input().strip()
    # Calling the Function count_substring and retrieving the return value in variable count.
    count = count_substring(string, sub_string)
    print(count)