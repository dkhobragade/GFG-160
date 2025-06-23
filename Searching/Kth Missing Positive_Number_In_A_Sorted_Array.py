arr = [2, 3, 4, 7, 11]
k = 5

low = 0
high = len(arr) - 1

res = len(arr) + k

while low <= high:
    mid = (low + high) // 2

    if arr[mid] > mid + k:
        res = mid + k
        high = mid - 1
    else:
        low = mid + 1
print(res)
