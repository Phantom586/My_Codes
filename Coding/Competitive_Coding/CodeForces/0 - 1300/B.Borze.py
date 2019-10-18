# Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used.
# Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e.
# to find out the ternary number given its representation in Borze alphabet.

# Input
# The first line contains a number in Borze code. The length of the string is between 1 and 200 characters.
# It's guaranteed that the given string is a valid Borze code of some ternary number
# (this number can have leading zeroes).

# Output
# Output the decoded ternary number. It can have leading zeroes.

# Examples
# input
#   .-.--
# output
#   012
# input
#   --.
# output
#   20
# input
#   -..-.--
# Output
#   1012

b_code = input()
i = 0
while i < len(b_code):
    if b_code[i] == '-':
        if b_code[i:i+2] == '-.':
            i += 2
            print(1, end="")
        elif b_code[i:i+2] == '--':
            i += 2
            print(2, end="")
    elif b_code[i] == '.':
        i += 1
        print(0, end="")
