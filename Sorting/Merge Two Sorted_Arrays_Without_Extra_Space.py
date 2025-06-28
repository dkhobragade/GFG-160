a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]

left = 0
right = 0
temp = []

while left <= len(a) - 1 and right <= len(b) - 1:
    if a[left] >= b[right]:
        temp.append(b[right])
        right += 1
    else:
        temp.append(a[left])
        left += 1

while left <= len(a) - 1:
    temp.append(a[left])
    left += 1

while right <= len(b) - 1:
    temp.append(b[right])
    right += 1
print(temp)
