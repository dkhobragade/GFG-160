citations = [3, 0, 5, 3, 0]

n = len(citations)
freq = [0] * (n + 1)


for citation in citations:
    if citation >= n:
        freq[n] += 1
    else:
        freq[citation] += 1

idx = n

s = freq[n]
while s < idx:
    idx -= 1
    s += freq[idx]

print(idx)
