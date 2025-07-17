arr = [3, 0, 1, 0, 4, 0, 2]

left = 1
right = len(arr) - 2


mleft = arr[left - 1]
mright = arr[right + 1]
res = 0

while left <= right:

    if mright <= mleft:
        res += max(0, mright - arr[right])
        mright = max(mright, arr[right])
        right -= 1
    else:
        res += max(0, mleft - arr[left])
        mleft = max(mleft, arr[left])
        left += 1

print(res)
