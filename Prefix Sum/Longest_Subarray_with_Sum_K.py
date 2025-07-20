arr = [10, 5, 2, 7, 1, -10]
k = 15


mp = {}
res = 0
prefixSum = 0


for i in range(len(arr)):
    prefixSum += arr[i]

    if prefixSum == k:
        res = i + 1

    elif (prefixSum - k) in mp:
        res = max(res, i - mp[prefixSum - k])

    if prefixSum not in mp:
        mp[prefixSum] = i

print(res)
