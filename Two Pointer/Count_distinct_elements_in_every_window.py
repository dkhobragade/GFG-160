from collections import defaultdict

arr = [1, 2, 1, 3, 4, 2, 3]
k = 4

res = []
freq = defaultdict(int)

for i in range(k):
    freq[arr[i]] += 1

print(freq)
res.append(len(freq))

for i in range(k, len(arr)):
    freq[arr[i]] += 1
    freq[arr[i - k]] -= 1

    if freq[arr[i - k]] == 0:
        del freq[arr[i - k]]

    res.append(len(freq))
print(freq)
print(res)
