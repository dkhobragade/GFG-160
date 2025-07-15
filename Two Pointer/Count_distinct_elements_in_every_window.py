from collections import defaultdict

arr = [1, 2, 1, 3, 4, 2, 3]
k = 4

# res = []
# freq = defaultdict(int)

# for i in range(k):
#     freq[arr[i]] += 1

# res.append(len(freq))

# for i in range(k, len(arr)):
#     freq[arr[i]] += 1
#     freq[arr[i - k]] -= 1

#     if freq[arr[i - k]] == 0:
#         del freq[arr[i - k]]

#     res.append(len(freq))
# print(res)

n = len(arr)
res = []

freq = {}

for i in range(k):
    if arr[i] in freq:
        freq[arr[i]] += 1
    else:
        freq[arr[i]] = 1

res.append(len(freq))


for i in range(k, n):
    outgoing = arr[i - k]
    freq[outgoing] -= 1

    if freq[outgoing] == 0:
        del freq[outgoing]

    incoming = arr[i]
    if incoming in freq:
        freq[incoming] += 1
    else:
        freq[incoming] = 1

    res.append(len(freq))

print(res)
