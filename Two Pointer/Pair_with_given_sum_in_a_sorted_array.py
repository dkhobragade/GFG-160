arr = [1, 1, 1, 1]
target = 2

# count = 0

# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if arr[i] + arr[j] == target:
#             count += 1

# print(count)

count = 0

left = 0
right = len(arr) - 1


while left < right:
    if arr[left] + arr[right] > target:
        right -= 1
    elif arr[left] + arr[right] < target:
        left += 1

    else:
        cnt1 = 0
        cnt2 = 0
        ele1 = arr[left]
        ele2 = arr[right]

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
