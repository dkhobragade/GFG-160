arr = [0, -1, 2, -3, 1]

# temp = []
# n = len(arr)

# for i in range(n - 2):
#     for j in range(i + 1, n - 1):
#         for k in range(j + 1, n):
#             if arr[i] + arr[j] + arr[k] == 0:
#                 temp.append([i, j, k])
# print(temp)

res = set()
n = len(arr)
mp = {}


for i in range(n):
    for j in range(i + 1, n):
        a = arr[i] + arr[j]
        if a not in mp:
            mp[a] = []
        mp[a].append((i, j))

for i in range(n):
    rem = -arr[i]
    if rem in mp:
        for p in mp[rem]:
            if p[0] != i and p[1] != i:
                curr = sorted([i, p[0], p[1]])
                res.add(tuple(curr))
print(res)
print([list(triplet) for triplet in res])

print(mp)
