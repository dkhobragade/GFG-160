arr = [8, -8, 9, -9, 10, -11, 12]

totalSum = 0
curmax = 0
curmin = 0
maxSum = arr[0]
minSum = arr[0]

for i in range(len(arr)):
    curmax = max(curmax + arr[i], arr[i])
    maxSum = max(maxSum, curmax)

    curmin = min(curmin + arr[i], arr[i])
    minSum = min(minSum, curmin)

    totalSum += arr[i]

normalSum = maxSum
circularSum = totalSum - minSum

if minSum == totalSum:
    print(normalSum)
else:
    print(max(normalSum, circularSum))
