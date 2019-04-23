def average(array):
    # your code goes here
    arr = list(set(array))
    s = sum(arr)
    l = len(arr)
    return (s/l)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)