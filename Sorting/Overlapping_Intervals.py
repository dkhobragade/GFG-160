arr = [[1, 3], [2, 4], [9, 10], [6, 8]]

n = len(arr)

# Normal
# res = []
# for i in range(n):
#     start = arr[i][0]
#     end = arr[i][1]

#     if res and res[-1][1] >= end:
#         continue

#     for j in range(i + 1, n):
#         if arr[j][0] <= end:
#             end = max(end, arr[j][1])

#     res.append([start, end])
# print(res)

# ExtraSpace-O(n)

arr.sort()

res = []
res.append(arr[0])

for i in range(1, n):
    last = res[-1]
    cur = arr[i]

    if cur[0] <= last[1]:
        last[1] = max(last[1], cur[1])
    else:
        res.append(cur)

print(res)

# Inpalce - O(1)
