arr = [3, 2, 1, 56, 10000, 167]

minI = float("inf")
maxI = float("-inf")

for i in arr:
    if i > maxI:
        maxI = i
    if i < minI:
        minI = i

print(minI, maxI)
