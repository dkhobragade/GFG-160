arr = [-3, -1, -1, 0, 1, 2]
target = -2


n = len(arr)
count = 0

# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if arr[i] + arr[j] + arr[k] == target:
#                 count += 1
# print(count)


for i in range(n):
    newTarget = arr[i] - target

    left = i + 1
    right = n - 1

    while left < right:
        if arr[left] + arr[right] == target:
            count += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

print(count)
