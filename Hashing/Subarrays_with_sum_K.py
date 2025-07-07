arr = [10, 2, -2, -20, 10]
k = -10


# count = 0
# for i in range(len(arr)):
#     sum = 0
#     for j in range(i, len(arr)):
#         sum += arr[j]
#         if sum == k:
#             count += 1
# print(count)

prefixSum = {}
count = 0
curSum = 0


for i in arr:
    curSum += i

    if curSum == k:
        count += 1

    if curSum - k in prefixSum:
        count += prefixSum[curSum - k]

    prefixSum[curSum] = prefixSum.get(curSum, 0) + 1

print(count)
