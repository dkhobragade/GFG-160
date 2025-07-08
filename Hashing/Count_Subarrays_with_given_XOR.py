arr = [4, 2, 2, 6, 4]
k = 6


count = 0

for i in range(len(arr)):
    ans = 0
    for j in range(i, len(arr)):
        ans ^= arr[j]

        if ans == k:
            count += 1
print(count)
