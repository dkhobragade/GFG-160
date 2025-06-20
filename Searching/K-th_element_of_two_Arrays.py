a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

i = 0
j = 0
last = 0
while k != 0:
    if i < len(a):
        if a[i] > b[j]:
            last = b[j]
            j += 1
        else:
            last = a[i]
        i += 1
    elif j < len(b):
        last = b[j]
        j += 1

    k -= 1
print(last)
