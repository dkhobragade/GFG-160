arr = [1, 0, 1, 1, 1, 0, 0]

mp = {}

preSum = 0
res = 0

for i in range(len(arr)):

    preSum += -1 if arr[i] == 0 else 1

    if preSum == 0:
        res = i + 1

    if preSum in mp:
        res = max(res, i - mp[preSum])

    else:
        mp[preSum] = i

print(res)
