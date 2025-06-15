a = [2, 4, 7, 10]
b = [2, 3]


# for i in range(len(b) - 1, -1, -1):

#     if a[-1] > b[i]:
#         last = a[-1]
#         j = len(a) - 2

#         while j >= 0 and a[j] > b[i]:
#             a[j + 1] = a[j]
#             j -= 1

#         a[j + 1] = b[i]
#         b[i] = last

# print(a)
# print(b)

# i = len(a) - 1
# j = 0


# while i >= 0 and j < len(b):

#     if a[i] > b[j]:
#         a[i], b[j] = b[j], a[i]
#     else:
#         i -= 1
#     j += 1
#     i -= 1

# a.sort()
# b.sort()

# print(a, b)


n = len(a)
m = len(b)
gap = (n + m + 1) // 2


while gap > 0:
    i = 0
    j = gap

    while j < n + m:
        if j < n and a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
        elif i < n and j >= n and a[i] > b[j - n]:
            a[i], b[j - n] = b[j - n], a[i]
        elif i >= n and b[i - n] > b[j - n]:
            b[i - n], b[j - n] = b[j - n], b[i - n]
        i += 1
        j += 1
    if gap == 1:
        break
    gap = (gap + 1) // 2

print(a, b)
