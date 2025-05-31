arr = [-2, 6, -3, -10, 0, 2]

# curMax = arr[0]
# curMin = arr[0]
# res = arr[0]

# for i in range(1, len(arr)):

#     temp = max(arr[i], arr[i] * curMax, arr[i] * curMin)

#     curMin = min(arr[i], arr[i] * curMax, arr[i] * curMin)

#     curMax = temp

#     res = max(res, curMax)

# print(res)


maxPro = float("-inf")

left = 1
right = 1

for i in range(1, len(arr)):
    if left == 0:
        left = 1
    if right == 0:
        right = 1

    left *= arr[i]

    right *= arr[len(arr) - 1 - i]

    maxPro = max(maxPro, left, right)

print(maxPro)
