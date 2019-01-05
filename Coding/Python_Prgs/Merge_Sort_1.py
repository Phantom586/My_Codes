
def Merge_Sort_Slice(lst):
    n = len(lst) // 2
    if n == 1:
        return lst
    L = Merge_Sort_Slice(lst[ : n])
    R = Merge_Sort_Slice(lst[n : ])
    return Merge_Sort(L, R)

def Merge_Sort(L, R):
    result = []
    l = r = 0
    while l < len(L) or r < len(R):
        if l < len(L) and ( r >= len(R) or L[l] <= R[r]):
            result.append(L[l])
            l += 1
        else:
            result.append(R[r])
            r += 1
    return result

if __name__ == '__main__':
    inp = list(input('Enter the Elements of the List :').split(' '))
    result = list(Merge_Sort_Slice(inp))
    print('Sorted List is :')
    print(result)