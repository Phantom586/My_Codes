# Code for Vegeneres Cipher

# List of all the Alphabets using List Comprehension
lst = [chr(x) for x in range(65, 91)]

# Creating Vegeneres Table using for loops

# # 2D List to Store the Vegeneres Table
# arr = []
# for i in range(0, 26):
#     # List to store rows Alphabets respective to their Index
#     temp = []
#     c = i
#     for j in range(0, 26):
#         # Appending the Alphabets in the temporary list(row) 
#         temp.append(lst[c % 26])
#         c += 1
#     # now Appending the row in the 2D list
#     arr.append(temp)

# Provide Options
print("Welcome to Ph@ntom's Cipher :::")
print("1 >>> Encrypt")
print("2 >>> Decrypt")

# Input the Plain Text and the Corresponding Key
ch = int(input('>>>'))
if ch == 1:
    print("Enter the Text to be Encrypted")
    # Taking the input and converting into UpperCase
    str = input('-->>>').upper()
    print("Enter the Key")
    # Taking the Key in UpperCase and Converting it into a List 
    Key = list(input("should contain NO Spaces >>>").upper())
    # Length of the Key
    l = len(Key)
    # Removing any Spaces Available in the Plain Text
    # Plain = list("".join(str.split()))
    # List Containing the Cipher Text
    Cipher = []
    for i in range(len(str)):
        if str[i] != ' ':
            k = lst.index(Key[i % l])
            m = lst.index(str[i])
            Cipher.append(lst[(m + k) % 26])
        else:
            Cipher.append(' ')
    
    # Print out the Cipher Text
    print("The Encrypted Text is :::")
    print("".join(Cipher))

elif ch == 2:
    print("Enter the Text to be Derypted")
    # Taking the input and converting into UpperCase
    str = input('-->>>').upper()
    print("Enter the Key")
    # Taking the Key in UpperCase and Converting it into a List 
    Key = list(input("should contain NO Spaces >>>").upper())
    # Length of the Key
    l = len(Key)
    # Removing any Spaces Available in the Encrypted Text
    # Cipher = list("".join(str.split()))
    # List Containing the Decrypted Text
    Decipher = []
    for i in range(len(str)):
        if str[i] != ' ':
            k = lst.index(Key[i % l])
            m = lst.index(str[i])
            Decipher.append(lst[(m - k) % 26])
        else:
            Decipher.append(' ')

    # Print out the Decrypted Text
    print("The Decrypted Text is :::")
    print("".join(Decipher))




