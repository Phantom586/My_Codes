
n = int(input())
s = input()


## My Solution
# def count_valleys(n, s):
#     sea_level = 0
#     check = False
#     valleys = 0
#     for i in s:
#         if i == "U":
#             sea_level += 1
#             print("one level up : ", sea_level)
#         elif i == "D":
#             sea_level -= 1
#             print("one level down : ", sea_level)
#         if sea_level < 0:
#             print("going down")
#             check = True
#         if check:
#             if sea_level == 0:
#                 print("reached sea_level ", sea_level)
#                 valleys += 1
#                 check = False
#     return valleys

# logic : we just have to see if the current sea_level is 0 and if it's last value was exactly -1,then we could say that
# the person was in a valley and could increase the count of valleys.

## Optimal Solution
def count_valleys(n, s):
    sea_level = 0
    valleys = 0
    tmp = sea_level
    for i in s:
        tmp = sea_level
        if i == "U":
            sea_level += 1
        elif i == "D":
            sea_level -= 1
        if sea_level == 0 and tmp == -1:
            valleys += 1
    return valleys


# count_valleys(n, s)
res = count_valleys(n, s)
print(res)
