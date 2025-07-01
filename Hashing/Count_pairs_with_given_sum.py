arr = [1, 1, 1, 1]
target = 2

# count = 0

# for i in range(1, len(arr) - 1):
#     for j in range(len(arr) - 1):
#         if arr[i] + arr[j] == target:
#             count += 1


# print(count)

# left = 0
# right = len(arr) - 1
# count = 0
# while left < right:

#     if arr[left] + arr[right] < target:
#         left += 1
#     elif arr[left] + arr[right] > target:
#         right += 1
#     else:
#         co1 = 0
#         co2 = 0
#         ele1 = arr[left]
#         ele2 = arr[right]

#         while left <= right and arr[left] == ele2:
#             co1 += 1
#             left += 1

#         while left <= right and arr[right] == ele2:
#             co2 += 1
#             right -= 1

#         if ele1 == ele2:
#             count += (co1 * (co1 - 1)) // 2
#         else:
#             count += co1 * co2
# print(count)


freq = {}
count = 0

for i in range(len(arr)):
    if (target - arr[i]) in freq:
        count += freq[target - arr[i]]
    freq[arr[i]] = freq.get(arr[i], 0) + 1
print(count)
