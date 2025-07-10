arr = [7, 2, 5, 3]
target = 8


count = 0

arr.sort()


left = 0
right = len(arr) - 1


while left < right:
    if arr[left] + arr[right] < target:
        count += right - left
        left += 1
    else:
        right -= 1

print(count)
