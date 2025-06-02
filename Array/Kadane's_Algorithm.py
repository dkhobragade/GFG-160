arr = [-2, -4]


res = arr[0]
maxE = arr[0]

for i in range(1, len(arr)):
    maxE = max(arr[i], arr[i] + maxE)
    res = max(res, maxE)
print(res)
