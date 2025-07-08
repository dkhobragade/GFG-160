arr = [4, 2, 2, 6, 4]
k = 6


# count = 0

# for i in range(len(arr)):
#     ans = 0
#     for j in range(i, len(arr)):
#         ans ^= arr[j]

#         if ans == k:
#             count += 1
# print(count)

count = 0
mp = {}
pefixXOR = 0


for val in arr:
    pefixXOR ^= val

    count += mp.get(pefixXOR ^ k, 0)

    if pefixXOR == k:
        count += 1

    mp[pefixXOR] = mp.get(pefixXOR, 0) + 1

print(count)
