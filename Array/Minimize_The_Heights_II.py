arr = [3, 9, 12, 16, 20]
k = 3

arr.sort()

res = arr[-1] - arr[0]

for i in range(1, len(arr)):
    if arr[i] - k < 0:
        continue

    minH = min(arr[0] + k, arr[i] - k)

    maxH = max(arr[i - 1] + k, arr[len(arr) - 1] - k)

    res = min(res, maxH - minH)

print(res)
