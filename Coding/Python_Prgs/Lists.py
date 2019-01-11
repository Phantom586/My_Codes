if __name__ == '__main__':
    # Inputting The no. of operations user wants to perform.
    N = int(input())
    # list to store the Elements after performing operations on it.
    mine = []
    # for loop for N operations.
    for i in range(N):
        # List to Store the operation and their required values.
        com = list(input().split())
        # now matching the type of operation the user wants to perform and working according to that.
        if com[0] == 'insert':
            # Inserting the Element stored in list(com[2]) at index(com[1]).
            mine.insert(int(com[1]),int(com[2]))
        elif com[0] == 'print':
            print(mine)
        elif com[0] == 'remove':
            # Converting the String into an Integer value.
            n1 = int(com[1])
            # Deleting the First Occurrence of the Integer(com[1]).
            mine.pop(mine.index(n1))
        elif com[0] == 'append':
            # Converting the String into an Integer value.
            n1 = int(com[1])
            mine.append(n1)
        elif com[0] == 'sort':
            # Sorting the List.
            mine.sort()
        elif com[0] == 'pop':
            # Removing the last element of the list.
            mine.pop()
        elif com[0] == 'reverse':
            # Reversing the List.
            mine.reverse()
