arr = [10, 30, 20, 5]
target = 25

arr.sort()

left = 0
right = len(arr) - 1
res = []
minDiff = float("inf")


while left < right:
    sum = arr[left] + arr[right]

    if abs(sum - target) < minDiff:
        minDiff = abs(sum - target)
        res = [arr[left], arr[right]]

    elif abs(sum - target) == minDiff:
        if (arr[right] - arr[left]) > (res[1] - res[0]):
            res = [arr[left], arr[right]]

    if sum < target:
        left += 1
    elif sum > target:
        right -= 1
    else:
        break

print(res)
