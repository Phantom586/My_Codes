test_case = int(input())
lst = list(map(int, input().split()))
for i in range(test_case):
    for j in range(1, lst[i]+1):
        if j % 3 == 0 and j % 5 == 0:
            print("FizzBuzz")
        elif j % 5 == 0:
            print("Buzz")
        elif j % 3 == 0:
            print("Fizz")
        else:
            print(j)