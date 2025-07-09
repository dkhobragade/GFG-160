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


# for i in range(n):
#     newTarget = arr[i] - target

#     left = i + 1
#     right = n - 1

#     while left < right:
#         if arr[left] + arr[right] == target:
#             count += 1
#             left += 1
#             right -= 1
#         elif arr[left] + arr[right] < target:
#             left += 1
#         else:
#             right -= 1

# print(count)


for i in range(n - 2):

    left = i + 1
    right = n - 1

    while left < right:

        sum = arr[left] + arr[right] + arr[i]

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            ele1 = arr[left]
            ele2 = arr[right]

            cnt1 = 0
            cnt2 = 0

            while left <= right and arr[left] == ele1:
                cnt1 += 1
                left += 1

            while left <= right and arr[right] == ele2:
                cnt2 += 1
                right -= 1

            if ele1 == ele2:
                count += (cnt1 * (cnt1 - 1)) // 2
            else:
                count += cnt1 * cnt2

print(count)
