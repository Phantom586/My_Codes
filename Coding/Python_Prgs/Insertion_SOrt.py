
def Insertion_Sort(lst):

    for i in range(1, len(lst)):
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
    return lst



if __name__ == '__main__':
    inp = list(input('Enter the Elements of the List :').split(' '))
    result = Insertion_Sort(inp)
    print('The Sorted List is :')
    print(result)