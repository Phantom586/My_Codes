details = list(map(int, input().split()))
d_toast = (details[1] * details[2])/details[6]
l_toast = details[3] * details[4]
s_toast = details[5]/details[7]
toasts = min(d_toast, l_toast, s_toast)//details[0]
print(int(toasts))