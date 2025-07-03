a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]

s = []

for i in range(len(a)):
    if (a[i] in b) and a[i] not in s:
        s.append(a[i])

print(s)
