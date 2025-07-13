arr = [10, 21, 22, 100, 101, 200, 300]

count = 0
arr.sort()


for i in range(2, len(arr)):

    left = 0
    right = i - 1

    while left < right:
        if arr[left] + arr[right] > arr[i]:
            count += right - left
            right -= 1
        else:
            left += 1

print(count)
