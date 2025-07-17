arr = [3, 0, 1, 0, 4, 0, 2]
# left = 1
# right = len(arr) - 2


# mleft = arr[left - 1]
# mright = arr[right + 1]
# res = 0

# while left <= right:

#     if mright <= mleft:
#         res += max(0, mright - arr[right])
#         mright = max(mright, arr[right])
#         right -= 1
#     else:
#         res += max(0, mleft - arr[left])
#         mleft = max(mleft, arr[left])
#         left += 1

# print(res)

res = 0

n = len(arr)


prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = max(prefix[i - 1], arr[i])

sufix = [0] * n
sufix[-1] = arr[-1]
for i in range(n - 2, -1, -1):
    sufix[i] = max(sufix[i + 1], arr[i])


for i in range(n):
    trapped = min(prefix[i], sufix[i]) - arr[i]
    if trapped > 0:
        res += trapped

print(res)
