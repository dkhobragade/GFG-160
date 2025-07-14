arr = [1, 2, 3, 7, 5]
target = 12


left = 0
cur_sum = 0
res = []

for right in range(len(arr)):
    cur_sum += arr[right]

    while cur_sum > target and left <= right:
        cur_sum -= arr[left]
        left += 1

    if cur_sum == target:
        res.append(left + 1)
        res.append(right + 1)
        break

print(res)
