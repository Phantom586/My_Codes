
def compress(lst):
    lst1 = []
    result = []
    lst1.append(lst[0])
    for i in range(1, len(lst) + 1):
        c = 1
        print("Outer", i)
        while(lst[i] == lst[i-1]):
            c += 1
            i += 1
            print("Inner", i)
        result.append((c, lst[i-1]))
        lst1.append(lst[i])





if __name__ == "__main__":
    lst = list(map(int, input()))
    compress(lst)