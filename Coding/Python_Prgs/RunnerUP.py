#Prints the Second last of the Array

if __name__ == '__main__':
    n = int(input())
    # mapping the input as integers and casting them into a list
    arr = list(map(int, input().split()))
    # removing duplicate elements and retrieving modified arr into a list(arr)
    arr = list(set(arr))
    # Sorting the list
    arr.sort()
    # Printing the Second Runner Up
    print(arr[-2])
